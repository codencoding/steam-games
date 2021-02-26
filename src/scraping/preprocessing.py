import pandas as pd
import re
import datetime
from scipy.stats import zscore

def dt_convert(dt):
    """Convert release_date to datetime values"""
    if dt is None:
        return None
    try:
        return pd.to_datetime(dt)
    except:
        return None

def get_zscores(col):
    def convert_dt(time):
        if pd.isnull(time):
            return None
        return time.timestamp()

    if isinstance(col.iloc[0], datetime.datetime):
        col = col.apply(convert_dt)
    zscores = zscore(col, nan_policy="omit")
    
    return zscores

def gpu_conv(flops):
    """Convert console gpu measurements to floats"""
    if pd.isna(flops):
        return None
    data = flops.split(' ')
    if data[-1][0] == 'G':
        return float(data[0])
    else:
        return float(data[0]) * 1000

def date_conv(date):
    """Convert dates in console data to datetimes"""
    if pd.isna(date):
        return None
    month, day, year = date.split('/')
    month = int(month)
    day = int(day)
    year = int(year)
    return datetime.datetime(year, month, day)

def mem_extract(string):
    """Process min_memory into interpretable RAM"""
    if pd.isna(string):
        return None
    ram = re.findall(r"(\d+\+?\s?.{1}B)", string)
    if len(ram) == 0:
        return None
    return mem_convert(ram[0])

def mem_convert(ram):
    """Convert RAM measurements to Gigabytes"""
    convert = {
        "GB":1,
        "MB":0.001
    }
    measure = ram[-2:]
    num = int(re.findall(r"\d+", ram)[0])
    return num * convert[measure]

def hrtz_convert(hrtz):
    if pd.isna(hrtz):
        return None
    measure = re.findall(r"\+?\s?(\D+)", hrtz)[-1][0].lower()
    num = float(re.findall(r"(\d\.?\d*)", hrtz)[0])
    if measure == 'g':
        return num
    elif measure == 'm':
        return num * 0.001

def proc_num_lookup(proc_num, cpus):
    cpu = cpus[cpus["Processor_Number"].str.contains(proc_num)]
    if cpu.shape[0] == 0:
        return None
    cpu = cpu.iloc[0].dropna()
    if "Max_Turbo_Frequency" in cpu.index:
        return cpu["Max_Turbo_Frequency"]
    elif "Processor_Base_Frequency" in cpu.index:
        return cpu["Processor_Base_Frequency"]
    return None

def get_cpu_speed(cpu_str, cpus):
    if pd.isna(cpu_str):
        return None
    
    cpu_speed = re.findall(r"(\d+\.?,?\d*\+?\s?(?i:[g|m]hz))\s?", cpu_str)
    if len(cpu_speed) > 0:
        cpu_speed = cpu_speed[0]
    else:
        proc_num = re.findall(r"(i\d?\s?-?\s?\d+\w?)[/|\s|]?", cpu_str)
        if len(proc_num) == 0:
            proc_num = re.findall(r"(\w\d+)\s", cpu_str)
            if len(proc_num) == 0:
                return None
        proc_num = proc_num[0].replace('k', 'K').replace(' ', '-')
        proc_num = re.sub(r'-+', '-', proc_num)
        cpu_speed = proc_num_lookup(proc_num, cpus=cpus)
        if cpu_speed is None:
            return cpu_speed
    
    cpu_speed = cpu_speed.replace(',', '.')
    cpu_speed = hrtz_convert(cpu_speed)
    
    return cpu_speed

def mad_zscore(series):
    mad = series.mad()
    median = series.median()
    return (series - median) / mad

def preprocess_data(df, cpus):
    sdata = df[["name", "href", "release_date", "min_processor", "min_memory",
              "min_graphics", "min_storage"]]

    # Drop any dates that can't be converted.
    sdata["release_date"] = sdata.release_date.apply(dt_convert)    

    # Process min_memory into interpretable RAM
    sdata["min_memory"] = sdata["min_memory"].apply(mem_extract)

    # Process min_storage into interpretable sizes
    sdata["min_storage"] = sdata["min_storage"].apply(mem_extract)

    # Process min_processor into Ghz
    sdata["min_processor"] = sdata["min_processor"].apply(get_cpu_speed, cpus=cpus)

    return sdata

def filter_data(df):
    # Using Median Absolute Deviation (MAD) to remove massive outliers,
    # keeps null values
    cpu_mad = (mad_zscore(df["min_processor"]) < 3) | df["min_processor"].isna()
    ram_mad = (mad_zscore(df["min_memory"]) < 3) | df["min_memory"].isna()
    
    # I don't think filtering storage with MAD is a good move
    # because games can reasonably have radically different
    # sizes. Indie game vs AAA title for example.
    # storage_mad = (mad_zscore(df["min_storage"]) < 3) | df["min_storage"].isna()
    storage_zscore = (get_zscores(df["min_storage"]) < 3) | df["min_storage"].isna()

    return df[cpu_mad & ram_mad & storage_zscore].reset_index(drop=True)
    