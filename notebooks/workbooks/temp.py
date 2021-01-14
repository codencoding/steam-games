html_page = """<!DOCTYPE html>
<html class="responsive" lang="en">
<head>
<meta content="text/html; charset=utf-8" http-equiv="Content-Type"/>
<meta content="width=device-width,initial-scale=1" name="viewport"/>
<meta content="#171a21" name="theme-color"/>
<title>Rust on Steam</title>
<link href="/favicon.ico" rel="shortcut icon" type="image/x-icon"/>
<link href="https://store.cloudflare.steamstatic.com/public/shared/css/motiva_sans.css?v=GvhJzpHNW-hA&amp;l=english&amp;_cdn=cloudflare" rel="stylesheet" type="text/css"/>
<link href="https://store.cloudflare.steamstatic.com/public/shared/css/shared_global.css?v=Ees51BsBNwIC&amp;l=english&amp;_cdn=cloudflare" rel="stylesheet" type="text/css"/>
<link href="https://store.cloudflare.steamstatic.com/public/shared/css/buttons.css?v=l3li_MNwxNDv&amp;l=english&amp;_cdn=cloudflare" rel="stylesheet" type="text/css"/>
<link href="https://store.cloudflare.steamstatic.com/public/css/v6/store.css?v=duQ1py9GsvUF&amp;l=english&amp;_cdn=cloudflare" rel="stylesheet" type="text/css"/>
<link href="https://store.cloudflare.steamstatic.com/public/shared/css/user_reviews.css?v=W6O0HwaYszHN&amp;l=english&amp;_cdn=cloudflare" rel="stylesheet" type="text/css"/>
<link href="https://store.cloudflare.steamstatic.com/public/shared/css/store_game_shared.css?v=kTQXgVodaFoU&amp;l=english&amp;_cdn=cloudflare" rel="stylesheet" type="text/css"/>
<link href="https://store.cloudflare.steamstatic.com/public/css/v6/game.css?v=1qnOoZezRPGG&amp;l=english&amp;_cdn=cloudflare" rel="stylesheet" type="text/css"/>
<link href="https://store.cloudflare.steamstatic.com/public/css/v6/recommended.css?v=DI5BTGWFZNdo&amp;l=english&amp;_cdn=cloudflare" rel="stylesheet" type="text/css"/>
<link href="https://store.cloudflare.steamstatic.com/public/css/v6/user_reviews_rewards.css?v=5-HJZa1v4wFP&amp;l=english&amp;_cdn=cloudflare" rel="stylesheet" type="text/css"/>
<link href="https://store.cloudflare.steamstatic.com/public/shared/css/apphub.css?v=UWNPI41CbGcf&amp;l=english&amp;_cdn=cloudflare" rel="stylesheet" type="text/css"/>
<link href="https://store.cloudflare.steamstatic.com/public/shared/css/ui-lightness/jquery-ui-1.7.2.custom.css?v=.23LkAmA0IgZV&amp;_cdn=cloudflare" rel="stylesheet" type="text/css"/>
<link href="https://store.cloudflare.steamstatic.com/public/shared/css/shared_responsive.css?v=nZoH3ohA_bdx&amp;l=english&amp;_cdn=cloudflare" rel="stylesheet" type="text/css"/>
<script>
				(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
						(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
					m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
				})(window,document,'script','//www.google-analytics.com/analytics.js','ga');

				ga('create', 'UA-33786258-1', 'auto', {
					'sampleRate': 0.4				});
				ga('set', 'dimension1', false );
				ga('set', 'dimension2', 'External' );
				ga('set', 'dimension3', 'application' );
				ga('set', 'dimension4', "application\/app" );
				ga('send', 'pageview' );

			</script>
<script type="text/javascript">Object.seal && Object.seal( Object.prototype );</script><script src="https://store.cloudflare.steamstatic.com/public/shared/javascript/jquery-1.8.3.min.js?v=.TZ2NKhB-nliU&amp;_cdn=cloudflare" type="text/javascript"></script>
<script type="text/javascript">$J = jQuery.noConflict();</script><script type="text/javascript">VALVE_PUBLIC_PATH = "https:\/\/store.cloudflare.steamstatic.com\/public\/";</script><script src="https://store.cloudflare.steamstatic.com/public/shared/javascript/tooltip.js?v=.9Z1XDV02xrml&amp;_cdn=cloudflare" type="text/javascript"></script>
<script src="https://store.cloudflare.steamstatic.com/public/shared/javascript/shared_global.js?v=R2JmKYDaxby2&amp;l=english&amp;_cdn=cloudflare" type="text/javascript"></script>
<script src="https://store.cloudflare.steamstatic.com/public/javascript/main.js?v=nrDlmSXyO2YF&amp;l=english&amp;_cdn=cloudflare" type="text/javascript"></script>
<script src="https://store.cloudflare.steamstatic.com/public/javascript/dynamicstore.js?v=aO8FaoRbo5Gf&amp;l=english&amp;_cdn=cloudflare" type="text/javascript"></script>
<script type="text/javascript">
			document.addEventListener('DOMContentLoaded', function(event) {
				$J.data( document, 'x_readytime', new Date().getTime() );
				$J.data( document, 'x_oldref', GetNavCookie() );
				SetupTooltips( { tooltipCSSClass: 'store_tooltip'} );
		});
		</script><script src="https://store.cloudflare.steamstatic.com/public/javascript/gamehighlightplayer.js?v=xhmc3Gs3aQ2w&amp;l=english&amp;_cdn=cloudflare" type="text/javascript"></script>
<script src="https://store.cloudflare.steamstatic.com/public/shared/javascript/user_reviews.js?v=UAtN6EjFM4-v&amp;l=english&amp;_cdn=cloudflare" type="text/javascript"></script>
<script src="https://store.cloudflare.steamstatic.com/public/shared/javascript/dselect.js?v=yT8Q5U2-O4wX&amp;l=english&amp;_cdn=cloudflare" type="text/javascript"></script>
<script src="https://store.cloudflare.steamstatic.com/public/javascript/app_tagging.js?v=WUwl9xP5ZkwE&amp;l=english&amp;_cdn=cloudflare" type="text/javascript"></script>
<script src="https://store.cloudflare.steamstatic.com/public/javascript/game.js?v=h6D49XZw6Aan&amp;l=english&amp;_cdn=cloudflare" type="text/javascript"></script>
<script src="https://store.cloudflare.steamstatic.com/public/shared/javascript/flot-0.8/jquery.flot.min.js?v=.-m414tR-pxn_&amp;_cdn=cloudflare" type="text/javascript"></script>
<script src="https://store.cloudflare.steamstatic.com/public/shared/javascript/flot-0.8/jquery.flot.resize.min.js?v=.4PeWDSmdkiqV&amp;_cdn=cloudflare" type="text/javascript"></script>
<script src="https://store.cloudflare.steamstatic.com/public/shared/javascript/flot-0.8/jquery.flot.time.min.js?v=.tcjKevZLo5Un&amp;_cdn=cloudflare" type="text/javascript"></script>
<script src="https://store.cloudflare.steamstatic.com/public/shared/javascript/flot-0.8/jquery.flot.selection.min.js?v=._7pxnS3SCqO7&amp;_cdn=cloudflare" type="text/javascript"></script>
<script src="https://store.cloudflare.steamstatic.com/public/shared/javascript/jquery-ui-1.9.2.js?v=.4YjdpcHj68MM&amp;_cdn=cloudflare" type="text/javascript"></script>
<script src="https://store.cloudflare.steamstatic.com/public/shared/javascript/shared_responsive_adapter.js?v=TbBMCK37KgCo&amp;l=english&amp;_cdn=cloudflare" type="text/javascript"></script>
<meta content="summary_large_image" name="twitter:card"/>
<meta content="The only aim in Rust is to survive - Overcome struggles such as hunger, thirst and cold. Build a fire. Build a shelter. Kill animals. Protect yourself from other players." name="Description"/>
<meta content="@steam" name="twitter:site"/>
<meta content="Rust on Steam" property="og:title"/>
<meta content="Rust on Steam" property="twitter:title"/>
<meta content="website" property="og:type"/>
<meta content="105386699540688" property="fb:app_id"/>
<meta content="Steam" property="og:site"/>
<meta content="https://store.steampowered.com/app/252490/Rust/" property="og:url"/>
<meta content="The only aim in Rust is to survive - Overcome struggles such as hunger, thirst and cold. Build a fire. Build a shelter. Kill animals. Protect yourself from other players." property="og:description"/>
<meta content="The only aim in Rust is to survive - Overcome struggles such as hunger, thirst and cold. Build a fire. Build a shelter. Kill animals. Protect yourself from other players." property="twitter:description"/>
<link href="https://store.steampowered.com/app/252490/Rust/" rel="canonical"/>
<link href="https://cdn.cloudflare.steamstatic.com/steam/apps/252490/capsule_616x353.jpg?t=1608404151" rel="image_src"/>
<meta content="https://cdn.cloudflare.steamstatic.com/steam/apps/252490/capsule_616x353.jpg?t=1608404151" property="og:image"/>
<meta content="https://cdn.cloudflare.steamstatic.com/steam/apps/252490/capsule_616x353.jpg?t=1608404151" name="twitter:image"/>
</head>
<body class="v6 app game_bg responsive_page">
<div class="responsive_page_frame with_header">
<div class="responsive_page_menu_ctn mainmenu">
<div class="responsive_page_menu" id="responsive_page_menu">
<div class="mainmenu_contents">
<div class="mainmenu_contents_items">
<a class="menuitem" href="https://store.steampowered.com/login/?redir=app%2F252490%2FRust%2F&amp;redir_ssl=1&amp;snr=1_5_9__global-header">
									Login								</a>
<a class="menuitem supernav" data-tooltip-content=".submenu_store" data-tooltip-type="selector" href="https://store.steampowered.com/?snr=1_5_9__global-responsive-menu">
		Store	</a>
<div class="submenu_store" data-submenuid="store" style="display: none;">
<a class="submenuitem" href="https://store.steampowered.com/?snr=1_5_9__global-responsive-menu">Home</a>
<a class="submenuitem" href="https://store.steampowered.com/explore/?snr=1_5_9__global-responsive-menu">Discovery Queue</a>
<a class="submenuitem" href="https://steamcommunity.com/my/wishlist/">Wishlist</a>
<a class="submenuitem" href="https://store.steampowered.com/points/shop/?snr=1_5_9__global-responsive-menu">Points Shop</a>
<a class="submenuitem" href="https://store.steampowered.com/news/?snr=1_5_9__global-responsive-menu">News</a>
<a class="submenuitem" href="https://store.steampowered.com/stats/?snr=1_5_9__global-responsive-menu">Stats</a>
</div>
<a class="menuitem supernav" data-tooltip-content=".submenu_community" data-tooltip-type="selector" href="https://steamcommunity.com/" style="display: block">
			Community		</a>
<div class="submenu_community" data-submenuid="community" style="display: none;">
<a class="submenuitem" href="https://steamcommunity.com/">Home</a>
<a class="submenuitem" href="https://steamcommunity.com/discussions/">Discussions</a>
<a class="submenuitem" href="https://steamcommunity.com/workshop/">Workshop</a>
<a class="submenuitem" href="https://steamcommunity.com/market/">Market</a>
<a class="submenuitem" href="https://steamcommunity.com/?subsection=broadcasts">Broadcasts</a>
</div>
<a class="menuitem" href="https://help.steampowered.com/en/">
		Support	</a>
<div class="minor_menu_items">
<div class="menuitem change_language_action">
									Change language								</div>
<div class="menuitem" onclick="Responsive_RequestDesktopView();">
										View desktop website									</div>
</div>
</div>
<div class="mainmenu_footer_spacer"></div>
<div class="mainmenu_footer">
<div class="mainmenu_footer_logo"><img src="https://store.cloudflare.steamstatic.com/public/shared/images/responsive/logo_valve_footer.png"/></div>
								© Valve Corporation. All rights reserved. All trademarks are property of their respective owners in the US and other countries.								<span class="mainmenu_valve_links">
<a href="https://store.steampowered.com/privacy_agreement/?snr=1_5_9__global-responsive-menu" target="_blank">Privacy Policy</a>
									 |  <a href="http://www.valvesoftware.com/legal.htm" target="_blank">Legal</a>
									 |  <a href="https://store.steampowered.com/subscriber_agreement/?snr=1_5_9__global-responsive-menu" target="_blank">Steam Subscriber Agreement</a>
									 |  <a href="https://store.steampowered.com/steam_refunds/?snr=1_5_9__global-responsive-menu" target="_blank">Refunds</a>
</span>
</div>
</div>
</div>
</div>
<div class="responsive_local_menu_tab">
</div>
<div class="responsive_page_menu_ctn localmenu">
<div class="responsive_page_menu" id="responsive_page_local_menu">
<div class="localmenu_content">
</div>
</div>
</div>
<div class="responsive_header">
<div class="responsive_header_content">
<div id="responsive_menu_logo">
<img height="100%" src="https://store.cloudflare.steamstatic.com/public/shared/images/responsive/header_menu_hamburger.png"/>
</div>
<div class="responsive_header_logo">
<a href="https://store.steampowered.com/?snr=1_5_9__global-responsive-menu">
<img alt="STEAM" border="0" height="36" src="https://store.cloudflare.steamstatic.com/public/shared/images/responsive/header_logo.png"/>
</a>
</div>
</div>
</div>
<div class="responsive_page_content_overlay">
</div>
<div class="responsive_fixonscroll_ctn nonresponsive_hidden">
</div>
<div class="responsive_page_content">
<div id="global_header">
<div class="content">
<div class="logo">
<span id="logo_holder">
<a href="https://store.steampowered.com/?snr=1_5_9__global-header">
<img height="44" src="https://store.cloudflare.steamstatic.com/public/shared/images/header/logo_steam.svg?t=962016" width="176"/>
</a>
</span>
<!--[if lt IE 7]>
			<style type="text/css">
				#logo_holder img { filter:progid:DXImageTransform.Microsoft.Alpha(opacity=0); }
				#logo_holder { display: inline-block; width: 176px; height: 44px; filter:progid:DXImageTransform.Microsoft.AlphaImageLoader(src='https://store.cloudflare.steamstatic.com/public/images/v5/globalheader_logo.png'); }
			</style>
			<![endif]-->
</div>
<div class="supernav_container">
<a class="menuitem supernav" data-tooltip-content=".submenu_store" data-tooltip-type="selector" href="https://store.steampowered.com/?snr=1_5_9__global-header">
		STORE	</a>
<div class="submenu_store" data-submenuid="store" style="display: none;">
<a class="submenuitem" href="https://store.steampowered.com/?snr=1_5_9__global-header">Home</a>
<a class="submenuitem" href="https://store.steampowered.com/explore/?snr=1_5_9__global-header">Discovery Queue</a>
<a class="submenuitem" href="https://steamcommunity.com/my/wishlist/">Wishlist</a>
<a class="submenuitem" href="https://store.steampowered.com/points/shop/?snr=1_5_9__global-header">Points Shop</a>
<a class="submenuitem" href="https://store.steampowered.com/news/?snr=1_5_9__global-header">News</a>
<a class="submenuitem" href="https://store.steampowered.com/stats/?snr=1_5_9__global-header">Stats</a>
</div>
<a class="menuitem supernav" data-tooltip-content=".submenu_community" data-tooltip-type="selector" href="https://steamcommunity.com/" style="display: block">
			COMMUNITY		</a>
<div class="submenu_community" data-submenuid="community" style="display: none;">
<a class="submenuitem" href="https://steamcommunity.com/">Home</a>
<a class="submenuitem" href="https://steamcommunity.com/discussions/">Discussions</a>
<a class="submenuitem" href="https://steamcommunity.com/workshop/">Workshop</a>
<a class="submenuitem" href="https://steamcommunity.com/market/">Market</a>
<a class="submenuitem" href="https://steamcommunity.com/?subsection=broadcasts">Broadcasts</a>
</div>
<a class="menuitem" href="https://store.steampowered.com/about/?snr=1_5_9__global-header">
				ABOUT			</a>
<a class="menuitem" href="https://help.steampowered.com/en/">
		SUPPORT	</a>
</div>
<script type="text/javascript">
		jQuery(function($) {
			$('#global_header .supernav').v_tooltip({'location':'bottom', 'destroyWhenDone': false, 'tooltipClass': 'supernav_content', 'offsetY':-4, 'offsetX': 1, 'horizontalSnap': 4, 'tooltipParent': '#global_header .supernav_container', 'correctForScreenSize': false});
		});
	</script>
<div id="global_actions">
<div id="global_action_menu">
<div class="header_installsteam_btn header_installsteam_btn_green">
<a class="header_installsteam_btn_content" href="https://store.steampowered.com/about/?snr=1_5_9__global-header">
							Install Steam						</a>
</div>
<a class="global_action_link" href="https://store.steampowered.com/login/?redir=app%2F252490%2FRust%2F&amp;redir_ssl=1&amp;snr=1_5_9__global-header">login</a>
											 | 
						<span class="pulldown global_action_link" id="language_pulldown" onclick="ShowMenu( this, 'language_dropdown', 'right' );">language</span>
<div class="popup_block_new" id="language_dropdown" style="display: none;">
<div class="popup_body popup_menu">
<a class="popup_menu_item tight" href="?l=schinese" onclick="ChangeLanguage( 'schinese' ); return false;">简体中文 (Simplified Chinese)</a>
<a class="popup_menu_item tight" href="?l=tchinese" onclick="ChangeLanguage( 'tchinese' ); return false;">繁體中文 (Traditional Chinese)</a>
<a class="popup_menu_item tight" href="?l=japanese" onclick="ChangeLanguage( 'japanese' ); return false;">日本語 (Japanese)</a>
<a class="popup_menu_item tight" href="?l=koreana" onclick="ChangeLanguage( 'koreana' ); return false;">한국어 (Korean)</a>
<a class="popup_menu_item tight" href="?l=thai" onclick="ChangeLanguage( 'thai' ); return false;">ไทย (Thai)</a>
<a class="popup_menu_item tight" href="?l=bulgarian" onclick="ChangeLanguage( 'bulgarian' ); return false;">Български (Bulgarian)</a>
<a class="popup_menu_item tight" href="?l=czech" onclick="ChangeLanguage( 'czech' ); return false;">Čeština (Czech)</a>
<a class="popup_menu_item tight" href="?l=danish" onclick="ChangeLanguage( 'danish' ); return false;">Dansk (Danish)</a>
<a class="popup_menu_item tight" href="?l=german" onclick="ChangeLanguage( 'german' ); return false;">Deutsch (German)</a>
<a class="popup_menu_item tight" href="?l=spanish" onclick="ChangeLanguage( 'spanish' ); return false;">Español - España (Spanish - Spain)</a>
<a class="popup_menu_item tight" href="?l=latam" onclick="ChangeLanguage( 'latam' ); return false;">Español - Latinoamérica (Spanish - Latin America)</a>
<a class="popup_menu_item tight" href="?l=greek" onclick="ChangeLanguage( 'greek' ); return false;">Ελληνικά (Greek)</a>
<a class="popup_menu_item tight" href="?l=french" onclick="ChangeLanguage( 'french' ); return false;">Français (French)</a>
<a class="popup_menu_item tight" href="?l=italian" onclick="ChangeLanguage( 'italian' ); return false;">Italiano (Italian)</a>
<a class="popup_menu_item tight" href="?l=hungarian" onclick="ChangeLanguage( 'hungarian' ); return false;">Magyar (Hungarian)</a>
<a class="popup_menu_item tight" href="?l=dutch" onclick="ChangeLanguage( 'dutch' ); return false;">Nederlands (Dutch)</a>
<a class="popup_menu_item tight" href="?l=norwegian" onclick="ChangeLanguage( 'norwegian' ); return false;">Norsk (Norwegian)</a>
<a class="popup_menu_item tight" href="?l=polish" onclick="ChangeLanguage( 'polish' ); return false;">Polski (Polish)</a>
<a class="popup_menu_item tight" href="?l=portuguese" onclick="ChangeLanguage( 'portuguese' ); return false;">Português (Portuguese)</a>
<a class="popup_menu_item tight" href="?l=brazilian" onclick="ChangeLanguage( 'brazilian' ); return false;">Português - Brasil (Portuguese - Brazil)</a>
<a class="popup_menu_item tight" href="?l=romanian" onclick="ChangeLanguage( 'romanian' ); return false;">Română (Romanian)</a>
<a class="popup_menu_item tight" href="?l=russian" onclick="ChangeLanguage( 'russian' ); return false;">Русский (Russian)</a>
<a class="popup_menu_item tight" href="?l=finnish" onclick="ChangeLanguage( 'finnish' ); return false;">Suomi (Finnish)</a>
<a class="popup_menu_item tight" href="?l=swedish" onclick="ChangeLanguage( 'swedish' ); return false;">Svenska (Swedish)</a>
<a class="popup_menu_item tight" href="?l=turkish" onclick="ChangeLanguage( 'turkish' ); return false;">Türkçe (Turkish)</a>
<a class="popup_menu_item tight" href="?l=vietnamese" onclick="ChangeLanguage( 'vietnamese' ); return false;">Tiếng Việt (Vietnamese)</a>
<a class="popup_menu_item tight" href="?l=ukrainian" onclick="ChangeLanguage( 'ukrainian' ); return false;">Українська (Ukrainian)</a>
<a class="popup_menu_item tight" href="http://translation.steampowered.com" target="_blank">Help us translate Steam</a>
</div>
</div>
</div>
</div>
</div>
</div>
<div id="responsive_store_nav_ctn"></div><div data-cart-banner-spot="1"></div>
<div class="responsive_page_template_content">
<script type="text/javascript">
			try {
				if ( typeof ga != 'undefined' && ga )
				{
					ga( 'create', "UA-29119593-3", 'auto', "app", {
						anonymizeIp: true
					} );
					ga( 'app.require', 'linker' );
					ga( 'app.linker:autolink', ["store.steampowered.com","steamcommunity.com","help.steampowered.com"] );
					ga( 'app.send', 'pageview' );
				}
			} catch ( e ) { }
		</script>
<script type="text/javascript">

	var g_eDiscoveryQueueType = 0;

	GStoreItemData.AddStoreItemDataSet(
		{"rgApps":{"648800":{"name":"Raft","url_name":"Raft","discount_block":"<div class=\"discount_block  no_discount\" data-price-final=\"1999\"><div class=\"discount_prices\"><div class=\"discount_final_price\">$19.99<\/div><\/div><\/div>","descids":[],"small_capsulev5":"https:\/\/cdn.cloudflare.steamstatic.com\/steam\/apps\/648800\/capsule_184x69.jpg?t=1602795811","os_windows":true,"early_access":true,"has_live_broadcast":false,"localized":true},"346110":{"name":"ARK: Survival Evolved","url_name":"ARK_Survival_Evolved","discount_block":"<div class=\"discount_block  no_discount\" data-price-final=\"4999\"><div class=\"discount_prices\"><div class=\"discount_final_price\">$49.99<\/div><\/div><\/div>","descids":[],"small_capsulev5":"https:\/\/cdn.cloudflare.steamstatic.com\/steam\/apps\/346110\/capsule_184x69.jpg?t=1608086122","os_windows":true,"os_macos":true,"os_linux":true,"has_live_broadcast":false,"localized":true,"status_string":"Just Updated"},"440900":{"name":"Conan Exiles","url_name":"Conan_Exiles","discount_block":"<div class=\"discount_block  no_discount\" data-price-final=\"3999\"><div class=\"discount_prices\"><div class=\"discount_final_price\">$39.99<\/div><\/div><\/div>","descids":[1,2,5],"small_capsulev5":"https:\/\/cdn.cloudflare.steamstatic.com\/steam\/apps\/440900\/capsule_184x69.jpg?t=1603288258","os_windows":true,"has_live_broadcast":false,"localized":true,"has_adult_content_violence":true,"has_adult_content_sex":true},"105600":{"name":"Terraria","url_name":"Terraria","discount_block":"<div class=\"discount_block  no_discount\" data-price-final=\"999\"><div class=\"discount_prices\"><div class=\"discount_final_price\">$9.99<\/div><\/div><\/div>","descids":[],"small_capsulev5":"https:\/\/cdn.cloudflare.steamstatic.com\/steam\/apps\/105600\/capsule_184x69.jpg?t=1590092560","os_windows":true,"os_macos":true,"os_linux":true,"has_live_broadcast":false,"localized":true,"status_string":"Just Updated"},"526870":{"name":"Satisfactory","url_name":"Satisfactory","discount_block":"<div class=\"discount_block  no_discount\" data-price-final=\"2999\"><div class=\"discount_prices\"><div class=\"discount_final_price\">$29.99<\/div><\/div><\/div>","descids":[],"small_capsulev5":"https:\/\/cdn.cloudflare.steamstatic.com\/steam\/apps\/526870\/capsule_184x69.jpg?t=1598908784","os_windows":true,"early_access":true,"has_live_broadcast":true,"localized":true},"242760":{"name":"The Forest","url_name":"The_Forest","discount_block":"<div class=\"discount_block  no_discount\" data-price-final=\"1999\"><div class=\"discount_prices\"><div class=\"discount_final_price\">$19.99<\/div><\/div><\/div>","descids":[],"small_capsulev5":"https:\/\/cdn.cloudflare.steamstatic.com\/steam\/apps\/242760\/capsule_184x69.jpg?t=1590522045","os_windows":true,"vr_htcvive":true,"vr_oculusrift":true,"has_live_broadcast":false,"localized":true},"244850":{"name":"Space Engineers","url_name":"Space_Engineers","discount_block":"<div class=\"discount_block  no_discount\" data-price-final=\"1999\"><div class=\"discount_prices\"><div class=\"discount_final_price\">$19.99<\/div><\/div><\/div>","descids":[],"small_capsulev5":"https:\/\/cdn.cloudflare.steamstatic.com\/steam\/apps\/244850\/capsule_184x69.jpg?t=1607424211","os_windows":true,"has_live_broadcast":false,"localized":true},"361420":{"name":"ASTRONEER","url_name":"ASTRONEER","discount_block":"<div class=\"discount_block  no_discount\" data-price-final=\"2999\"><div class=\"discount_prices\"><div class=\"discount_final_price\">$29.99<\/div><\/div><\/div>","descids":[],"small_capsulev5":"https:\/\/cdn.cloudflare.steamstatic.com\/steam\/apps\/361420\/capsule_184x69.jpg?t=1608327289","os_windows":true,"has_live_broadcast":false,"localized":true},"1307550":{"name":"Craftopia","url_name":"Craftopia","discount_block":"<div class=\"discount_block  no_discount\" data-price-final=\"2499\"><div class=\"discount_prices\"><div class=\"discount_final_price\">$24.99<\/div><\/div><\/div>","descids":[],"small_capsulev5":"https:\/\/cdn.cloudflare.steamstatic.com\/steam\/apps\/1307550\/capsule_184x69.jpg?t=1607510758","os_windows":true,"early_access":true,"has_live_broadcast":false,"localized":true},"962130":{"name":"Grounded","url_name":"Grounded","discount_block":"<div class=\"discount_block  no_discount\" data-price-final=\"2999\"><div class=\"discount_prices\"><div class=\"discount_final_price\">$29.99<\/div><\/div><\/div>","descids":[],"small_capsulev5":"https:\/\/cdn.cloudflare.steamstatic.com\/steam\/apps\/962130\/capsule_184x69.jpg?t=1608148728","os_windows":true,"early_access":true,"has_live_broadcast":false,"localized":true},"322330":{"name":"Don't Starve Together","url_name":"Dont_Starve_Together","discount_block":"<div class=\"discount_block  no_discount\" data-price-final=\"1499\"><div class=\"discount_prices\"><div class=\"discount_final_price\">$14.99<\/div><\/div><\/div>","descids":[],"small_capsulev5":"https:\/\/cdn.cloudflare.steamstatic.com\/steam\/apps\/322330\/capsule_184x69_alt_assets_0.jpg?t=1608060905","os_windows":true,"os_macos":true,"os_linux":true,"has_live_broadcast":false,"localized":true,"status_string":"Just Updated!"},"264710":{"name":"Subnautica","url_name":"Subnautica","discount_block":"<div class=\"discount_block  no_discount\" data-price-final=\"2999\"><div class=\"discount_prices\"><div class=\"discount_final_price\">$29.99<\/div><\/div><\/div>","descids":[],"small_capsulev5":"https:\/\/cdn.cloudflare.steamstatic.com\/steam\/apps\/264710\/capsule_184x69.jpg?t=1609982984","os_windows":true,"os_macos":true,"vr_htcvive":true,"vr_oculusrift":true,"has_live_broadcast":false,"localized":true},"251570":{"name":"7 Days to Die","url_name":"7_Days_to_Die","discount_block":"<div class=\"discount_block  no_discount\" data-price-final=\"2499\"><div class=\"discount_prices\"><div class=\"discount_final_price\">$24.99<\/div><\/div><\/div>","descids":[],"small_capsulev5":"https:\/\/cdn.cloudflare.steamstatic.com\/steam\/apps\/251570\/capsule_184x69.jpg?t=1608788477","os_windows":true,"os_macos":true,"os_linux":true,"early_access":true,"has_live_broadcast":false,"localized":true,"status_string":"Just Updated"},"275850":{"name":"No Man's Sky","url_name":"No_Mans_Sky","discount_block":"<div class=\"discount_block  no_discount\" data-price-final=\"5999\"><div class=\"discount_prices\"><div class=\"discount_final_price\">$59.99<\/div><\/div><\/div>","descids":[],"small_capsulev5":"https:\/\/cdn.cloudflare.steamstatic.com\/steam\/apps\/275850\/capsule_184x69.jpg?t=1606325215","os_windows":true,"vr_htcvive":true,"vr_oculusrift":true,"has_live_broadcast":false,"localized":true},"382310":{"name":"Eco","url_name":"Eco","discount_block":"<div class=\"discount_block  no_discount\" data-price-final=\"2999\"><div class=\"discount_prices\"><div class=\"discount_final_price\">$29.99<\/div><\/div><\/div>","descids":[],"small_capsulev5":"https:\/\/cdn.cloudflare.steamstatic.com\/steam\/apps\/382310\/capsule_184x69.jpg?t=1607126536","os_windows":true,"early_access":true,"has_live_broadcast":false,"localized":true},"895400":{"name":"Deadside","url_name":"Deadside","discount_block":"<div class=\"discount_block  no_discount\" data-price-final=\"1999\"><div class=\"discount_prices\"><div class=\"discount_final_price\">$19.99<\/div><\/div><\/div>","descids":[2,5],"small_capsulev5":"https:\/\/cdn.cloudflare.steamstatic.com\/steam\/apps\/895400\/capsule_184x69.jpg?t=1589988562","os_windows":true,"early_access":true,"has_live_broadcast":false,"localized":true,"has_adult_content_violence":true},"513710":{"name":"SCUM","url_name":"SCUM","discount_block":"<div class=\"discount_block  no_discount\" data-price-final=\"2999\"><div class=\"discount_prices\"><div class=\"discount_final_price\">$29.99<\/div><\/div><\/div>","descids":[1,2,5],"small_capsulev5":"https:\/\/cdn.cloudflare.steamstatic.com\/steam\/apps\/513710\/capsule_184x69.jpg?t=1595590056","os_windows":true,"early_access":true,"has_live_broadcast":false,"localized":true,"has_adult_content_violence":true},"815370":{"name":"Green Hell","url_name":"Green_Hell","discount_block":"<div class=\"discount_block  no_discount\" data-price-final=\"2499\"><div class=\"discount_prices\"><div class=\"discount_final_price\">$24.99<\/div><\/div><\/div>","descids":[],"small_capsulev5":"https:\/\/cdn.cloudflare.steamstatic.com\/steam\/apps\/815370\/capsule_184x69.jpg?t=1608044710","os_windows":true,"has_live_broadcast":false,"localized":true},"221100":{"name":"DayZ","url_name":"DayZ","discount_block":"<div class=\"discount_block  no_discount\" data-price-final=\"4499\"><div class=\"discount_prices\"><div class=\"discount_final_price\">$44.99<\/div><\/div><\/div>","descids":[],"small_capsulev5":"https:\/\/cdn.cloudflare.steamstatic.com\/steam\/apps\/221100\/capsule_184x69.jpg?t=1608209844","os_windows":true,"has_live_broadcast":false,"localized":true},"108600":{"name":"Project Zomboid","url_name":"Project_Zomboid","discount_block":"<div class=\"discount_block  no_discount\" data-price-final=\"1499\"><div class=\"discount_prices\"><div class=\"discount_final_price\">$14.99<\/div><\/div><\/div>","descids":[],"small_capsulev5":"https:\/\/cdn.cloudflare.steamstatic.com\/steam\/apps\/108600\/capsule_184x69.jpg?t=1605306992","os_windows":true,"os_macos":true,"os_linux":true,"early_access":true,"has_live_broadcast":false,"localized":true,"status_string":"Early Access Now Available"},"387990":{"name":"Scrap Mechanic","url_name":"Scrap_Mechanic","discount_block":"<div class=\"discount_block  no_discount\" data-price-final=\"1999\"><div class=\"discount_prices\"><div class=\"discount_final_price\">$19.99<\/div><\/div><\/div>","descids":[],"small_capsulev5":"https:\/\/cdn.cloudflare.steamstatic.com\/steam\/apps\/387990\/capsule_184x69.jpg?t=1593703247","os_windows":true,"early_access":true,"has_live_broadcast":false,"localized":true,"status_string":"Now with Steam Workshop!"},"313120":{"name":"Stranded Deep","url_name":"Stranded_Deep","discount_block":"<div class=\"discount_block  no_discount\" data-price-final=\"1499\"><div class=\"discount_prices\"><div class=\"discount_final_price\">$14.99<\/div><\/div><\/div>","descids":[],"small_capsulev5":"https:\/\/cdn.cloudflare.steamstatic.com\/steam\/apps\/313120\/capsule_184x69.jpg?t=1574473597","os_windows":true,"os_macos":true,"os_linux":true,"early_access":true,"has_live_broadcast":false,"localized":true},"848450":{"name":"Subnautica: Below Zero","url_name":"Subnautica_Below_Zero","discount_block":"<div class=\"discount_block  no_discount\" data-price-final=\"2999\"><div class=\"discount_prices\"><div class=\"discount_final_price\">$29.99<\/div><\/div><\/div>","descids":[],"small_capsulev5":"https:\/\/cdn.cloudflare.steamstatic.com\/steam\/apps\/848450\/capsule_184x69.jpg?t=1609983070","os_windows":true,"os_macos":true,"early_access":true,"has_live_broadcast":false,"localized":true},"427520":{"name":"Factorio","url_name":"Factorio","discount_block":"<div class=\"discount_block  no_discount\" data-price-final=\"3000\"><div class=\"discount_prices\"><div class=\"discount_final_price\">$30.00<\/div><\/div><\/div>","descids":[],"small_capsulev5":"https:\/\/cdn.cloudflare.steamstatic.com\/steam\/apps\/427520\/capsule_184x69.jpg?t=1597395512","os_windows":true,"os_macos":true,"os_linux":true,"has_live_broadcast":false,"localized":true},"211820":{"name":"Starbound","url_name":"Starbound","discount_block":"<div class=\"discount_block  no_discount\" data-price-final=\"1499\"><div class=\"discount_prices\"><div class=\"discount_final_price\">$14.99<\/div><\/div><\/div>","descids":[],"small_capsulev5":"https:\/\/cdn.cloudflare.steamstatic.com\/steam\/apps\/211820\/capsule_184x69.jpg?t=1599228095","os_windows":true,"os_macos":true,"os_linux":true,"has_live_broadcast":false,"localized":true},"594650":{"name":"Hunt: Showdown","url_name":"Hunt_Showdown","discount_block":"<div class=\"discount_block  no_discount\" data-price-final=\"3999\"><div class=\"discount_prices\"><div class=\"discount_final_price\">$39.99<\/div><\/div><\/div>","descids":[2,5],"small_capsulev5":"https:\/\/cdn.cloudflare.steamstatic.com\/steam\/apps\/594650\/capsule_184x69.jpg?t=1610393013","os_windows":true,"has_live_broadcast":false,"localized":true,"has_adult_content_violence":true},"1129580":{"name":"Medieval Dynasty","url_name":"Medieval_Dynasty","discount_block":"<div class=\"discount_block  no_discount\" data-price-final=\"2999\"><div class=\"discount_prices\"><div class=\"discount_final_price\">$29.99<\/div><\/div><\/div>","descids":[],"small_capsulev5":"https:\/\/cdn.cloudflare.steamstatic.com\/steam\/apps\/1129580\/capsule_184x69.jpg?t=1608671866","os_windows":true,"early_access":true,"has_live_broadcast":true,"localized":true},"518790":{"name":"theHunter: Call of the Wild\u2122","url_name":"theHunter_Call_of_the_Wild","discount_block":"<div class=\"discount_block  no_discount\" data-price-final=\"1999\"><div class=\"discount_prices\"><div class=\"discount_final_price\">$19.99<\/div><\/div><\/div>","descids":[],"small_capsulev5":"https:\/\/cdn.cloudflare.steamstatic.com\/steam\/apps\/518790\/capsule_184x69.jpg?t=1607595944","os_windows":true,"has_live_broadcast":false,"localized":true},"239140":{"name":"Dying Light","url_name":"Dying_Light","discount_block":"<div class=\"discount_block  no_discount\" data-price-final=\"3999\"><div class=\"discount_prices\"><div class=\"discount_final_price\">$39.99<\/div><\/div><\/div>","descids":[],"small_capsulev5":"https:\/\/cdn.cloudflare.steamstatic.com\/steam\/apps\/239140\/capsule_184x69.jpg?t=1610457360","os_windows":true,"os_macos":true,"os_linux":true,"has_live_broadcast":false,"localized":true},"305620":{"name":"The Long Dark","url_name":"The_Long_Dark","discount_block":"<div class=\"discount_block  no_discount\" data-price-final=\"2999\"><div class=\"discount_prices\"><div class=\"discount_final_price\">$29.99<\/div><\/div><\/div>","descids":[],"small_capsulev5":"https:\/\/cdn.cloudflare.steamstatic.com\/steam\/apps\/305620\/capsule_184x69_alt_assets_1.jpg?t=1608080968","os_windows":true,"os_macos":true,"os_linux":true,"has_live_broadcast":false,"localized":true}},"rgPackages":{"244390":{"name":"Rust","url_name":"Rust","discount_block":"<div class=\"discount_block  no_discount\" data-price-final=\"3999\"><div class=\"discount_prices\"><div class=\"discount_final_price\">$39.99<\/div><\/div><\/div>","descids":[1,2,5],"tiny_capsule":"https:\/\/cdn.cloudflare.steamstatic.com\/steam\/apps\/252490\/capsule_sm_120.jpg?t=1608404151","tags":["Survival","Crafting","Multiplayer","Open World","Open World Survival Craft"],"tagids":[1662,1702,3859,1695,1100689,1643],"os_windows":true,"os_macos":true,"appids":[252490],"has_live_broadcast":false,"localized":true,"has_adult_content_violence":true},"402208":{"name":"Rust Instrument Pack","url_name":"Rust_Instrument_Pack","discount_block":"<div class=\"discount_block  no_discount\" data-price-final=\"999\"><div class=\"discount_prices\"><div class=\"discount_final_price\">$9.99<\/div><\/div><\/div>","descids":[],"tiny_capsule":"https:\/\/cdn.cloudflare.steamstatic.com\/steam\/apps\/1174370\/capsule_sm_120.jpg?t=1594121520","tags":["Indie","Massively Multiplayer","Action","Adventure","RPG"],"tagids":[492,128,19,21,122,1662],"os_windows":true,"os_macos":true,"appids":[1174370],"has_live_broadcast":false,"localized":true},"474021":{"name":"Rust Sunburn Pack","url_name":"Rust_Sunburn_Pack","discount_block":"<div class=\"discount_block  no_discount\" data-price-final=\"999\"><div class=\"discount_prices\"><div class=\"discount_final_price\">$9.99<\/div><\/div><\/div>","descids":[],"tiny_capsule":"https:\/\/cdn.cloudflare.steamstatic.com\/steam\/apps\/1353060\/capsule_sm_120.jpg?t=1604016443","tags":["Action","RPG","Indie","Massively Multiplayer","Adventure"],"tagids":[19,122,492,128,21,1662],"os_windows":true,"os_macos":true,"appids":[1353060],"has_live_broadcast":false,"localized":true},"218":{"name":"Garry's Mod","url_name":"Garrys_Mod","discount_block":"<div class=\"discount_block  no_discount\" data-price-final=\"999\"><div class=\"discount_prices\"><div class=\"discount_final_price\">$9.99<\/div><\/div><\/div>","descids":[],"tiny_capsule":"https:\/\/cdn.cloudflare.steamstatic.com\/steam\/apps\/4000\/capsule_sm_120.jpg?t=1601306982","tags":["Sandbox","Multiplayer","Funny","Moddable","Building"],"tagids":[3810,3859,4136,1669,1643,1719],"os_windows":true,"os_macos":true,"os_linux":true,"appids":[4000],"has_live_broadcast":false,"localized":true},"158488":{"name":"Chippy","url_name":"Chippy","discount_block":"<div class=\"discount_block  no_discount\" data-price-final=\"1499\"><div class=\"discount_prices\"><div class=\"discount_final_price\">$14.99<\/div><\/div><\/div>","descids":[],"tiny_capsule":"https:\/\/cdn.cloudflare.steamstatic.com\/steam\/apps\/602700\/capsule_sm_120.jpg?t=1594122144","tags":["Bullet Hell","Twin Stick Shooter","Arena Shooter","Shoot 'Em Up","Top-Down Shooter"],"tagids":[4885,4758,5547,4255,4637,4026],"os_windows":true,"appids":[602700],"has_live_broadcast":false,"localized":true},"158509":{"name":"Clatter","url_name":"Clatter","discount_block":"<div class=\"discount_block  no_discount\" data-price-final=\"999\"><div class=\"discount_prices\"><div class=\"discount_final_price\">$9.99<\/div><\/div><\/div>","descids":[],"tiny_capsule":"https:\/\/cdn.cloudflare.steamstatic.com\/steam\/apps\/602770\/capsule_sm_120.jpg?t=1594122295","tags":["Strategy","Indie","Turn-Based","Turn-Based Strategy","Turn-Based Combat"],"tagids":[9,492,1677,1741,4325,14139],"os_windows":true,"appids":[602770],"has_live_broadcast":false,"localized":true}},"rgBundles":[]}	);
	GStoreItemData.AddNavParams( {
		recommended: "1_5_9__300",
		recommend_franchise: "1_5_9__316",
		more_from_franchise: "1_5_9__317",
		bundle_component_preview: "1_5_9__412",
		recommended_ranked_played: "1_5_9__862",
	} );

	$J( function() {
		var $Expander = $J('#devnotes_expander');
		if( $Expander.length && $Expander.height() < parseInt( $Expander.css('max-height') ) ) {
			$J('#devnotes_more').hide();
		}

		CollapseLongStrings( '.dev_row .summary.column' );

				InitAutocollapse();
		InitHorizontalAutoSliders();

		Responsive_ReparentItemsInResponsiveMode( '.responsive_apppage_details_right', $J('#responsive_apppage_details_right_ctn') );
		Responsive_ReparentItemsInResponsiveMode( '.responsive_apppage_details_left', $J('#responsive_apppage_details_left_ctn') );
		Responsive_ReparentItemsInResponsiveMode( '.responsive_apppage_reviewblock', $J('#responsive_apppage_reviewblock_ctn') );

		//hack to workaround chrome bug
		$J('#responsive_apppage_reviewblock_ctn' ).css('width', '100%' );
		window.setTimeout( function() { $J('#responsive_apppage_reviewblock_ctn').css('width', '' ); }, 1 );

		
				var watcher = new CScrollOffsetWatcher( $J('#app_reviews_hash'), OnLoadReviews );
		watcher.SetBufferHeight( 0 );

				InitPlaytimeFilterSlider();
		
	} );
	GDynamicStore.OnReady( function() {
		RenderMoreLikeThisBlock( ["648800","346110","440900","105600","526870","242760","244850","361420","1307550","962130","322330","264710","251570","275850","382310","895400","513710","815370","221100","108600","387990","313120","848450","427520","211820","594650","1129580","518790","239140","305620"], !!true );
		RenderFranchiseAppBlock( [] );
		RenderMoreDLCFromBaseGameBlock( [] );

	});

	
	function OpenTagModal()
	{
		ShowAppTagModal( 252490 );
	}

</script>
<div class="game_page_background game" style="background-image: url('https://cdn.cloudflare.steamstatic.com/steam/apps/252490/page_bg_generated_v6b.jpg?t=1608404151');">
<div class="" id="store_header">
<div class="content">
<div id="store_controls">
<div id="cart_status_data">
<div class="store_header_btn_green store_header_btn" id="store_header_cart_btn" style="display: none;">
<div class="store_header_btn_caps store_header_btn_leftcap"></div>
<div class="store_header_btn_caps store_header_btn_rightcap"></div>
<a class="store_header_btn_content" href="https://store.steampowered.com/cart/?snr=1_5_9__12" id="cart_link">
								Cart								(<span id="cart_item_count_value">0</span>)
							</a>
</div>
</div>
</div>
<div id="store_nav_area">
<div class="store_nav_leftcap"></div>
<div class="store_nav_bg">
<div class="store_nav">
<div class="tab flyout_tab" data-flyout="foryou_flyout" data-flyout-align="left" data-flyout-valign="bottom" id="foryou_tab" onmouseover="EnsureStoreMenuTagsLoaded( '#foryou_yourtags' );">
<span class="pulldown">
<a class="pulldown_desktop" href="https://store.steampowered.com/?snr=1_5_9__12">Your Store</a>
<span></span>
</span>
</div>
<div class="popup_block_new flyout_tab_flyout responsive_slidedown" id="foryou_flyout" style="display: none;">
<div class="popup_body popup_menu">
<a class="popup_menu_item" href="https://store.steampowered.com/?snr=1_5_9__12">
										Home									</a>
<div class="hr"></div>
<a class="popup_menu_item" href="https://store.steampowered.com/communityrecommendations/?snr=1_5_9__12">
					                                            Community Recommendations					                                        </a>
<a class="popup_menu_item" href="https://store.steampowered.com/recommended/?snr=1_5_9__12">
											Recently Viewed										</a>
<a class="popup_menu_item" href="https://store.steampowered.com/curators/?snr=1_5_9__12">
					                                            Steam Curators					                                        </a>
</div>
</div>
<div class="tab flyout_tab" data-flyout="genre_flyout" data-flyout-align="left" data-flyout-valign="bottom" id="genre_tab">
<span class="pulldown">
<a class="pulldown_desktop" href="https://store.steampowered.com/games/?snr=1_5_9__12">Browse</a>
<a class="pulldown_mobile" href="#">Browse</a>
<span></span>
</span>
</div>
<div class="popup_block_new flyout_tab_flyout responsive_slidedown" id="genre_flyout" style="display: none;">
<div class="popup_body popup_menu_twocol">
<div class="popup_menu">
<a class="popup_menu_item" href="https://store.steampowered.com/genre/Free%20to%20Play/?snr=1_5_9__12">
														Free to Play													</a>
<a class="popup_menu_item" href="https://store.steampowered.com/genre/Early%20Access/?snr=1_5_9__12">
														Early Access													</a>
<a class="popup_menu_item" href="https://store.steampowered.com/demos/?snr=1_5_9__12">
<span>Demos</span>
</a>
<a class="popup_menu_item" href="https://store.steampowered.com/controller/?snr=1_5_9__12">
<span>Controller Friendly</span>
</a>
<a class="popup_menu_item" href="https://store.steampowered.com/pccafe/?snr=1_5_9__12">
<span>For PC Cafés</span>
</a>
<a class="popup_menu_item" href="https://store.steampowered.com/remoteplay_hub/?snr=1_5_9__12">
<span>Remote Play</span>
</a>
<div class="hr"></div>
<div class="popup_menu_subheader">Virtual Reality</div>
<a class="popup_menu_item" href="https://store.steampowered.com/vr/?snr=1_5_9__12">
<span>VR Games &amp; Experiences</span>
</a>
<a class="popup_menu_item" href="https://store.steampowered.com/vrhardware/?snr=1_5_9__12">
<span>VR Hardware</span>
</a>
<div class="hr"></div>
<div class="popup_menu_subheader">Platforms</div>
<a class="popup_menu_item" href="https://store.steampowered.com/macos?snr=1_5_9__12">
												Mac OS X											</a>
<a class="popup_menu_item" href="https://store.steampowered.com/linux?snr=1_5_9__12">
												SteamOS + Linux											</a>
<div class="hr"></div>
<div class="popup_menu_subheader">Additional Content</div>
<a class="popup_menu_item" href="https://store.steampowered.com/soundtracks?snr=1_5_9__12">
												Soundtracks											</a>
</div>
<div class="popup_menu">
<div class="popup_menu_subheader">Game Genres</div>
<a class="popup_menu_item" href="https://store.steampowered.com/tags/en/Action/?snr=1_5_9__12">
														Action													</a>
<a class="popup_menu_item" href="https://store.steampowered.com/tags/en/Adventure/?snr=1_5_9__12">
														Adventure													</a>
<a class="popup_menu_item" href="https://store.steampowered.com/tags/en/Casual/?snr=1_5_9__12">
														Casual													</a>
<a class="popup_menu_item" href="https://store.steampowered.com/tags/en/Indie/?snr=1_5_9__12">
														Indie													</a>
<a class="popup_menu_item" href="https://store.steampowered.com/tags/en/Massively%20Multiplayer/?snr=1_5_9__12">
														Massively Multiplayer													</a>
<a class="popup_menu_item" href="https://store.steampowered.com/tags/en/Racing/?snr=1_5_9__12">
														Racing													</a>
<a class="popup_menu_item" href="https://store.steampowered.com/tags/en/RPG/?snr=1_5_9__12">
														RPG													</a>
<a class="popup_menu_item" href="https://store.steampowered.com/tags/en/Simulation/?snr=1_5_9__12">
														Simulation													</a>
<a class="popup_menu_item" href="https://store.steampowered.com/tags/en/Sports/?snr=1_5_9__12">
														Sports													</a>
<a class="popup_menu_item" href="https://store.steampowered.com/tags/en/Strategy/?snr=1_5_9__12">
														Strategy													</a>
<div class="hr"></div>
<a class="popup_menu_item" href="https://store.steampowered.com/tag/browse/?snr=1_5_9__12">
													More Popular Tags...												</a>
</div>
<!-- Software third column -->
<div class="popup_menu">
<div class="popup_menu_subheader">Software</div>
<a class="popup_menu_item" href="https://store.steampowered.com/tags/en/Animation%20%26%20Modeling/?snr=1_5_9__12">
														Animation &amp; Modeling													</a>
<a class="popup_menu_item" href="https://store.steampowered.com/tags/en/Audio%20Production/?snr=1_5_9__12">
														Audio Production													</a>
<a class="popup_menu_item" href="https://store.steampowered.com/tags/en/Design%20%26%20Illustration/?snr=1_5_9__12">
														Design &amp; Illustration													</a>
<a class="popup_menu_item" href="https://store.steampowered.com/tags/en/Education/?snr=1_5_9__12">
														Education													</a>
<a class="popup_menu_item" href="https://store.steampowered.com/tags/en/Game%20Development/?snr=1_5_9__12">
														Game Development													</a>
<a class="popup_menu_item" href="https://store.steampowered.com/tags/en/Photo%20Editing/?snr=1_5_9__12">
														Photo Editing													</a>
<a class="popup_menu_item" href="https://store.steampowered.com/tags/en/Utilities/?snr=1_5_9__12">
														Utilities													</a>
<a class="popup_menu_item" href="https://store.steampowered.com/tags/en/Video%20Production/?snr=1_5_9__12">
														Video Production													</a>
<a class="popup_menu_item" href="https://store.steampowered.com/tags/en/Web%20Publishing/?snr=1_5_9__12">
														Web Publishing													</a>
</div>
</div>
</div>
<!--                                                                 <div class="tab  flyout_tab " id="software_tab" data-flyout="software_flyout" data-flyout-align="left" data-flyout-valign="bottom">
                                    <span class="pulldown">
                                        <a class="pulldown_desktop" href="https://store.steampowered.com/software/?snr=1_5_9__12">Software</a>
                                        <a class="pulldown_mobile" href="#">Software</a>
                                        <span></span>
                                    </span>
                                </div>

                                <div class="popup_block_new flyout_tab_flyout responsive_slidedown" id="software_flyout" style="display: none;">
                                    <div class="popup_body popup_menu">
                                        <a class="popup_menu_item" href="https://store.steampowered.com/software/?snr=1_5_9__12">
                                            Software                                        </a>
                                        <div class="hr"></div>
                                                                                    <a class="popup_menu_item" href="https://store.steampowered.com/tags/en/Animation%20%26%20Modeling/?snr=1_5_9__12">
                                                Animation & Modeling                                            </a>
                                                                                    <a class="popup_menu_item" href="https://store.steampowered.com/tags/en/Audio%20Production/?snr=1_5_9__12">
                                                Audio Production                                            </a>
                                                                                    <a class="popup_menu_item" href="https://store.steampowered.com/tags/en/Design%20%26%20Illustration/?snr=1_5_9__12">
                                                Design & Illustration                                            </a>
                                                                                    <a class="popup_menu_item" href="https://store.steampowered.com/tags/en/Education/?snr=1_5_9__12">
                                                Education                                            </a>
                                                                                    <a class="popup_menu_item" href="https://store.steampowered.com/tags/en/Game%20Development/?snr=1_5_9__12">
                                                Game Development                                            </a>
                                                                                    <a class="popup_menu_item" href="https://store.steampowered.com/tags/en/Photo%20Editing/?snr=1_5_9__12">
                                                Photo Editing                                            </a>
                                                                                    <a class="popup_menu_item" href="https://store.steampowered.com/tags/en/Utilities/?snr=1_5_9__12">
                                                Utilities                                            </a>
                                                                                    <a class="popup_menu_item" href="https://store.steampowered.com/tags/en/Video%20Production/?snr=1_5_9__12">
                                                Video Production                                            </a>
                                                                                    <a class="popup_menu_item" href="https://store.steampowered.com/tags/en/Web%20Publishing/?snr=1_5_9__12">
                                                Web Publishing                                            </a>
                                        
                                    </div>
                                </div>
                             -->
<!--                                                                 <div class="tab  flyout_tab " id="hardware_tab" data-flyout="hardware_flyout" data-flyout-align="left" data-flyout-valign="bottom">
                                    <span class="pulldown">
                                        <a class="pulldown_desktop" href="https://store.steampowered.com/controller/?snr=1_5_9__12">Hardware</a>
                                        <a class="pulldown_mobile" href="#">Hardware</a>
                                        <span></span>
                                    </span>
                                </div>
                                <div class="popup_block_new flyout_tab_flyout responsive_slidedown" id="hardware_flyout" style="display: none;">
                                    <div class="popup_body popup_menu">
                                   		 <a class="popup_menu_item" href="https://store.steampowered.com/valveindex?snr=1_5_9__12">
											Valve Index<sup>&reg;</sup>                                        </a>
                                        <a class="popup_menu_item" href="https://store.steampowered.com/app/353370/?snr=1_5_9__12">
                                            Steam Controller                                        </a>
                                        <a class="popup_menu_item" href="https://store.steampowered.com/app/358040/?snr=1_5_9__12">
                                            HTC Vive                                        </a>
                                    </div>
                                </div>
                             -->
<a class="tab" href="https://store.steampowered.com/points/?snr=1_5_9__12">
<span>Points Shop</span>
</a>
<a class="tab" href="https://store.steampowered.com/news/?snr=1_5_9__12">
<span>News</span>
</a>
<a class="tab" href="https://store.steampowered.com/labs/?snr=1_5_9__12">
<span>Steam Labs</span>
</a>
<div class="search_area">
<div id="store_search">
<form action="https://store.steampowered.com/search/" id="searchform" method="get" name="searchform" onsubmit="return SearchSuggestCheckTerm(this);">
<input name="snr" type="hidden" value="1_5_9__12"/>
<div class="searchbox">
<input autocomplete="off" class="default" id="store_nav_search_term" name="term" placeholder="search the store" size="22" type="text"/>
<a href="#" id="store_search_link" onclick="var $Form = $J(this).parents('form'); $Form.submit(); return false;"><img src="https://store.cloudflare.steamstatic.com/public/images/blank.gif"/></a>
</div>
</form>
</div>
<div class="search_suggest popup_block_new" id="searchterm_options" style="display: none;">
<div class="popup_body" style="border-top: none;">
<div id="search_suggestion_contents">
</div>
</div>
</div>
</div>
</div>
</div>
<div class="store_nav_rightcap"></div>
</div>
</div>
</div>
<script type="text/javascript">
			$J( function() {
				BindAutoFlyoutEvents();

				var $Window = $J(window);
				var $Header = $J('#store_header');
				var $ResponsiveNavCtn = $J('#responsive_store_nav_ctn');
				var $HeaderWrapper;
				$Window.on('Responsive_SmallScreenModeToggled.StoreMenu', function() {
					var bUseSmallScreenMode =window.UseSmallScreenMode && window.UseSmallScreenMode();

					if ( !$HeaderWrapper )
						$HeaderWrapper = $Header.wrap( $J('<div/>', {'class': 'responsive_store_nav_ctn_spacer'} ) ).parent();

					if ( bUseSmallScreenMode )
						$ResponsiveNavCtn.append( $Header );
					else
						$HeaderWrapper.append( $Header );


					if ( bUseSmallScreenMode )
					{
						$Header.css( 'visibility', 'hidden' );
						$Header.show();
						var nMenuHeight = $J('#store_header' ).height() + $J('#store_header' ).offset().top;
						if ( $Window.scrollTop() < nMenuHeight )
							$Window.scrollTop( nMenuHeight - GetResponsiveHeaderFixedOffsetAdjustment() );

						$Header.css('visibility', 'visible');
					}
				} ).trigger('Responsive_SmallScreenModeToggled.StoreMenu');

									if( $J('#searchform').length > 0 )
					{
						var g_rgUserPreferences = {
							excluded_tags : [],
							excluded_content_descriptors : [3,4]						};
						EnableSearchSuggestions( $J('#searchform')[0].elements['term'], '1_5_9_', 'US', 1, 'english', g_rgUserPreferences, '10452513' );
					}
				

			} );
		</script>
<script type="text/javascript">
	var g_AccountID = 0;
	var g_sessionID = "97752a7f6ec9d5fec99adf7e";
	var g_ServerTime = 1610482014;

	$J( InitMiniprofileHovers );

			GStoreItemData.AddNavParams({
			__page_default: "1_5_9_",
			storemenu_recommendedtags: "1_5_9__17"		});
		GDynamicStore.Init( 0, false, "", {"primary_language":null,"secondary_languages":null,"platform_windows":null,"platform_mac":null,"platform_linux":null,"hide_adult_content_violence":null,"hide_adult_content_sex":null,"timestamp_updated":null,"hide_store_broadcast":null,"review_score_preference":null,"timestamp_content_descriptor_preferences_updated":null}, 'US' );
		GStoreItemData.SetCurrencyFormatter( function( nValueInCents, bWholeUnitsOnly ) { var fmt = function( nValueInCents, bWholeUnitsOnly ) {	var format = v_numberformat( nValueInCents / 100, bWholeUnitsOnly ? 0 : 2, ".", ","); return format; };var strNegativeSymbol = '';	if ( nValueInCents < 0 ) { strNegativeSymbol = '-'; nValueInCents = -nValueInCents; }return strNegativeSymbol + "$" + fmt( nValueInCents, bWholeUnitsOnly );} );
		GStoreItemData.SetCurrencyMinPriceIncrement( 1 );
	</script>
<div data-broadcastuser='{"success":1,"bHideStoreBroadcast":false}' data-config='{"EUNIVERSE":1,"WEB_UNIVERSE":"public","LANGUAGE":"english","COUNTRY":"US","MEDIA_CDN_COMMUNITY_URL":"https:\/\/cdn.cloudflare.steamstatic.com\/steamcommunity\/public\/","MEDIA_CDN_URL":"https:\/\/cdn.cloudflare.steamstatic.com\/","COMMUNITY_CDN_URL":"https:\/\/community.cloudflare.steamstatic.com\/","COMMUNITY_CDN_ASSET_URL":"https:\/\/cdn.cloudflare.steamstatic.com\/steamcommunity\/public\/assets\/","STORE_CDN_URL":"https:\/\/store.cloudflare.steamstatic.com\/","PUBLIC_SHARED_URL":"https:\/\/store.cloudflare.steamstatic.com\/public\/shared\/","COMMUNITY_BASE_URL":"https:\/\/steamcommunity.com\/","CHAT_BASE_URL":"https:\/\/steamcommunity.com\/","STORE_BASE_URL":"https:\/\/store.steampowered.com\/","IMG_URL":"https:\/\/store.cloudflare.steamstatic.com\/public\/images\/","STEAMTV_BASE_URL":"https:\/\/steam.tv\/","HELP_BASE_URL":"https:\/\/help.steampowered.com\/","PARTNER_BASE_URL":"https:\/\/partner.steamgames.com\/","STATS_BASE_URL":"https:\/\/partner.steampowered.com\/","INTERNAL_STATS_BASE_URL":"https:\/\/steamstats.valvesoftware.com\/","IN_CLIENT":false,"USE_POPUPS":false,"STORE_ICON_BASE_URL":"https:\/\/cdn.cloudflare.steamstatic.com\/steam\/apps\/","WEBAPI_BASE_URL":"https:\/\/api.steampowered.com\/","TOKEN_URL":"https:\/\/store.steampowered.com\/\/chat\/clientjstoken","BUILD_TIMESTAMP":1610477003,"PAGE_TIMESTAMP":1610482014,"IN_TENFOOT":false,"PLATFORM":"unknown","BASE_URL_STORE_CDN_ASSETS":"https:\/\/cdn.cloudflare.steamstatic.com\/store\/","EREALM":1}' data-userinfo='{"logged_in":false,"country_code":"US"}' id="application_config" style="display: none;"></div>
<div class="page_content_ctn" itemscope="" itemtype="http://schema.org/Product">
<meta content="https://cdn.cloudflare.steamstatic.com/steam/apps/252490/capsule_231x87.jpg?t=1608404151" itemprop="image"/>
<div itemprop="offers" itemscope="" itemtype="http://schema.org/Offer" style="display: none;">
<meta content="USD" itemprop="priceCurrency"/>
<meta content="39.99" itemprop="price"/>
</div>
<div class="page_title_area game_title_area page_content">
<div class="breadcrumbs">
<div class="blockbg">
<a href="https://store.steampowered.com/search/?term=&amp;snr=1_5_9__205">All Games</a>
																					&gt; <a href="https://store.steampowered.com/genre/Action/?snr=1_5_9__205">Action Games</a>
																				&gt; <a href="https://store.steampowered.com/app/252490/?snr=1_5_9__205"><span itemprop="name">Rust</span></a>
</div>
<div style="clear: left;"></div>
</div>
<div class="apphub_HomeHeaderContent">
<div class="apphub_HeaderStandardTop">
<div class="apphub_OtherSiteInfo">
<a class="btnv6_blue_hoverfade btn_medium" href="https://steamcommunity.com/app/252490">
<span>Community Hub</span>
</a>
</div>
<div class="apphub_AppIcon"><img src="https://cdn.cloudflare.steamstatic.com/steamcommunity/public/images/apps/252490/820be4782639f9c4b64fa3ca7e6c26a95ae4fd1c.jpg"/><div class="overlay"></div></div>
<div class="apphub_AppName">Rust</div>
<div style="clear: both"></div>
</div>
</div>
</div>
<div style="clear: left;"></div>
<div class="block">
<script type="text/javascript">
				var strRequiredVersion = "9";
				if ( typeof( g_bIsOnMac ) != 'undefined' && g_bIsOnMac )
					strRequiredVersion = "10.1.0";

			</script>
<div class="game_background_glow">
<div class="block_content page_content" id="game_highlights">
<div class="rightcol">
<div class="glance_ctn">
<div class="game_header_image_ctn">
<img class="game_header_image_full" src="https://cdn.cloudflare.steamstatic.com/steam/apps/252490/header.jpg?t=1608404151"/>
</div>
<div class="game_description_snippet">
								The only aim in Rust is to survive - Overcome struggles such as hunger, thirst and cold. Build a fire. Build a shelter. Kill animals. Protect yourself from other players.							</div>
<div class="glance_ctn_responsive_left">
<div class="user_reviews">
<div class="user_reviews_summary_row" data-tooltip-html="91% of the 23,196 user reviews in the last 30 days are positive." onclick="window.location='#app_reviews_hash'" style="cursor: pointer;">
<div class="subtitle column">Recent Reviews:</div>
<div class="summary column">
<span class="game_review_summary positive">Very Positive</span>
<span class="responsive_hidden">
													(23,196)
												</span>
<span class="nonresponsive_hidden responsive_reviewdesc">
												- 91% of the 23,196 user reviews in the last 30 days are positive.											</span>
</div>
</div>
<div class="user_reviews_summary_row" data-tooltip-html="85% of the 416,447 user reviews for this game are positive." itemprop="aggregateRating" itemscope="" itemtype="http://schema.org/AggregateRating" onclick="window.location='#app_reviews_hash'" style="cursor: pointer;">
<div class="subtitle column all">All Reviews:</div>
<div class="summary column">
<span class="game_review_summary positive" itemprop="description">Very Positive</span>
<span class="responsive_hidden">
													(416,447)
												</span>
<span class="nonresponsive_hidden responsive_reviewdesc">
												- 85% of the 416,447 user reviews for this game are positive.											</span>
<!-- microdata -->
<meta content="416447" itemprop="reviewCount"/>
<meta content="9" itemprop="ratingValue"/>
<meta content="10" itemprop="bestRating"/>
<meta content="1" itemprop="worstRating"/>
</div>
</div>
<div class="release_date">
<div class="subtitle column">Release Date:</div>
<div class="date">Feb 8, 2018</div>
</div>
<div class="dev_row">
<div class="subtitle column">Developer:</div>
<div class="summary column" id="developers_list">
<a href="https://store.steampowered.com/developer/facepunch?snr=1_5_9__2000">Facepunch Studios</a> </div>
</div>
<div class="dev_row">
<div class="subtitle column">Publisher:</div>
<div class="summary column">
<a href="https://store.steampowered.com/publisher/facepunch?snr=1_5_9__2000">Facepunch Studios</a> </div>
</div>
</div>
</div>
<div class="glance_ctn_responsive_right">
<!-- when the javascript runs, it will set these visible or not depending on what fits in the area -->
<div class="glance_tags_ctn popular_tags_ctn">
<div class="glance_tags_label">Popular user-defined tags for this product:</div>
<div class="glance_tags popular_tags" data-appid="252490">
<a class="app_tag" href="https://store.steampowered.com/tags/en/Survival/?snr=1_5_9__409" style="display: none;">
												Survival												</a><a class="app_tag" href="https://store.steampowered.com/tags/en/Crafting/?snr=1_5_9__409" style="display: none;">
												Crafting												</a><a class="app_tag" href="https://store.steampowered.com/tags/en/Multiplayer/?snr=1_5_9__409" style="display: none;">
												Multiplayer												</a><a class="app_tag" href="https://store.steampowered.com/tags/en/Open%20World/?snr=1_5_9__409" style="display: none;">
												Open World												</a><a class="app_tag" href="https://store.steampowered.com/tags/en/Open%20World%20Survival%20Craft/?snr=1_5_9__409" style="display: none;">
												Open World Survival Craft												</a><a class="app_tag" href="https://store.steampowered.com/tags/en/Building/?snr=1_5_9__409" style="display: none;">
												Building												</a><a class="app_tag" href="https://store.steampowered.com/tags/en/Sandbox/?snr=1_5_9__409" style="display: none;">
												Sandbox												</a><a class="app_tag" href="https://store.steampowered.com/tags/en/PvP/?snr=1_5_9__409" style="display: none;">
												PvP												</a><a class="app_tag" href="https://store.steampowered.com/tags/en/Adventure/?snr=1_5_9__409" style="display: none;">
												Adventure												</a><a class="app_tag" href="https://store.steampowered.com/tags/en/First-Person/?snr=1_5_9__409" style="display: none;">
												First-Person												</a><a class="app_tag" href="https://store.steampowered.com/tags/en/Action/?snr=1_5_9__409" style="display: none;">
												Action												</a><a class="app_tag" href="https://store.steampowered.com/tags/en/FPS/?snr=1_5_9__409" style="display: none;">
												FPS												</a><a class="app_tag" href="https://store.steampowered.com/tags/en/Nudity/?snr=1_5_9__409" style="display: none;">
												Nudity												</a><a class="app_tag" href="https://store.steampowered.com/tags/en/Co-op/?snr=1_5_9__409" style="display: none;">
												Co-op												</a><a class="app_tag" href="https://store.steampowered.com/tags/en/Shooter/?snr=1_5_9__409" style="display: none;">
												Shooter												</a><a class="app_tag" href="https://store.steampowered.com/tags/en/Online%20Co-Op/?snr=1_5_9__409" style="display: none;">
												Online Co-Op												</a><a class="app_tag" href="https://store.steampowered.com/tags/en/Indie/?snr=1_5_9__409" style="display: none;">
												Indie												</a><a class="app_tag" href="https://store.steampowered.com/tags/en/Early%20Access/?snr=1_5_9__409" style="display: none;">
												Early Access												</a><a class="app_tag" href="https://store.steampowered.com/tags/en/Post-apocalyptic/?snr=1_5_9__409" style="display: none;">
												Post-apocalyptic												</a><a class="app_tag" href="https://store.steampowered.com/tags/en/Simulation/?snr=1_5_9__409" style="display: none;">
												Simulation												</a><div class="app_tag add_button" onclick="ShowAppTagModal( 252490 )">+</div>
</div>
</div>
</div>
<div style="clear: both;"></div>
</div>
</div>
<div class="leftcol">
<div class="highlight_ctn">
<div class="highlight_overflow">
<div id="highlight_player_area">
<div class="highlight_player_area_spacer">
<img src="https://store.cloudflare.steamstatic.com/public/images/game/game_highlight_image_spacer.gif"/>
</div>
<div class="highlight_player_item highlight_movie" data-mp4-hd-source="https://cdn.cloudflare.steamstatic.com/steam/apps/256684736/movie_max.mp4?t=1518121486" data-mp4-source="https://cdn.cloudflare.steamstatic.com/steam/apps/256684736/movie480.mp4?t=1518121486" data-poster="https://cdn.cloudflare.steamstatic.com/steam/apps/256684736/movie.293x165.jpg?t=1518121486" data-webm-hd-source="https://cdn.cloudflare.steamstatic.com/steam/apps/256684736/movie_max.webm?t=1518121486" data-webm-source="https://cdn.cloudflare.steamstatic.com/steam/apps/256684736/movie480.webm?t=1518121486" id="highlight_movie_256684736" style="display: none;">
</div>
<div class="highlight_player_item highlight_movie" data-mp4-hd-source="https://cdn.cloudflare.steamstatic.com/steam/apps/256791647/movie_max.mp4?t=1593743141" data-mp4-source="https://cdn.cloudflare.steamstatic.com/steam/apps/256791647/movie480.mp4?t=1593743141" data-poster="https://cdn.cloudflare.steamstatic.com/steam/apps/256791647/movie.293x165.jpg?t=1593743141" data-webm-hd-source="https://cdn.cloudflare.steamstatic.com/steam/apps/256791647/movie_max_vp9.webm?t=1593743141" data-webm-source="https://cdn.cloudflare.steamstatic.com/steam/apps/256791647/movie480_vp9.webm?t=1593743141" id="highlight_movie_256791647" style="display: none;">
</div>
<div class="highlight_player_item highlight_movie" data-mp4-hd-source="https://cdn.cloudflare.steamstatic.com/steam/apps/256761600/movie_max.mp4?t=1568120227" data-mp4-source="https://cdn.cloudflare.steamstatic.com/steam/apps/256761600/movie480.mp4?t=1568120227" data-poster="https://cdn.cloudflare.steamstatic.com/steam/apps/256761600/movie.293x165.jpg?t=1568120227" data-webm-hd-source="https://cdn.cloudflare.steamstatic.com/steam/apps/256761600/movie_max.webm?t=1568120227" data-webm-source="https://cdn.cloudflare.steamstatic.com/steam/apps/256761600/movie480.webm?t=1568120227" id="highlight_movie_256761600" style="display: none;">
</div>
<div class="highlight_player_item highlight_movie" data-mp4-hd-source="https://cdn.cloudflare.steamstatic.com/steam/apps/256761603/movie_max.mp4?t=1568120218" data-mp4-source="https://cdn.cloudflare.steamstatic.com/steam/apps/256761603/movie480.mp4?t=1568120218" data-poster="https://cdn.cloudflare.steamstatic.com/steam/apps/256761603/movie.293x165.jpg?t=1568120218" data-webm-hd-source="https://cdn.cloudflare.steamstatic.com/steam/apps/256761603/movie_max.webm?t=1568120218" data-webm-source="https://cdn.cloudflare.steamstatic.com/steam/apps/256761603/movie480.webm?t=1568120218" id="highlight_movie_256761603" style="display: none;">
</div>
<div class="highlight_player_item highlight_screenshot" id="highlight_screenshot_ss_9652dbaf2de41b8c8f8305af714ee258564c453d.jpg" style="display: none;">
<div class="screenshot_holder">
<a class="highlight_screenshot_link" data-screenshotid="ss_9652dbaf2de41b8c8f8305af714ee258564c453d.jpg" href="https://cdn.cloudflare.steamstatic.com/steam/apps/252490/ss_9652dbaf2de41b8c8f8305af714ee258564c453d.1920x1080.jpg?t=1608404151" rel="noreferrer" target="_blank">
<img src="https://store.cloudflare.steamstatic.com/public/images/blank.gif"/>
</a>
</div>
</div>
<div class="highlight_player_item highlight_screenshot" id="highlight_screenshot_ss_39740ea705e70bdf3d5c3f72167f2b94d2db92f8.jpg" style="display: none;">
<div class="screenshot_holder">
<a class="highlight_screenshot_link" data-screenshotid="ss_39740ea705e70bdf3d5c3f72167f2b94d2db92f8.jpg" href="https://cdn.cloudflare.steamstatic.com/steam/apps/252490/ss_39740ea705e70bdf3d5c3f72167f2b94d2db92f8.1920x1080.jpg?t=1608404151" rel="noreferrer" target="_blank">
<img src="https://store.cloudflare.steamstatic.com/public/images/blank.gif"/>
</a>
</div>
</div>
<div class="highlight_player_item highlight_screenshot" id="highlight_screenshot_ss_0e646f1a70e5cb8eed00efef8adb9579d40d5b2e.jpg" style="display: none;">
<div class="screenshot_holder">
<a class="highlight_screenshot_link" data-screenshotid="ss_0e646f1a70e5cb8eed00efef8adb9579d40d5b2e.jpg" href="https://cdn.cloudflare.steamstatic.com/steam/apps/252490/ss_0e646f1a70e5cb8eed00efef8adb9579d40d5b2e.1920x1080.jpg?t=1608404151" rel="noreferrer" target="_blank">
<img src="https://store.cloudflare.steamstatic.com/public/images/blank.gif"/>
</a>
</div>
</div>
<div class="highlight_player_item highlight_screenshot" id="highlight_screenshot_ss_f05168330593f4f476cd4a6a6094b248c7c8556e.jpg" style="display: none;">
<div class="screenshot_holder">
<a class="highlight_screenshot_link" data-screenshotid="ss_f05168330593f4f476cd4a6a6094b248c7c8556e.jpg" href="https://cdn.cloudflare.steamstatic.com/steam/apps/252490/ss_f05168330593f4f476cd4a6a6094b248c7c8556e.1920x1080.jpg?t=1608404151" rel="noreferrer" target="_blank">
<img src="https://store.cloudflare.steamstatic.com/public/images/blank.gif"/>
</a>
</div>
</div>
<div class="highlight_player_item highlight_screenshot" id="highlight_screenshot_ss_a63f203245f322f28cf489bf46beaeec780cccec.jpg" style="display: none;">
<div class="screenshot_holder">
<a class="highlight_screenshot_link" data-screenshotid="ss_a63f203245f322f28cf489bf46beaeec780cccec.jpg" href="https://cdn.cloudflare.steamstatic.com/steam/apps/252490/ss_a63f203245f322f28cf489bf46beaeec780cccec.1920x1080.jpg?t=1608404151" rel="noreferrer" target="_blank">
<img src="https://store.cloudflare.steamstatic.com/public/images/blank.gif"/>
</a>
</div>
</div>
<div class="highlight_player_item highlight_screenshot" id="highlight_screenshot_ss_2a8518810024a5fbf9c714e697a43a1201b5d53e.jpg" style="display: none;">
<div class="screenshot_holder">
<a class="highlight_screenshot_link" data-screenshotid="ss_2a8518810024a5fbf9c714e697a43a1201b5d53e.jpg" href="https://cdn.cloudflare.steamstatic.com/steam/apps/252490/ss_2a8518810024a5fbf9c714e697a43a1201b5d53e.1920x1080.jpg?t=1608404151" rel="noreferrer" target="_blank">
<img src="https://store.cloudflare.steamstatic.com/public/images/blank.gif"/>
</a>
</div>
</div>
<div class="highlight_player_item highlight_screenshot" id="highlight_screenshot_ss_03baf60f7ea967235606f130249ed791157ef922.jpg" style="display: none;">
<div class="screenshot_holder">
<a class="highlight_screenshot_link" data-screenshotid="ss_03baf60f7ea967235606f130249ed791157ef922.jpg" href="https://cdn.cloudflare.steamstatic.com/steam/apps/252490/ss_03baf60f7ea967235606f130249ed791157ef922.1920x1080.jpg?t=1608404151" rel="noreferrer" target="_blank">
<img src="https://store.cloudflare.steamstatic.com/public/images/blank.gif"/>
</a>
</div>
</div>
<div class="highlight_player_item highlight_screenshot" id="highlight_screenshot_ss_830f94ec6e62142da296aa760cfc681d454c466e.jpg" style="display: none;">
<div class="screenshot_holder">
<a class="highlight_screenshot_link" data-screenshotid="ss_830f94ec6e62142da296aa760cfc681d454c466e.jpg" href="https://cdn.cloudflare.steamstatic.com/steam/apps/252490/ss_830f94ec6e62142da296aa760cfc681d454c466e.1920x1080.jpg?t=1608404151" rel="noreferrer" target="_blank">
<img src="https://store.cloudflare.steamstatic.com/public/images/blank.gif"/>
</a>
</div>
</div>
<div class="highlight_player_item highlight_screenshot" id="highlight_screenshot_ss_e0d27fd0174504796ae5e15eba91d6f576f95330.jpg" style="display: none;">
<div class="screenshot_holder">
<a class="highlight_screenshot_link" data-screenshotid="ss_e0d27fd0174504796ae5e15eba91d6f576f95330.jpg" href="https://cdn.cloudflare.steamstatic.com/steam/apps/252490/ss_e0d27fd0174504796ae5e15eba91d6f576f95330.1920x1080.jpg?t=1608404151" rel="noreferrer" target="_blank">
<img src="https://store.cloudflare.steamstatic.com/public/images/blank.gif"/>
</a>
</div>
</div>
<div class="highlight_player_item highlight_screenshot" id="highlight_screenshot_ss_1d6dd798ec9ebe3b6da69483bfcdd19e7300971c.jpg" style="display: none;">
<div class="screenshot_holder">
<a class="highlight_screenshot_link" data-screenshotid="ss_1d6dd798ec9ebe3b6da69483bfcdd19e7300971c.jpg" href="https://cdn.cloudflare.steamstatic.com/steam/apps/252490/ss_1d6dd798ec9ebe3b6da69483bfcdd19e7300971c.1920x1080.jpg?t=1608404151" rel="noreferrer" target="_blank">
<img src="https://store.cloudflare.steamstatic.com/public/images/blank.gif"/>
</a>
</div>
</div>
<div class="highlight_player_item highlight_screenshot" id="highlight_screenshot_ss_58c5b4107fbd90f5a56b3adc97a6b61384ce4f12.jpg" style="display: none;">
<div class="screenshot_holder">
<a class="highlight_screenshot_link" data-screenshotid="ss_58c5b4107fbd90f5a56b3adc97a6b61384ce4f12.jpg" href="https://cdn.cloudflare.steamstatic.com/steam/apps/252490/ss_58c5b4107fbd90f5a56b3adc97a6b61384ce4f12.1920x1080.jpg?t=1608404151" rel="noreferrer" target="_blank">
<img src="https://store.cloudflare.steamstatic.com/public/images/blank.gif"/>
</a>
</div>
</div>
<div class="highlight_player_item highlight_screenshot" id="highlight_screenshot_ss_803a18bcbf6004706f12a1f88bb3cadbd9ac5f5b.jpg" style="display: none;">
<div class="screenshot_holder">
<a class="highlight_screenshot_link" data-screenshotid="ss_803a18bcbf6004706f12a1f88bb3cadbd9ac5f5b.jpg" href="https://cdn.cloudflare.steamstatic.com/steam/apps/252490/ss_803a18bcbf6004706f12a1f88bb3cadbd9ac5f5b.1920x1080.jpg?t=1608404151" rel="noreferrer" target="_blank">
<img src="https://store.cloudflare.steamstatic.com/public/images/blank.gif"/>
</a>
</div>
</div>
<div class="highlight_player_item highlight_screenshot" id="highlight_screenshot_ss_297da1914b2de9c380e8c77478d9774958f49a9c.jpg" style="display: none;">
<div class="screenshot_holder">
<a class="highlight_screenshot_link" data-screenshotid="ss_297da1914b2de9c380e8c77478d9774958f49a9c.jpg" href="https://cdn.cloudflare.steamstatic.com/steam/apps/252490/ss_297da1914b2de9c380e8c77478d9774958f49a9c.1920x1080.jpg?t=1608404151" rel="noreferrer" target="_blank">
<img src="https://store.cloudflare.steamstatic.com/public/images/blank.gif"/>
</a>
</div>
</div>
<div class="highlight_player_item highlight_screenshot" id="highlight_screenshot_ss_651097c65458ae555b42c42dd9667d7174397bdf.jpg" style="display: none;">
<div class="screenshot_holder">
<a class="highlight_screenshot_link" data-screenshotid="ss_651097c65458ae555b42c42dd9667d7174397bdf.jpg" href="https://cdn.cloudflare.steamstatic.com/steam/apps/252490/ss_651097c65458ae555b42c42dd9667d7174397bdf.1920x1080.jpg?t=1608404151" rel="noreferrer" target="_blank">
<img src="https://store.cloudflare.steamstatic.com/public/images/blank.gif"/>
</a>
</div>
</div>
<div class="highlight_player_item highlight_screenshot" id="highlight_screenshot_ss_6b729c0a2a0db015a238154ce78feca76c890b55.jpg" style="display: none;">
<div class="screenshot_holder">
<a class="highlight_screenshot_link" data-screenshotid="ss_6b729c0a2a0db015a238154ce78feca76c890b55.jpg" href="https://cdn.cloudflare.steamstatic.com/steam/apps/252490/ss_6b729c0a2a0db015a238154ce78feca76c890b55.1920x1080.jpg?t=1608404151" rel="noreferrer" target="_blank">
<img src="https://store.cloudflare.steamstatic.com/public/images/blank.gif"/>
</a>
</div>
</div>
<div class="highlight_player_item highlight_screenshot" id="highlight_screenshot_ss_326282c7485e8aff1ebf6750c82622afef098998.jpg" style="display: none;">
<div class="screenshot_holder">
<a class="highlight_screenshot_link" data-screenshotid="ss_326282c7485e8aff1ebf6750c82622afef098998.jpg" href="https://cdn.cloudflare.steamstatic.com/steam/apps/252490/ss_326282c7485e8aff1ebf6750c82622afef098998.1920x1080.jpg?t=1608404151" rel="noreferrer" target="_blank">
<img src="https://store.cloudflare.steamstatic.com/public/images/blank.gif"/>
</a>
</div>
</div>
<div class="highlight_player_item highlight_screenshot" id="highlight_screenshot_ss_9264a17b6bc1b3f9df55cf2aafcc25c6188bba59.jpg" style="display: none;">
<div class="screenshot_holder">
<a class="highlight_screenshot_link" data-screenshotid="ss_9264a17b6bc1b3f9df55cf2aafcc25c6188bba59.jpg" href="https://cdn.cloudflare.steamstatic.com/steam/apps/252490/ss_9264a17b6bc1b3f9df55cf2aafcc25c6188bba59.1920x1080.jpg?t=1608404151" rel="noreferrer" target="_blank">
<img src="https://store.cloudflare.steamstatic.com/public/images/blank.gif"/>
</a>
</div>
</div>
<div class="highlight_player_item highlight_screenshot" id="highlight_screenshot_ss_54c335670b8beba01e7330263751bda74dcd72f1.jpg" style="display: none;">
<div class="screenshot_holder">
<a class="highlight_screenshot_link" data-screenshotid="ss_54c335670b8beba01e7330263751bda74dcd72f1.jpg" href="https://cdn.cloudflare.steamstatic.com/steam/apps/252490/ss_54c335670b8beba01e7330263751bda74dcd72f1.1920x1080.jpg?t=1608404151" rel="noreferrer" target="_blank">
<img src="https://store.cloudflare.steamstatic.com/public/images/blank.gif"/>
</a>
</div>
</div>
<div class="highlight_player_item highlight_screenshot" id="highlight_screenshot_ss_652294496bc3f4626dbcdfdd0ff60d5e7398c25e.jpg" style="display: none;">
<div class="screenshot_holder">
<a class="highlight_screenshot_link" data-screenshotid="ss_652294496bc3f4626dbcdfdd0ff60d5e7398c25e.jpg" href="https://cdn.cloudflare.steamstatic.com/steam/apps/252490/ss_652294496bc3f4626dbcdfdd0ff60d5e7398c25e.1920x1080.jpg?t=1608404151" rel="noreferrer" target="_blank">
<img src="https://store.cloudflare.steamstatic.com/public/images/blank.gif"/>
</a>
</div>
</div>
<div class="highlight_player_item highlight_screenshot" id="highlight_screenshot_ss_4f2d0e89f55bcf236bb64c72736104c44aa50275.jpg" style="display: none;">
<div class="screenshot_holder">
<a class="highlight_screenshot_link" data-screenshotid="ss_4f2d0e89f55bcf236bb64c72736104c44aa50275.jpg" href="https://cdn.cloudflare.steamstatic.com/steam/apps/252490/ss_4f2d0e89f55bcf236bb64c72736104c44aa50275.1920x1080.jpg?t=1608404151" rel="noreferrer" target="_blank">
<img src="https://store.cloudflare.steamstatic.com/public/images/blank.gif"/>
</a>
</div>
</div>
<div class="highlight_player_item highlight_screenshot" id="highlight_screenshot_ss_8880205af12b492f866479477b9a98e731f956d2.jpg" style="display: none;">
<div class="screenshot_holder">
<a class="highlight_screenshot_link" data-screenshotid="ss_8880205af12b492f866479477b9a98e731f956d2.jpg" href="https://cdn.cloudflare.steamstatic.com/steam/apps/252490/ss_8880205af12b492f866479477b9a98e731f956d2.1920x1080.jpg?t=1608404151" rel="noreferrer" target="_blank">
<img src="https://store.cloudflare.steamstatic.com/public/images/blank.gif"/>
</a>
</div>
</div>
<div class="highlight_player_item highlight_screenshot" id="highlight_screenshot_ss_f78385eb47e11f046f696e09d5bfa4d329017b1e.jpg" style="display: none;">
<div class="screenshot_holder">
<a class="highlight_screenshot_link" data-screenshotid="ss_f78385eb47e11f046f696e09d5bfa4d329017b1e.jpg" href="https://cdn.cloudflare.steamstatic.com/steam/apps/252490/ss_f78385eb47e11f046f696e09d5bfa4d329017b1e.1920x1080.jpg?t=1608404151" rel="noreferrer" target="_blank">
<img src="https://store.cloudflare.steamstatic.com/public/images/blank.gif"/>
</a>
</div>
</div>
<div class="highlight_player_item highlight_screenshot" id="highlight_screenshot_ss_c21e99d11d22a035744cfb974ee03647c1e628c5.jpg" style="display: none;">
<div class="screenshot_holder">
<a class="highlight_screenshot_link" data-screenshotid="ss_c21e99d11d22a035744cfb974ee03647c1e628c5.jpg" href="https://cdn.cloudflare.steamstatic.com/steam/apps/252490/ss_c21e99d11d22a035744cfb974ee03647c1e628c5.1920x1080.jpg?t=1608404151" rel="noreferrer" target="_blank">
<img src="https://store.cloudflare.steamstatic.com/public/images/blank.gif"/>
</a>
</div>
</div>
<div class="highlight_player_item highlight_screenshot" id="highlight_screenshot_ss_4bd74e976bc5e2c519cd0011b7192a20126253b9.jpg" style="display: none;">
<div class="screenshot_holder">
<a class="highlight_screenshot_link" data-screenshotid="ss_4bd74e976bc5e2c519cd0011b7192a20126253b9.jpg" href="https://cdn.cloudflare.steamstatic.com/steam/apps/252490/ss_4bd74e976bc5e2c519cd0011b7192a20126253b9.1920x1080.jpg?t=1608404151" rel="noreferrer" target="_blank">
<img src="https://store.cloudflare.steamstatic.com/public/images/blank.gif"/>
</a>
</div>
</div>
<div class="highlight_player_item highlight_screenshot" id="highlight_screenshot_ss_6c71cf2f4b13fdaed53f5b0de381a9c9227b9c78.jpg" style="display: none;">
<div class="screenshot_holder">
<a class="highlight_screenshot_link" data-screenshotid="ss_6c71cf2f4b13fdaed53f5b0de381a9c9227b9c78.jpg" href="https://cdn.cloudflare.steamstatic.com/steam/apps/252490/ss_6c71cf2f4b13fdaed53f5b0de381a9c9227b9c78.1920x1080.jpg?t=1608404151" rel="noreferrer" target="_blank">
<img src="https://store.cloudflare.steamstatic.com/public/images/blank.gif"/>
</a>
</div>
</div>
<div class="highlight_player_item highlight_screenshot" id="highlight_screenshot_ss_234b12804c91c911e4095fcb872ef7f1a1371ca2.jpg" style="display: none;">
<div class="screenshot_holder">
<a class="highlight_screenshot_link" data-screenshotid="ss_234b12804c91c911e4095fcb872ef7f1a1371ca2.jpg" href="https://cdn.cloudflare.steamstatic.com/steam/apps/252490/ss_234b12804c91c911e4095fcb872ef7f1a1371ca2.1920x1080.jpg?t=1608404151" rel="noreferrer" target="_blank">
<img src="https://store.cloudflare.steamstatic.com/public/images/blank.gif"/>
</a>
</div>
</div>
<div class="highlight_player_item highlight_screenshot" id="highlight_screenshot_ss_9b15e65273879b475a4d223fb4af181fbd8960ef.jpg" style="display: none;">
<div class="screenshot_holder">
<a class="highlight_screenshot_link" data-screenshotid="ss_9b15e65273879b475a4d223fb4af181fbd8960ef.jpg" href="https://cdn.cloudflare.steamstatic.com/steam/apps/252490/ss_9b15e65273879b475a4d223fb4af181fbd8960ef.1920x1080.jpg?t=1608404151" rel="noreferrer" target="_blank">
<img src="https://store.cloudflare.steamstatic.com/public/images/blank.gif"/>
</a>
</div>
</div>
<script type="text/javascript">
																		var rgScreenshotURLs = {"ss_9652dbaf2de41b8c8f8305af714ee258564c453d.jpg":"https:\/\/cdn.cloudflare.steamstatic.com\/steam\/apps\/252490\/ss_9652dbaf2de41b8c8f8305af714ee258564c453d_SIZE_.jpg?t=1608404151","ss_39740ea705e70bdf3d5c3f72167f2b94d2db92f8.jpg":"https:\/\/cdn.cloudflare.steamstatic.com\/steam\/apps\/252490\/ss_39740ea705e70bdf3d5c3f72167f2b94d2db92f8_SIZE_.jpg?t=1608404151","ss_0e646f1a70e5cb8eed00efef8adb9579d40d5b2e.jpg":"https:\/\/cdn.cloudflare.steamstatic.com\/steam\/apps\/252490\/ss_0e646f1a70e5cb8eed00efef8adb9579d40d5b2e_SIZE_.jpg?t=1608404151","ss_f05168330593f4f476cd4a6a6094b248c7c8556e.jpg":"https:\/\/cdn.cloudflare.steamstatic.com\/steam\/apps\/252490\/ss_f05168330593f4f476cd4a6a6094b248c7c8556e_SIZE_.jpg?t=1608404151","ss_a63f203245f322f28cf489bf46beaeec780cccec.jpg":"https:\/\/cdn.cloudflare.steamstatic.com\/steam\/apps\/252490\/ss_a63f203245f322f28cf489bf46beaeec780cccec_SIZE_.jpg?t=1608404151","ss_2a8518810024a5fbf9c714e697a43a1201b5d53e.jpg":"https:\/\/cdn.cloudflare.steamstatic.com\/steam\/apps\/252490\/ss_2a8518810024a5fbf9c714e697a43a1201b5d53e_SIZE_.jpg?t=1608404151","ss_03baf60f7ea967235606f130249ed791157ef922.jpg":"https:\/\/cdn.cloudflare.steamstatic.com\/steam\/apps\/252490\/ss_03baf60f7ea967235606f130249ed791157ef922_SIZE_.jpg?t=1608404151","ss_830f94ec6e62142da296aa760cfc681d454c466e.jpg":"https:\/\/cdn.cloudflare.steamstatic.com\/steam\/apps\/252490\/ss_830f94ec6e62142da296aa760cfc681d454c466e_SIZE_.jpg?t=1608404151","ss_e0d27fd0174504796ae5e15eba91d6f576f95330.jpg":"https:\/\/cdn.cloudflare.steamstatic.com\/steam\/apps\/252490\/ss_e0d27fd0174504796ae5e15eba91d6f576f95330_SIZE_.jpg?t=1608404151","ss_1d6dd798ec9ebe3b6da69483bfcdd19e7300971c.jpg":"https:\/\/cdn.cloudflare.steamstatic.com\/steam\/apps\/252490\/ss_1d6dd798ec9ebe3b6da69483bfcdd19e7300971c_SIZE_.jpg?t=1608404151","ss_58c5b4107fbd90f5a56b3adc97a6b61384ce4f12.jpg":"https:\/\/cdn.cloudflare.steamstatic.com\/steam\/apps\/252490\/ss_58c5b4107fbd90f5a56b3adc97a6b61384ce4f12_SIZE_.jpg?t=1608404151","ss_803a18bcbf6004706f12a1f88bb3cadbd9ac5f5b.jpg":"https:\/\/cdn.cloudflare.steamstatic.com\/steam\/apps\/252490\/ss_803a18bcbf6004706f12a1f88bb3cadbd9ac5f5b_SIZE_.jpg?t=1608404151","ss_297da1914b2de9c380e8c77478d9774958f49a9c.jpg":"https:\/\/cdn.cloudflare.steamstatic.com\/steam\/apps\/252490\/ss_297da1914b2de9c380e8c77478d9774958f49a9c_SIZE_.jpg?t=1608404151","ss_651097c65458ae555b42c42dd9667d7174397bdf.jpg":"https:\/\/cdn.cloudflare.steamstatic.com\/steam\/apps\/252490\/ss_651097c65458ae555b42c42dd9667d7174397bdf_SIZE_.jpg?t=1608404151","ss_6b729c0a2a0db015a238154ce78feca76c890b55.jpg":"https:\/\/cdn.cloudflare.steamstatic.com\/steam\/apps\/252490\/ss_6b729c0a2a0db015a238154ce78feca76c890b55_SIZE_.jpg?t=1608404151","ss_326282c7485e8aff1ebf6750c82622afef098998.jpg":"https:\/\/cdn.cloudflare.steamstatic.com\/steam\/apps\/252490\/ss_326282c7485e8aff1ebf6750c82622afef098998_SIZE_.jpg?t=1608404151","ss_9264a17b6bc1b3f9df55cf2aafcc25c6188bba59.jpg":"https:\/\/cdn.cloudflare.steamstatic.com\/steam\/apps\/252490\/ss_9264a17b6bc1b3f9df55cf2aafcc25c6188bba59_SIZE_.jpg?t=1608404151","ss_54c335670b8beba01e7330263751bda74dcd72f1.jpg":"https:\/\/cdn.cloudflare.steamstatic.com\/steam\/apps\/252490\/ss_54c335670b8beba01e7330263751bda74dcd72f1_SIZE_.jpg?t=1608404151","ss_652294496bc3f4626dbcdfdd0ff60d5e7398c25e.jpg":"https:\/\/cdn.cloudflare.steamstatic.com\/steam\/apps\/252490\/ss_652294496bc3f4626dbcdfdd0ff60d5e7398c25e_SIZE_.jpg?t=1608404151","ss_4f2d0e89f55bcf236bb64c72736104c44aa50275.jpg":"https:\/\/cdn.cloudflare.steamstatic.com\/steam\/apps\/252490\/ss_4f2d0e89f55bcf236bb64c72736104c44aa50275_SIZE_.jpg?t=1608404151","ss_8880205af12b492f866479477b9a98e731f956d2.jpg":"https:\/\/cdn.cloudflare.steamstatic.com\/steam\/apps\/252490\/ss_8880205af12b492f866479477b9a98e731f956d2_SIZE_.jpg?t=1608404151","ss_f78385eb47e11f046f696e09d5bfa4d329017b1e.jpg":"https:\/\/cdn.cloudflare.steamstatic.com\/steam\/apps\/252490\/ss_f78385eb47e11f046f696e09d5bfa4d329017b1e_SIZE_.jpg?t=1608404151","ss_c21e99d11d22a035744cfb974ee03647c1e628c5.jpg":"https:\/\/cdn.cloudflare.steamstatic.com\/steam\/apps\/252490\/ss_c21e99d11d22a035744cfb974ee03647c1e628c5_SIZE_.jpg?t=1608404151","ss_4bd74e976bc5e2c519cd0011b7192a20126253b9.jpg":"https:\/\/cdn.cloudflare.steamstatic.com\/steam\/apps\/252490\/ss_4bd74e976bc5e2c519cd0011b7192a20126253b9_SIZE_.jpg?t=1608404151","ss_6c71cf2f4b13fdaed53f5b0de381a9c9227b9c78.jpg":"https:\/\/cdn.cloudflare.steamstatic.com\/steam\/apps\/252490\/ss_6c71cf2f4b13fdaed53f5b0de381a9c9227b9c78_SIZE_.jpg?t=1608404151","ss_234b12804c91c911e4095fcb872ef7f1a1371ca2.jpg":"https:\/\/cdn.cloudflare.steamstatic.com\/steam\/apps\/252490\/ss_234b12804c91c911e4095fcb872ef7f1a1371ca2_SIZE_.jpg?t=1608404151","ss_9b15e65273879b475a4d223fb4af181fbd8960ef.jpg":"https:\/\/cdn.cloudflare.steamstatic.com\/steam\/apps\/252490\/ss_9b15e65273879b475a4d223fb4af181fbd8960ef_SIZE_.jpg?t=1608404151"};
								</script>
</div>
<div id="highlight_strip">
<div id="highlight_strip_scroll" style="width: 3722px;">
<div class="highlight_selector"></div>
<div class="highlight_strip_item highlight_strip_movie" id="thumb_movie_256684736">
<img class="movie_thumb" src="https://cdn.cloudflare.steamstatic.com/steam/apps/256684736/movie.184x123.jpg?t=1518121486"/>
<div class="highlight_movie_marker"></div>
</div>
<div class="highlight_strip_item highlight_strip_movie" id="thumb_movie_256791647">
<img class="movie_thumb" src="https://cdn.cloudflare.steamstatic.com/steam/apps/256791647/movie.184x123.jpg?t=1593743141"/>
<div class="highlight_movie_marker"></div>
</div>
<div class="highlight_strip_item highlight_strip_movie" id="thumb_movie_256761600">
<img class="movie_thumb" src="https://cdn.cloudflare.steamstatic.com/steam/apps/256761600/movie.184x123.jpg?t=1568120227"/>
<div class="highlight_movie_marker"></div>
</div>
<div class="highlight_strip_item highlight_strip_movie" id="thumb_movie_256761603">
<img class="movie_thumb" src="https://cdn.cloudflare.steamstatic.com/steam/apps/256761603/movie.184x123.jpg?t=1568120218"/>
<div class="highlight_movie_marker"></div>
</div>
<div class="highlight_strip_item highlight_strip_screenshot" id="thumb_screenshot_ss_9652dbaf2de41b8c8f8305af714ee258564c453d.jpg">
<img src="https://cdn.cloudflare.steamstatic.com/steam/apps/252490/ss_9652dbaf2de41b8c8f8305af714ee258564c453d.116x65.jpg?t=1608404151"/>
</div>
<div class="highlight_strip_item highlight_strip_screenshot" id="thumb_screenshot_ss_39740ea705e70bdf3d5c3f72167f2b94d2db92f8.jpg">
<img src="https://cdn.cloudflare.steamstatic.com/steam/apps/252490/ss_39740ea705e70bdf3d5c3f72167f2b94d2db92f8.116x65.jpg?t=1608404151"/>
</div>
<div class="highlight_strip_item highlight_strip_screenshot" id="thumb_screenshot_ss_0e646f1a70e5cb8eed00efef8adb9579d40d5b2e.jpg">
<img src="https://cdn.cloudflare.steamstatic.com/steam/apps/252490/ss_0e646f1a70e5cb8eed00efef8adb9579d40d5b2e.116x65.jpg?t=1608404151"/>
</div>
<div class="highlight_strip_item highlight_strip_screenshot" id="thumb_screenshot_ss_f05168330593f4f476cd4a6a6094b248c7c8556e.jpg">
<img src="https://cdn.cloudflare.steamstatic.com/steam/apps/252490/ss_f05168330593f4f476cd4a6a6094b248c7c8556e.116x65.jpg?t=1608404151"/>
</div>
<div class="highlight_strip_item highlight_strip_screenshot" id="thumb_screenshot_ss_a63f203245f322f28cf489bf46beaeec780cccec.jpg">
<img src="https://cdn.cloudflare.steamstatic.com/steam/apps/252490/ss_a63f203245f322f28cf489bf46beaeec780cccec.116x65.jpg?t=1608404151"/>
</div>
<div class="highlight_strip_item highlight_strip_screenshot" id="thumb_screenshot_ss_2a8518810024a5fbf9c714e697a43a1201b5d53e.jpg">
<img src="https://cdn.cloudflare.steamstatic.com/steam/apps/252490/ss_2a8518810024a5fbf9c714e697a43a1201b5d53e.116x65.jpg?t=1608404151"/>
</div>
<div class="highlight_strip_item highlight_strip_screenshot" id="thumb_screenshot_ss_03baf60f7ea967235606f130249ed791157ef922.jpg">
<img src="https://cdn.cloudflare.steamstatic.com/steam/apps/252490/ss_03baf60f7ea967235606f130249ed791157ef922.116x65.jpg?t=1608404151"/>
</div>
<div class="highlight_strip_item highlight_strip_screenshot" id="thumb_screenshot_ss_830f94ec6e62142da296aa760cfc681d454c466e.jpg">
<img src="https://cdn.cloudflare.steamstatic.com/steam/apps/252490/ss_830f94ec6e62142da296aa760cfc681d454c466e.116x65.jpg?t=1608404151"/>
</div>
<div class="highlight_strip_item highlight_strip_screenshot" id="thumb_screenshot_ss_e0d27fd0174504796ae5e15eba91d6f576f95330.jpg">
<img src="https://cdn.cloudflare.steamstatic.com/steam/apps/252490/ss_e0d27fd0174504796ae5e15eba91d6f576f95330.116x65.jpg?t=1608404151"/>
</div>
<div class="highlight_strip_item highlight_strip_screenshot" id="thumb_screenshot_ss_1d6dd798ec9ebe3b6da69483bfcdd19e7300971c.jpg">
<img src="https://cdn.cloudflare.steamstatic.com/steam/apps/252490/ss_1d6dd798ec9ebe3b6da69483bfcdd19e7300971c.116x65.jpg?t=1608404151"/>
</div>
<div class="highlight_strip_item highlight_strip_screenshot" id="thumb_screenshot_ss_58c5b4107fbd90f5a56b3adc97a6b61384ce4f12.jpg">
<img src="https://cdn.cloudflare.steamstatic.com/steam/apps/252490/ss_58c5b4107fbd90f5a56b3adc97a6b61384ce4f12.116x65.jpg?t=1608404151"/>
</div>
<div class="highlight_strip_item highlight_strip_screenshot" id="thumb_screenshot_ss_803a18bcbf6004706f12a1f88bb3cadbd9ac5f5b.jpg">
<img src="https://cdn.cloudflare.steamstatic.com/steam/apps/252490/ss_803a18bcbf6004706f12a1f88bb3cadbd9ac5f5b.116x65.jpg?t=1608404151"/>
</div>
<div class="highlight_strip_item highlight_strip_screenshot" id="thumb_screenshot_ss_297da1914b2de9c380e8c77478d9774958f49a9c.jpg">
<img src="https://cdn.cloudflare.steamstatic.com/steam/apps/252490/ss_297da1914b2de9c380e8c77478d9774958f49a9c.116x65.jpg?t=1608404151"/>
</div>
<div class="highlight_strip_item highlight_strip_screenshot" id="thumb_screenshot_ss_651097c65458ae555b42c42dd9667d7174397bdf.jpg">
<img src="https://cdn.cloudflare.steamstatic.com/steam/apps/252490/ss_651097c65458ae555b42c42dd9667d7174397bdf.116x65.jpg?t=1608404151"/>
</div>
<div class="highlight_strip_item highlight_strip_screenshot" id="thumb_screenshot_ss_6b729c0a2a0db015a238154ce78feca76c890b55.jpg">
<img src="https://cdn.cloudflare.steamstatic.com/steam/apps/252490/ss_6b729c0a2a0db015a238154ce78feca76c890b55.116x65.jpg?t=1608404151"/>
</div>
<div class="highlight_strip_item highlight_strip_screenshot" id="thumb_screenshot_ss_326282c7485e8aff1ebf6750c82622afef098998.jpg">
<img src="https://cdn.cloudflare.steamstatic.com/steam/apps/252490/ss_326282c7485e8aff1ebf6750c82622afef098998.116x65.jpg?t=1608404151"/>
</div>
<div class="highlight_strip_item highlight_strip_screenshot" id="thumb_screenshot_ss_9264a17b6bc1b3f9df55cf2aafcc25c6188bba59.jpg">
<img src="https://cdn.cloudflare.steamstatic.com/steam/apps/252490/ss_9264a17b6bc1b3f9df55cf2aafcc25c6188bba59.116x65.jpg?t=1608404151"/>
</div>
<div class="highlight_strip_item highlight_strip_screenshot" id="thumb_screenshot_ss_54c335670b8beba01e7330263751bda74dcd72f1.jpg">
<img src="https://cdn.cloudflare.steamstatic.com/steam/apps/252490/ss_54c335670b8beba01e7330263751bda74dcd72f1.116x65.jpg?t=1608404151"/>
</div>
<div class="highlight_strip_item highlight_strip_screenshot" id="thumb_screenshot_ss_652294496bc3f4626dbcdfdd0ff60d5e7398c25e.jpg">
<img src="https://cdn.cloudflare.steamstatic.com/steam/apps/252490/ss_652294496bc3f4626dbcdfdd0ff60d5e7398c25e.116x65.jpg?t=1608404151"/>
</div>
<div class="highlight_strip_item highlight_strip_screenshot" id="thumb_screenshot_ss_4f2d0e89f55bcf236bb64c72736104c44aa50275.jpg">
<img src="https://cdn.cloudflare.steamstatic.com/steam/apps/252490/ss_4f2d0e89f55bcf236bb64c72736104c44aa50275.116x65.jpg?t=1608404151"/>
</div>
<div class="highlight_strip_item highlight_strip_screenshot" id="thumb_screenshot_ss_8880205af12b492f866479477b9a98e731f956d2.jpg">
<img src="https://cdn.cloudflare.steamstatic.com/steam/apps/252490/ss_8880205af12b492f866479477b9a98e731f956d2.116x65.jpg?t=1608404151"/>
</div>
<div class="highlight_strip_item highlight_strip_screenshot" id="thumb_screenshot_ss_f78385eb47e11f046f696e09d5bfa4d329017b1e.jpg">
<img src="https://cdn.cloudflare.steamstatic.com/steam/apps/252490/ss_f78385eb47e11f046f696e09d5bfa4d329017b1e.116x65.jpg?t=1608404151"/>
</div>
<div class="highlight_strip_item highlight_strip_screenshot" id="thumb_screenshot_ss_c21e99d11d22a035744cfb974ee03647c1e628c5.jpg">
<img src="https://cdn.cloudflare.steamstatic.com/steam/apps/252490/ss_c21e99d11d22a035744cfb974ee03647c1e628c5.116x65.jpg?t=1608404151"/>
</div>
<div class="highlight_strip_item highlight_strip_screenshot" id="thumb_screenshot_ss_4bd74e976bc5e2c519cd0011b7192a20126253b9.jpg">
<img src="https://cdn.cloudflare.steamstatic.com/steam/apps/252490/ss_4bd74e976bc5e2c519cd0011b7192a20126253b9.116x65.jpg?t=1608404151"/>
</div>
<div class="highlight_strip_item highlight_strip_screenshot" id="thumb_screenshot_ss_6c71cf2f4b13fdaed53f5b0de381a9c9227b9c78.jpg">
<img src="https://cdn.cloudflare.steamstatic.com/steam/apps/252490/ss_6c71cf2f4b13fdaed53f5b0de381a9c9227b9c78.116x65.jpg?t=1608404151"/>
</div>
<div class="highlight_strip_item highlight_strip_screenshot" id="thumb_screenshot_ss_234b12804c91c911e4095fcb872ef7f1a1371ca2.jpg">
<img src="https://cdn.cloudflare.steamstatic.com/steam/apps/252490/ss_234b12804c91c911e4095fcb872ef7f1a1371ca2.116x65.jpg?t=1608404151"/>
</div>
<div class="highlight_strip_item highlight_strip_screenshot" id="thumb_screenshot_ss_9b15e65273879b475a4d223fb4af181fbd8960ef.jpg">
<img src="https://cdn.cloudflare.steamstatic.com/steam/apps/252490/ss_9b15e65273879b475a4d223fb4af181fbd8960ef.116x65.jpg?t=1608404151"/>
</div>
</div>
</div>
<div class="slider_ctn">
<div class="slider_left" id="highlight_slider_left"><span></span></div>
<div class="slider" id="highlight_slider">
<div class="slider_bg">
</div>
<div class="handle">
</div>
</div>
<div class="slider_right" id="highlight_slider_right"><span></span></div>
</div>
<script type="text/javascript">
									$J( function() {
										var player = new HighlightPlayer( {
											elemPlayerArea: 'highlight_player_area',
											elemStrip: 'highlight_strip',
											elemStripScroll: 'highlight_strip_scroll',
											elemSlider: 'highlight_slider',
											rgScreenshotURLs: rgScreenshotURLs
										} );

										$J('#highlight_slider_right').click( function() {
											player.Transition( true );
										});
										$J('#highlight_slider_left').click( function() {
											player.TransitionBack( true );
										});

										if( window.location.hash )
										{
											var ssid = window.location.hash.substr(1);
											player.HighlightScreenshot(ssid);
										}
									} );
								</script>
</div>
</div>
</div>
<div style="clear: both;"></div>
</div>
</div>
<div class="queue_overflow_ctn">
<div class="queue_ctn">
<div class="queue_actions_ctn">
<p><a href="https://store.steampowered.com/login/?redir=app%2F252490&amp;snr=1_5_9_">Sign in</a> to add this item to your wishlist, follow it, or mark it as not interested</p>
</div>
</div>
</div>
</div>
<div class="page_content">
<!-- Right Column -->
<div class="rightcol game_meta_data">
<div id="responsive_apppage_details_left_ctn"></div>
<div id="responsive_apppage_details_right_ctn"></div>
<div style="clear: both;"></div>
<div class="block responsive_apppage_details_right heading">Is this game relevant to you?</div>
<div class="block responsive_apppage_details_right recommendation_noinfo">
<p>
									Sign in to see reasons why you may or may not like this based on your games, friends, and curators you follow.
								</p>
<br/>
<a class="btnv6_blue_hoverfade btn_medium" href="https://store.steampowered.com/login/?redir=app/252490"><span>Sign In</span></a>
									or									<a class="btnv6_blue_hoverfade btn_medium" href="steam://store/252490"><span>Open in Steam</span></a>
</div>
<div class="block responsive_apppage_details_left" id="category_block">
<div class="game_area_details_specs"><div class="icon"><a href="https://store.steampowered.com/search/?category2=20&amp;snr=1_5_9__423"><img class="category_icon" src="https://store.cloudflare.steamstatic.com/public/images/v6/ico/ico_multiPlayer.png"/></a></div><a class="name" href="https://store.steampowered.com/search/?category2=20&amp;snr=1_5_9__423">MMO</a></div><div class="game_area_details_specs"><div class="icon"><a href="https://store.steampowered.com/search/?category2=36&amp;snr=1_5_9__423"><img class="category_icon" src="https://store.cloudflare.steamstatic.com/public/images/v6/ico/ico_multiPlayer.png"/></a></div><a class="name" href="https://store.steampowered.com/search/?category2=36&amp;snr=1_5_9__423">Online PvP</a></div><div class="game_area_details_specs"><div class="icon"><a href="https://store.steampowered.com/search/?category2=38&amp;snr=1_5_9__423"><img class="category_icon" src="https://store.cloudflare.steamstatic.com/public/images/v6/ico/ico_coop.png"/></a></div><a class="name" href="https://store.steampowered.com/search/?category2=38&amp;snr=1_5_9__423">Online Co-op</a></div><div class="game_area_details_specs"><div class="icon"><a href="https://store.steampowered.com/search/?category2=27&amp;snr=1_5_9__423"><img class="category_icon" src="https://store.cloudflare.steamstatic.com/public/images/v6/ico/ico_multiPlayer.png"/></a></div><a class="name" href="https://store.steampowered.com/search/?category2=27&amp;snr=1_5_9__423">Cross-Platform Multiplayer</a></div><div class="game_area_details_specs"><div class="icon"><a href="https://store.steampowered.com/search/?category2=22&amp;snr=1_5_9__423"><img class="category_icon" src="https://store.cloudflare.steamstatic.com/public/images/v6/ico/ico_achievements.png"/></a></div><a class="name" href="https://store.steampowered.com/search/?category2=22&amp;snr=1_5_9__423">Steam Achievements</a></div><div class="game_area_details_specs"><div class="icon"><a href="https://store.steampowered.com/search/?category2=29&amp;snr=1_5_9__423"><img class="category_icon" src="https://store.cloudflare.steamstatic.com/public/images/v6/ico/ico_cards.png"/></a></div><a class="name" href="https://store.steampowered.com/search/?category2=29&amp;snr=1_5_9__423">Steam Trading Cards</a></div><div class="game_area_details_specs"><div class="icon"><a href="https://store.steampowered.com/search/?category2=30&amp;snr=1_5_9__423"><img class="category_icon" src="https://store.cloudflare.steamstatic.com/public/images/v6/ico/ico_workshop.png"/></a></div><a class="name" href="https://store.steampowered.com/search/?category2=30&amp;snr=1_5_9__423">Steam Workshop</a></div><div class="game_area_details_specs"><div class="icon"><a href="https://store.steampowered.com/search/?category2=35&amp;snr=1_5_9__423"><img class="category_icon" src="https://store.cloudflare.steamstatic.com/public/images/v6/ico/ico_cart.png"/></a></div><a class="name" href="https://store.steampowered.com/search/?category2=35&amp;snr=1_5_9__423">In-App Purchases</a></div><div class="game_area_details_specs"><div class="icon"><a href="https://store.steampowered.com/search/?category2=8&amp;snr=1_5_9__423"><img class="category_icon" src="https://store.cloudflare.steamstatic.com/public/images/v6/ico/ico_vac.png"/></a></div><a class="name" href="https://store.steampowered.com/search/?category2=8&amp;snr=1_5_9__423">Valve Anti-Cheat enabled</a></div><div class="game_area_details_specs"><div class="icon"><a href="https://store.steampowered.com/search/?category2=15&amp;snr=1_5_9__423"><img class="category_icon" src="https://store.cloudflare.steamstatic.com/public/images/v6/ico/ico_stats.png"/></a></div><a class="name" href="https://store.steampowered.com/search/?category2=15&amp;snr=1_5_9__423">Stats</a></div><div class="game_area_details_specs"><div class="icon"><a href="https://store.steampowered.com/search/?category2=42&amp;snr=1_5_9__423"><img class="category_icon" src="https://store.cloudflare.steamstatic.com/public/images/v6/ico/ico_remote_play.png"/></a></div><a class="name" href="https://store.steampowered.com/search/?category2=42&amp;snr=1_5_9__423">Remote Play on Tablet</a></div>
<div class="DRM_notice">
<div>Requires agreement to a 3rd-party EULA</div>
<div><a href="https://store.steampowered.com//eula/252490_eula_0" onclick="ShowEULA( this ); return false;">Rust EULA</a></div>
</div>
</div>
<div class="block responsive_apppage_details_right">
<div class="block_title">
								Languages:
							</div>
<table cellpadding="0" cellspacing="0" class="game_language_options">
<tr>
<th style="width: 94px;"></th>
<th class="checkcol">Interface</th>
<th class="checkcol">Full Audio</th>
<th class="checkcol">Subtitles</th>
</tr>
<tr class="" style="">
<td class="ellipsis" style="width: 94px; text-align: left">
				English			</td>
<td class="checkcol">
<span>✔</span> </td>
<td class="checkcol">
<span>✔</span> </td>
<td class="checkcol">
<span>✔</span> </td>
</tr>
<tr class="" style="">
<td class="ellipsis" style="width: 94px; text-align: left">
				French			</td>
<td class="checkcol">
<span>✔</span> </td>
<td class="checkcol">
<span>✔</span> </td>
<td class="checkcol">
<span>✔</span> </td>
</tr>
<tr class="" style="">
<td class="ellipsis" style="width: 94px; text-align: left">
				Italian			</td>
<td class="checkcol">
<span>✔</span> </td>
<td class="checkcol">
<span>✔</span> </td>
<td class="checkcol">
<span>✔</span> </td>
</tr>
<tr class="" style="">
<td class="ellipsis" style="width: 94px; text-align: left">
				German			</td>
<td class="checkcol">
<span>✔</span> </td>
<td class="checkcol">
<span>✔</span> </td>
<td class="checkcol">
<span>✔</span> </td>
</tr>
<tr class="" style="">
<td class="ellipsis" style="width: 94px; text-align: left">
				Spanish - Spain			</td>
<td class="checkcol">
<span>✔</span> </td>
<td class="checkcol">
<span>✔</span> </td>
<td class="checkcol">
<span>✔</span> </td>
</tr>
<tr class="" style="display: none;">
<td class="ellipsis" style="width: 94px; text-align: left">
				Japanese			</td>
<td class="checkcol">
<span>✔</span> </td>
<td class="checkcol">
<span>✔</span> </td>
<td class="checkcol">
<span>✔</span> </td>
</tr>
<tr class="" style="display: none;">
<td class="ellipsis" style="width: 94px; text-align: left">
				Korean			</td>
<td class="checkcol">
<span>✔</span> </td>
<td class="checkcol">
<span>✔</span> </td>
<td class="checkcol">
<span>✔</span> </td>
</tr>
<tr class="" style="display: none;">
<td class="ellipsis" style="width: 94px; text-align: left">
				Russian			</td>
<td class="checkcol">
<span>✔</span> </td>
<td class="checkcol">
<span>✔</span> </td>
<td class="checkcol">
<span>✔</span> </td>
</tr>
<tr class="" style="display: none;">
<td class="ellipsis" style="width: 94px; text-align: left">
				Simplified Chinese			</td>
<td class="checkcol">
<span>✔</span> </td>
<td class="checkcol">
<span>✔</span> </td>
<td class="checkcol">
<span>✔</span> </td>
</tr>
<tr class="" style="display: none;">
<td class="ellipsis" style="width: 94px; text-align: left">
				Ukrainian			</td>
<td class="checkcol">
<span>✔</span> </td>
<td class="checkcol">
<span>✔</span> </td>
<td class="checkcol">
<span>✔</span> </td>
</tr>
<tr class="" style="display: none;">
<td class="ellipsis" style="width: 94px; text-align: left">
				Polish			</td>
<td class="checkcol">
<span>✔</span> </td>
<td class="checkcol">
<span>✔</span> </td>
<td class="checkcol">
<span>✔</span> </td>
</tr>
<tr class="" style="display: none;">
<td class="ellipsis" style="width: 94px; text-align: left">
				Portuguese			</td>
<td class="checkcol">
<span>✔</span> </td>
<td class="checkcol">
<span>✔</span> </td>
<td class="checkcol">
<span>✔</span> </td>
</tr>
<tr class="" style="display: none;">
<td class="ellipsis" style="width: 94px; text-align: left">
				Turkish			</td>
<td class="checkcol">
<span>✔</span> </td>
<td class="checkcol">
<span>✔</span> </td>
<td class="checkcol">
<span>✔</span> </td>
</tr>
<tr class="" style="display: none;">
<td class="ellipsis" style="width: 94px; text-align: left">
				Arabic			</td>
<td class="checkcol">
<span>✔</span> </td>
<td class="checkcol">
</td>
<td class="checkcol">
</td>
</tr>
<tr class="" style="display: none;">
<td class="ellipsis" style="width: 94px; text-align: left">
				Czech			</td>
<td class="checkcol">
<span>✔</span> </td>
<td class="checkcol">
</td>
<td class="checkcol">
</td>
</tr>
<tr class="" style="display: none;">
<td class="ellipsis" style="width: 94px; text-align: left">
				Danish			</td>
<td class="checkcol">
<span>✔</span> </td>
<td class="checkcol">
</td>
<td class="checkcol">
</td>
</tr>
<tr class="" style="display: none;">
<td class="ellipsis" style="width: 94px; text-align: left">
				Dutch			</td>
<td class="checkcol">
<span>✔</span> </td>
<td class="checkcol">
</td>
<td class="checkcol">
</td>
</tr>
<tr class="" style="display: none;">
<td class="ellipsis" style="width: 94px; text-align: left">
				Finnish			</td>
<td class="checkcol">
<span>✔</span> </td>
<td class="checkcol">
</td>
<td class="checkcol">
</td>
</tr>
<tr class="" style="display: none;">
<td class="ellipsis" style="width: 94px; text-align: left">
				Greek			</td>
<td class="checkcol">
<span>✔</span> </td>
<td class="checkcol">
</td>
<td class="checkcol">
</td>
</tr>
<tr class="" style="display: none;">
<td class="ellipsis" style="width: 94px; text-align: left">
				Norwegian			</td>
<td class="checkcol">
<span>✔</span> </td>
<td class="checkcol">
</td>
<td class="checkcol">
</td>
</tr>
<tr class="" style="display: none;">
<td class="ellipsis" style="width: 94px; text-align: left">
				Portuguese - Brazil			</td>
<td class="checkcol">
<span>✔</span> </td>
<td class="checkcol">
</td>
<td class="checkcol">
</td>
</tr>
<tr class="" style="display: none;">
<td class="ellipsis" style="width: 94px; text-align: left">
				Spanish - Latin America			</td>
<td class="checkcol">
<span>✔</span> </td>
<td class="checkcol">
</td>
<td class="checkcol">
</td>
</tr>
<tr class="" style="display: none;">
<td class="ellipsis" style="width: 94px; text-align: left">
				Swedish			</td>
<td class="checkcol">
<span>✔</span> </td>
<td class="checkcol">
</td>
<td class="checkcol">
</td>
</tr>
<tr class="" style="display: none;">
<td class="ellipsis" style="width: 94px; text-align: left">
				Traditional Chinese			</td>
<td class="checkcol">
<span>✔</span> </td>
<td class="checkcol">
</td>
<td class="checkcol">
</td>
</tr>
<tr class="" style="display: none;">
<td class="ellipsis" style="width: 94px; text-align: left">
				Vietnamese			</td>
<td class="checkcol">
<span>✔</span> </td>
<td class="checkcol">
</td>
<td class="checkcol">
</td>
</tr>
</table>
<a class="all_languages" onclick="$J('table.game_language_options tr').show(); $J(this).hide(); return false">See all 25 supported languages</a>
</div>
<div class="block responsive_apppage_details_right" id="achievement_block">
<div class="block_title">
								Includes 65 Steam Achievements							</div>
<div class="communitylink_achievement_images">
<div class="communitylink_achievement">
<img class="communitylink_achievement" src="https://cdn.cloudflare.steamstatic.com/steamcommunity/public/images/apps/252490/d02b8e1965d9d46c94406740bf87b50ff309f476.jpg" title="Craft Stone Pickaxe"/>
</div>
<div class="communitylink_achievement">
<img class="communitylink_achievement" src="https://cdn.cloudflare.steamstatic.com/steamcommunity/public/images/apps/252490/b989a707829fcf4b69fba6f1d2b89f6e8a752039.jpg" title="Collect 300 Metal Ore"/>
</div>
<div class="communitylink_achievement">
<img class="communitylink_achievement" src="https://cdn.cloudflare.steamstatic.com/steamcommunity/public/images/apps/252490/0f5ed511d50436bf40c7f32f37db038a53463394.jpg" title="Research an Item"/>
</div>
<a class="communitylink_achievement communitylink_achivement_plusmore" href="https://steamcommunity.com/stats/252490/achievements">
										View<br/>all 65									</a>
<div style="clear: left;"></div>
</div>
</div>
<div class="block responsive_apppage_details_right" id="achievement_block">
<div class="block_title">
								Points Shop Items Available							</div>
<div class="communitylink_points_shop_images">
<div class="communitylink_points_shop_item">
<a href="https://store.steampowered.com/points/shop/app/252490/reward/48126/"><img class="profile_background" src="https://steamcommunity.com/economy/profilebackground/items/252490/899c08520175dac6140eb2c8c4e107751f035c47.jpg?size=64x0" title="I love my rock"/></a>
</div>
<div class="communitylink_points_shop_item">
<a href="https://store.steampowered.com/points/shop/app/252490/reward/47868/"><img class="profile_background" src="https://steamcommunity.com/economy/profilebackground/items/252490/5db417664de705da067cc03f1aa706a787811507.jpg?size=64x0" title="Rust Camp Fire"/></a>
</div>
<div class="communitylink_points_shop_item">
<a href="https://store.steampowered.com/points/shop/app/252490/reward/47755/"><img class="" src="https://cdn.cloudflare.steamstatic.com/steamcommunity/public/images/items/252490/985910e45c50ffccf1555b3b00ffabe0fdda82a4.png" title=":rust:"/></a>
</div>
<a class="communitylink_achievement communitylink_achivement_plusmore" href="https://store.steampowered.com/points/shop/app/252490/">
										View<br/>all 12									</a>
<div style="clear: left;"></div>
</div>
</div>
<div class="block responsive_apppage_details_left game_details underlined_links">
<div class="block_content">
<div class="block_content_inner">
<div class="details_block">
<b>Title:</b> Rust<br/>
<b>Genre:</b> <a href="https://store.steampowered.com/genre/Action/?snr=1_5_9__408">Action</a>, <a href="https://store.steampowered.com/genre/Adventure/?snr=1_5_9__408">Adventure</a>, <a href="https://store.steampowered.com/genre/Indie/?snr=1_5_9__408">Indie</a>, <a href="https://store.steampowered.com/genre/Massively%20Multiplayer/?snr=1_5_9__408">Massively Multiplayer</a>, <a href="https://store.steampowered.com/genre/RPG/?snr=1_5_9__408">RPG</a><br/>
<div class="dev_row">
<b>Developer:</b>
<a href="https://store.steampowered.com/developer/facepunch?snr=1_5_9__408">Facepunch Studios</a>
</div>
<div class="dev_row">
<b>Publisher:</b>
<a href="https://store.steampowered.com/publisher/facepunch?snr=1_5_9__408">Facepunch Studios</a>
</div>
<b>Release Date:</b> Feb 8, 2018<br/>
</div>
<div class="details_block">
<br/>
<a class="linkbar" href="https://steamcommunity.com/linkfilter/?url=http://rust.facepunch.com/" rel="noreferrer noopener" target="_blank">
			Visit the website <img align="bottom" border="0" src="https://store.cloudflare.steamstatic.com/public/images/v5/ico_external_link.gif"/>
</a>
<a class="linkbar" href="https://store.steampowered.com/newshub/?appids=252490&amp;snr=1_5_9__408" rel="noreferrer" target="_blank">
			View update history		</a>
<a class="linkbar" href="https://store.steampowered.com/newshub/app/252490?snr=1_5_9__408" rel="noreferrer" target="_blank">
			Read related news		</a>
<a class="linkbar" href="https://steamcommunity.com/app/252490/discussions/" rel="noreferrer" target="_blank">
			View discussions		</a>
<a class="linkbar" href="https://steamcommunity.com/app/252490/workshop/" rel="noreferrer" target="_blank">
            Visit the Workshop        </a>
<a class="linkbar" href="https://steamcommunity.com/actions/Search?T=ClanAccount&amp;K=Rust">
            Find Community Groups        </a>
</div>
</div>
</div>
</div>
<div class="block responsive_apppage_details_left">
<a class="btnv6_blue_hoverfade btn_medium" href="#" onclick="ShowShareDialog(); return false;"><span>Share</span></a>
<a class="btnv6_blue_hoverfade btn_medium" href="#" onclick="ShowEmbedWidget(252490); return false;"><span>Embed</span></a>
<a class="btnv6_blue_hoverfade btn_medium" href="javascript:void(0)" id="ReportAppBtn" onclick="ShowReportDialog(252490)"><span data-tooltip-text="Report this Product"><i class="ico16 reportv6"></i> </span></a>
</div>
<div class="block responsive_apppage_reviewblock">
<div id="game_area_metascore">
<div class="score medium">
										69									</div>
<div class="logo"></div>
<div class="wordmark">
<div class="metacritic">metacritic</div>
<div id="game_area_metalink"><a href="https://www.metacritic.com/game/pc/rust?ftag=MCD-06-10aaa1f" target="_blank">Read Critic Reviews</a> <img align="bottom" border="0" src="https://store.cloudflare.steamstatic.com/public/images/ico/iconExternalLink.gif"/></div>
</div>
</div>
<div style="clear: both"></div>
</div>
</div>
<!-- End Right Column -->
<div class="leftcol game_description_column">
<div id="game_area_purchase">
<!--[if lte IE 7]>
<style type="text/css">
.game_area_purchase_game_dropdown_right_panel .btn_addtocart { float: none; }
</style>
<![endif]-->
<div class="game_area_purchase_game_wrapper">
<div class="game_area_purchase_game">
<form action="https://store.steampowered.com/cart/" method="POST" name="add_to_cart_244390">
<input name="snr" type="hidden" value="1_5_9__403"/>
<input name="originating_snr" type="hidden" value="1_direct-navigation__"/>
<input name="action" type="hidden" value="add_to_cart"/>
<input name="sessionid" type="hidden" value="97752a7f6ec9d5fec99adf7e"/>
<input name="subid" type="hidden" value="244390"/>
</form>
<div class="game_area_purchase_platform"><span class="platform_img win"></span><span class="platform_img mac"></span></div>
<h1>Buy Rust</h1>
<div class="game_purchase_action">
<div class="game_purchase_action_bg">
<div class="game_purchase_price price" data-price-final="3999">
							$39.99						</div>
<div class="btn_addtocart">
<a class="btn_green_steamui btn_medium" href="javascript:addToCart(244390);" id="btn_add_to_cart_244390">
<span>Add to Cart</span>
</a>
</div>
</div>
</div>
</div>
</div>
<div class="game_area_purchase_game_wrapper dynamic_bundle_description ds_no_flags" data-ds-bundle-data='{"m_nDiscountPct":"10","m_bMustPurchaseAsSet":0,"m_rgItems":[{"m_nPackageID":244390,"m_rgIncludedAppIDs":[252490],"m_bPackageDiscounted":false,"m_nBasePriceInCents":3999,"m_nFinalPriceInCents":3999,"m_nFinalPriceWithBundleDiscount":3599},{"m_nPackageID":402208,"m_rgIncludedAppIDs":[1174370],"m_bPackageDiscounted":false,"m_nBasePriceInCents":999,"m_nFinalPriceInCents":999,"m_nFinalPriceWithBundleDiscount":899},{"m_nPackageID":474021,"m_rgIncludedAppIDs":[1353060],"m_bPackageDiscounted":false,"m_nBasePriceInCents":999,"m_nFinalPriceInCents":999,"m_nFinalPriceWithBundleDiscount":899}],"m_bIsCommercial":false,"m_bRestrictGifting":true}' data-ds-bundleid="12976" data-ds-crtrids="[2081]" data-ds-descids="[1,2,5]" data-ds-itemkey="Bundle_12976" data-ds-tagids="[1662,492,19,128,21,122,1702]">
<div class="game_area_purchase_game_dropdown_subscription game_area_purchase_game">
<form action="https://store.steampowered.com/cart/" method="POST" name="add_bundle_to_cart_12976">
<input name="snr" type="hidden" value="1_5_9__403"/>
<input name="action" type="hidden" value="add_to_cart"/>
<input name="sessionid" type="hidden" value="97752a7f6ec9d5fec99adf7e"/>
<input name="bundleid" type="hidden" value="12976"/>
</form>
<div class="game_area_purchase_platform"><span class="platform_img win"></span><span class="platform_img mac"></span></div>
<h1>
			Buy Rust + DLC Bundle							<span class="bundle_label" data-tooltip-text="Bundles are a special discount on a set of products.  If you already own some of the products contained in the bundle, purchasing the bundle will allow you to &quot;complete the set&quot;, paying only for the products you don't already own while still receiving the full bundle discount on each of those products.">
					BUNDLE					<span class="bundle_label_tooltip">(?)</span>
</span>
</h1>
<p class="package_contents">
<b>Includes 3 items:</b>
<a href="https://store.steampowered.com/app/252490/Rust/">Rust</a>, <a href="https://store.steampowered.com/app/1174370/Rust__Instruments_Pack/">Rust Instrument Pack</a>, <a href="https://store.steampowered.com/app/1353060/Rust__Sunburn_Pack/">Rust Sunburn Pack</a> </p>
<div class="game_purchase_action">
<div class="game_purchase_action_bg">
<div class="btn_addtocart btn_packageinfo">
<a class="btn_blue_steamui btn_medium" href="https://store.steampowered.com/bundle/12976/Rust__DLC_Bundle/?snr=1_5_9__403">
<span>Bundle info</span>
</a>
</div>
</div>
<div class="game_purchase_action_bg">
<div class="discount_block game_purchase_discount no_discount" data-price-final="5397"><div class="bundle_base_discount">-10%</div><div class="discount_prices"><div class="discount_final_price">$53.97</div></div></div>
<div class="btn_addtocart">
<a class="btn_green_steamui btn_medium" href="javascript:addBundleToCart( 12976);">
<span>Add to Cart</span>
</a>
</div>
<div class="btn_addtocart btn_packageinfo btn_addtoaccount" data-tooltip-text="This game is available for free to your account.  Click here to add this game to your account." style="display: none">
<span class="btn_blue_steamui btn_medium" onclick='AddFreeBundle( 12976, "Rust + DLC Bundle" );'>
<span>Add to Account</span>
</span>
</div>
</div>
</div>
</div>
</div><div class="game_area_purchase_game_wrapper dynamic_bundle_description ds_no_flags" data-ds-bundle-data='{"m_nDiscountPct":"10","m_bMustPurchaseAsSet":0,"m_rgItems":[{"m_nPackageID":218,"m_rgIncludedAppIDs":[4000],"m_bPackageDiscounted":false,"m_nBasePriceInCents":999,"m_nFinalPriceInCents":999,"m_nFinalPriceWithBundleDiscount":899},{"m_nPackageID":158488,"m_rgIncludedAppIDs":[602700],"m_bPackageDiscounted":false,"m_nBasePriceInCents":1499,"m_nFinalPriceInCents":1499,"m_nFinalPriceWithBundleDiscount":1349},{"m_nPackageID":158509,"m_rgIncludedAppIDs":[602770],"m_bPackageDiscounted":false,"m_nBasePriceInCents":999,"m_nFinalPriceInCents":999,"m_nFinalPriceWithBundleDiscount":899},{"m_nPackageID":244390,"m_rgIncludedAppIDs":[252490],"m_bPackageDiscounted":false,"m_nBasePriceInCents":3999,"m_nFinalPriceInCents":3999,"m_nFinalPriceWithBundleDiscount":3599},{"m_nPackageID":474021,"m_rgIncludedAppIDs":[1353060],"m_bPackageDiscounted":false,"m_nBasePriceInCents":999,"m_nFinalPriceInCents":999,"m_nFinalPriceWithBundleDiscount":899},{"m_nPackageID":402208,"m_rgIncludedAppIDs":[1174370],"m_bPackageDiscounted":false,"m_nBasePriceInCents":999,"m_nFinalPriceInCents":999,"m_nFinalPriceWithBundleDiscount":899}],"m_bIsCommercial":false,"m_bRestrictGifting":true}' data-ds-bundleid="12958" data-ds-crtrids="[2081]" data-ds-descids="[1,2,5]" data-ds-itemkey="Bundle_12958" data-ds-tagids="[492,3859,1662,19,128,122,21]">
<div class="game_area_purchase_game_dropdown_subscription game_area_purchase_game">
<form action="https://store.steampowered.com/cart/" method="POST" name="add_bundle_to_cart_12958">
<input name="snr" type="hidden" value="1_5_9__403"/>
<input name="action" type="hidden" value="add_to_cart"/>
<input name="sessionid" type="hidden" value="97752a7f6ec9d5fec99adf7e"/>
<input name="bundleid" type="hidden" value="12958"/>
</form>
<div class="game_area_purchase_platform"><span class="platform_img win"></span></div>
<h1>
			Buy Facepunch Complete Bundle							<span class="bundle_label" data-tooltip-text="Bundles are a special discount on a set of products.  If you already own some of the products contained in the bundle, purchasing the bundle will allow you to &quot;complete the set&quot;, paying only for the products you don't already own while still receiving the full bundle discount on each of those products.">
					BUNDLE					<span class="bundle_label_tooltip">(?)</span>
</span>
</h1>
<p class="package_contents">
<b>Includes 6 items:</b>
<a href="https://store.steampowered.com/app/4000/Garrys_Mod/">Garry's Mod</a>, <a href="https://store.steampowered.com/app/602700/Chippy/">Chippy</a>, <a href="https://store.steampowered.com/app/602770/Clatter/">Clatter</a>, <a href="https://store.steampowered.com/app/252490/Rust/">Rust</a>, <a href="https://store.steampowered.com/app/1353060/Rust__Sunburn_Pack/">Rust Sunburn Pack</a>, <a href="https://store.steampowered.com/app/1174370/Rust__Instruments_Pack/">Rust Instrument Pack</a> </p>
<div class="game_purchase_action">
<div class="game_purchase_action_bg">
<div class="btn_addtocart btn_packageinfo">
<a class="btn_blue_steamui btn_medium" href="https://store.steampowered.com/bundle/12958/Facepunch_Complete_Bundle/?snr=1_5_9__403">
<span>Bundle info</span>
</a>
</div>
</div>
<div class="game_purchase_action_bg">
<div class="discount_block game_purchase_discount no_discount" data-price-final="8544"><div class="bundle_base_discount">-10%</div><div class="discount_prices"><div class="discount_final_price">$85.44</div></div></div>
<div class="btn_addtocart">
<a class="btn_green_steamui btn_medium" href="javascript:addBundleToCart( 12958);">
<span>Add to Cart</span>
</a>
</div>
<div class="btn_addtocart btn_packageinfo btn_addtoaccount" data-tooltip-text="This game is available for free to your account.  Click here to add this game to your account." style="display: none">
<span class="btn_blue_steamui btn_medium" onclick='AddFreeBundle( 12958, "Facepunch Complete Bundle" );'>
<span>Add to Account</span>
</span>
</div>
</div>
</div>
</div>
</div> <div class="game_area_dlc_section">
<h2 class="gradientbg">Content For This Game<span class="note"><a href="https://store.steampowered.com/dlc/252490/Rust/?snr=1_5_9__1061">Browse all <em>(2)</em></a></span></h2>
<div class="game_area_dlc_list">
<form action="https://store.steampowered.com/cart/?snr=1_5_9_" method="POST" name="add_all_dlc_to_cart">
<input name="action" type="hidden" value="add_to_cart"/>
<input name="sessionid" type="hidden" value="97752a7f6ec9d5fec99adf7e"/>
<div class="tableView">
<div class="gameDlcBlocks">
<a class="game_area_dlc_row odd ds_collapse_flag ds_collapse_flag_tiny" data-ds-appid="1174370" data-ds-crtrids="[2081]" data-ds-itemkey="App_1174370" data-ds-tagids="[492,128,19,21,122,1662,1621]" href="https://store.steampowered.com/app/1174370/Rust__Instruments_Pack/?snr=1_5_9__405" id="dlc_row_1174370" onmouseout="HideGameHover( this, event, 'global_hover' )" onmouseover="GameHover( this, event, 'global_hover', {&quot;type&quot;:&quot;app&quot;,&quot;id&quot;:1174370,&quot;public&quot;:1,&quot;v6&quot;:1} );">
<div class="game_area_dlc_price">
																																		$9.99																														</div>
<div class="game_area_dlc_name">
							Rust - Instruments Pack						</div>
<input name="subid[]" type="hidden" value="402208"/>
</a> <a class="game_area_dlc_row even ds_collapse_flag ds_collapse_flag_tiny" data-ds-appid="1353060" data-ds-itemkey="App_1353060" data-ds-tagids="[19,122,492,128,21,1662,1702]" href="https://store.steampowered.com/app/1353060/Rust__Sunburn_Pack/?snr=1_5_9__405" id="dlc_row_1353060" onmouseout="HideGameHover( this, event, 'global_hover' )" onmouseover="GameHover( this, event, 'global_hover', {&quot;type&quot;:&quot;app&quot;,&quot;id&quot;:1353060,&quot;public&quot;:1,&quot;v6&quot;:1} );">
<div class="game_area_dlc_price">
																																		$9.99																														</div>
<div class="game_area_dlc_name">
							Rust - Sunburn Pack						</div>
<input name="subid[]" type="hidden" value="474021"/>
</a>
<div class="game_purchase_action game_purchase_action_bg" id="dlc_purchase_action" style="">
<div class="game_purchase_price price">
													$19.98												</div>
<div class="btn_addtocart">
<a class="btn_green_steamui btn_medium" href="javascript:addAllDlcToCart();">
<span>Add all DLC to Cart</span>
</a>
</div>
<div style="clear: both;"></div>
</div>
</div>
</div> <!-- tableView -->
<div style="clear: right;"></div>
</form>
</div>
</div> <!-- game_area_dlc_section -->
</div>
<!-- game_area_purchase -->
<div class="item_store_items_block block responsive_apppage_reviewblock">
<div class="block_header">
<h2>Items available for this game</h2>
</div>
<div class="item_store_items_game_page_container">
<div class="item_def_grid_item">
<div class="item_def_icon_container">
<img class="item_def_icon" src="https://community.cloudflare.steamstatic.com/economy/image/6TMcQ7eX6E0EZl2byXi7vaVKyDk_zQLX05x6eLCFM9neAckxGDf7qU2e2gu64OnAeQ7835df5GLCfDY0jhyo8DEiv5dRPqo9q7c3Rf83n37_ZQ/256fx256f" srcset="https://community.cloudflare.steamstatic.com/economy/image/6TMcQ7eX6E0EZl2byXi7vaVKyDk_zQLX05x6eLCFM9neAckxGDf7qU2e2gu64OnAeQ7835df5GLCfDY0jhyo8DEiv5dRPqo9q7c3Rf83n37_ZQ/256fx256f 1x, https://community.cloudflare.steamstatic.com/economy/image/6TMcQ7eX6E0EZl2byXi7vaVKyDk_zQLX05x6eLCFM9neAckxGDf7qU2e2gu64OnAeQ7835df5GLCfDY0jhyo8DEiv5dRPqo9q7c3Rf83n37_ZQ/256fx256fdpx2x 2x"/>
</div>
<div>
<div class="item_def_price">$0.99</div>
<div style="clear: right"></div>
</div>
</div><div class="item_def_grid_item">
<div class="item_def_icon_container">
<img class="item_def_icon" src="https://community.cloudflare.steamstatic.com/economy/image/6TMcQ7eX6E0EZl2byXi7vaVKyDk_zQLX05x6eLCFM9neAckxGDf7qU2e2gu64OnAeQ7835df5GLHfDY0jhyo8DEiv5dQPqw6rbM0RfjWuqf02Q/256fx256f" srcset="https://community.cloudflare.steamstatic.com/economy/image/6TMcQ7eX6E0EZl2byXi7vaVKyDk_zQLX05x6eLCFM9neAckxGDf7qU2e2gu64OnAeQ7835df5GLHfDY0jhyo8DEiv5dQPqw6rbM0RfjWuqf02Q/256fx256f 1x, https://community.cloudflare.steamstatic.com/economy/image/6TMcQ7eX6E0EZl2byXi7vaVKyDk_zQLX05x6eLCFM9neAckxGDf7qU2e2gu64OnAeQ7835df5GLHfDY0jhyo8DEiv5dQPqw6rbM0RfjWuqf02Q/256fx256fdpx2x 2x"/>
</div>
<div>
<div class="item_def_price">$2.99</div>
<div style="clear: right"></div>
</div>
</div><div class="item_def_grid_item">
<div class="item_def_icon_container">
<img class="item_def_icon" src="https://community.cloudflare.steamstatic.com/economy/image/6TMcQ7eX6E0EZl2byXi7vaVKyDk_zQLX05x6eLCFM9neAckxGDf7qU2e2gu64OnAeQ7835df5GLNfDY0jhyo8DEiv5daPKE6pLw1QPi5XuozKbM/256fx256f" srcset="https://community.cloudflare.steamstatic.com/economy/image/6TMcQ7eX6E0EZl2byXi7vaVKyDk_zQLX05x6eLCFM9neAckxGDf7qU2e2gu64OnAeQ7835df5GLNfDY0jhyo8DEiv5daPKE6pLw1QPi5XuozKbM/256fx256f 1x, https://community.cloudflare.steamstatic.com/economy/image/6TMcQ7eX6E0EZl2byXi7vaVKyDk_zQLX05x6eLCFM9neAckxGDf7qU2e2gu64OnAeQ7835df5GLNfDY0jhyo8DEiv5daPKE6pLw1QPi5XuozKbM/256fx256fdpx2x 2x"/>
</div>
<div>
<div class="item_def_price">$2.49</div>
<div style="clear: right"></div>
</div>
</div><div class="item_def_grid_item">
<div class="item_def_icon_container">
<img class="item_def_icon" src="https://community.cloudflare.steamstatic.com/economy/image/6TMcQ7eX6E0EZl2byXi7vaVKyDk_zQLX05x6eLCFM9neAckxGDf7qU2e2gu64OnAeQ7835df5GLDfDY0jhyo8DEiv5dcPq4_q7Q2Rv_xfkR0rw/256fx256f" srcset="https://community.cloudflare.steamstatic.com/economy/image/6TMcQ7eX6E0EZl2byXi7vaVKyDk_zQLX05x6eLCFM9neAckxGDf7qU2e2gu64OnAeQ7835df5GLDfDY0jhyo8DEiv5dcPq4_q7Q2Rv_xfkR0rw/256fx256f 1x, https://community.cloudflare.steamstatic.com/economy/image/6TMcQ7eX6E0EZl2byXi7vaVKyDk_zQLX05x6eLCFM9neAckxGDf7qU2e2gu64OnAeQ7835df5GLDfDY0jhyo8DEiv5dcPq4_q7Q2Rv_xfkR0rw/256fx256fdpx2x 2x"/>
</div>
<div>
<div class="item_def_price">$0.99</div>
<div style="clear: right"></div>
</div>
</div><div class="item_def_grid_item">
<div class="item_def_icon_container">
<img class="item_def_icon" src="https://community.cloudflare.steamstatic.com/economy/image/6TMcQ7eX6E0EZl2byXi7vaVKyDk_zQLX05x6eLCFM9neAckxGDf7qU2e2gu64OnAeQ7835df5GLAfDY0jhyo8DEiv5dbPag4qrAyQvm7RpipcLY/256fx256f" srcset="https://community.cloudflare.steamstatic.com/economy/image/6TMcQ7eX6E0EZl2byXi7vaVKyDk_zQLX05x6eLCFM9neAckxGDf7qU2e2gu64OnAeQ7835df5GLAfDY0jhyo8DEiv5dbPag4qrAyQvm7RpipcLY/256fx256f 1x, https://community.cloudflare.steamstatic.com/economy/image/6TMcQ7eX6E0EZl2byXi7vaVKyDk_zQLX05x6eLCFM9neAckxGDf7qU2e2gu64OnAeQ7835df5GLAfDY0jhyo8DEiv5dbPag4qrAyQvm7RpipcLY/256fx256fdpx2x 2x"/>
</div>
<div>
<div class="item_def_price">$0.99</div>
<div style="clear: right"></div>
</div>
</div> <div class="item_store_overlay_link">
<a class="" href="https://store.steampowered.com/itemstore/252490/">
<span class="btnv6_lightblue_blue btn_medium">
<span>Shop available items</span>
</span>
</a>
</div>
</div>
</div>
<div class="purchase_area_spacer"> </div>
<script type="text/javascript">
						var StoreDefaults = {"PartnerEventStore":[{"gid":"2956017123849366368","clan_steamid":"103582791434898478","event_name":"January Update","event_type":13,"appid":252490,"server_address":"","server_password":"","rtime32_start_time":1610046000,"rtime32_end_time":1610051401,"comment_count":0,"creator_steamid":"76561198002789398","last_update_steamid":"76561198002789398","event_notes":"see announcement body","jsondata":"{\"localized_subtitle\":[null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null],\"localized_summary\":[\"Santa is packing up and clearing out the bodies, we hope you enjoyed the Holiday Season.\",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null],\"localized_title_image\":[\"5508f7ce451551ca7592a95b75161ffce846747e.png\",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null],\"localized_capsule_image\":[\"80d2f4ed7aa101fc75ab082222b2de4b8fd38cac.png\",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null],\"localized_spotlight_image\":[null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null],\"bSaleEnabled\":false,\"sale_show_creator\":false,\"sale_sections\":[],\"sale_browsemore_text\":\"\",\"sale_browsemore_url\":\"\",\"sale_browsemore_color\":\"\",\"sale_browsemore_bgcolor\":\"\",\"localized_sale_header\":[null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null],\"localized_sale_overlay\":[null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null],\"localized_sale_product_banner\":[null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null],\"localized_sale_product_mobile_banner\":[null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null],\"sale_font\":\"\",\"sale_background_color\":\"\",\"sale_header_offset\":150,\"referenced_appids\":[],\"bBroadcastEnabled\":false,\"broadcastChatSetting\":\"hide\",\"default_broadcast_title\":\"#Broadcast_default_title_dev\",\"localized_broadcast_title\":[null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null],\"localized_broadcast_left_image\":[null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null],\"localized_broadcast_right_image\":[null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null],\"broadcast_whitelist\":[],\"bScheduleEnabled\":false,\"scheduleEntries\":[]}","announcement_body":{"gid":"2956017123849366369","clanid":"5377070","posterid":"76561198002789398","headline":"January Update","posttime":1610046054,"updatetime":1610046054,"body":"Santa is packing up and clearing out the bodies, we hope you enjoyed the Holiday Season. We're getting back to work after a couple of weeks off which is why this is a light blog and we are looking forward to the journey ahead in 2021!\n\nWe're happy to announce Twitch Drops are now enabled for all Rust Twitch streamers. You can earn special and unique skins simply by watching your favourite Rust Twitch streamers.\n\nAdditionally, we've teamed up with Auronplay, Jacksepticeye, lilypichu, ludwig, Myth, pokimane, shroud, Sykkuno and xQc to bring you special unique drops which can only be earned by watching their channels - Learn more by clicking the [url=https:\/\/twitch.facepunch.com\/]Link[\/url]\n\nChangelist\n\n[list]\n[*]  Fixed some clothing casting incorrect shadows\n[*]  Fixed respawn icons not properly merging when creating a combined respawn icon\n[*]  Fixed push to talk setting not being respected when talking on a phone (if this is enabled you need to hold your push to talk key to speak into a Telephone)\n[*]  Fixed some non English characters in player names causing display issues in the inventory\n[*]  Fixed being able to slide open the windows of a locked armoured cockpit module that's directly in front of a taxi module that a player is riding in\n[*]  Sleeping bags that are too close to another sleeping bag will now be tinted orange while placing (also affects Beds and Beach Towels)\n[*]  Fixed some incorrect sound effects on the Telephone\n[*]  Voice audio transmitted through Telephones now has some audio filters applied\n[*]  Car lock info tooltips wait a while before showing up again\n[*]  SAM sites no longer target hot air balloons that aren't inflated\n[*]  Reduced research cost of T2 engine parts\n[*]  Reduced weather event chances - more clear skies\n[*]  Allow players to boost voices from the options menu rather than needing to use the console\n[*]  Disabled Xmas event and craftable item\n[\/list]\n\n","commentcount":229,"tags":["mod_reviewed","ModAct_383594390_1610048362_0"],"language":0,"hidden":0,"forum_topic_id":"3007808519561161114","event_gid":"2956017123849366368","voteupcount":3796,"votedowncount":150},"published":1,"hidden":0,"rtime32_visibility_start":0,"rtime32_visibility_end":0,"broadcaster_accountid":0,"follower_count":4,"ignore_count":0,"forum_topic_id":"3007808519561161114","rtime32_last_modified":1610481961,"news_post_gid":"0","rtime_mod_reviewed":1610048361,"featured_app_tagid":0,"referenced_appids":[],"votes_up":3796,"votes_down":150,"comment_type":"ForumTopic","gidfeature":"1635292137552441086","gidfeature2":"3007808519561161114"},{"gid":"4138210213525206574","clan_steamid":"103582791434898478","event_name":"Season's Beatings","event_type":35,"appid":252490,"server_address":"","server_password":"","rtime32_start_time":1608231660,"rtime32_end_time":1608237001,"comment_count":0,"creator_steamid":"76561198002789398","last_update_steamid":"76561198002789398","event_notes":"see announcement body","jsondata":"{\"localized_subtitle\":[null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null],\"localized_summary\":[\"The most wonderful time of the year!\",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null],\"localized_title_image\":[\"00b5a62ba95e5acf70b8f00b1c26d7455225afab.png\",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null],\"localized_capsule_image\":[\"63236b70c877e9db9982818638965384317b9c16.png\",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null],\"localized_spotlight_image\":[null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null],\"bSaleEnabled\":false,\"sale_show_creator\":false,\"sale_sections\":[],\"sale_browsemore_text\":\"\",\"sale_browsemore_url\":\"\",\"sale_browsemore_color\":\"\",\"sale_browsemore_bgcolor\":\"\",\"localized_sale_header\":[null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null],\"localized_sale_overlay\":[null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null],\"localized_sale_product_banner\":[null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null],\"localized_sale_product_mobile_banner\":[null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null],\"sale_font\":\"\",\"sale_background_color\":\"\",\"sale_header_offset\":150,\"referenced_appids\":[],\"bBroadcastEnabled\":false,\"broadcastChatSetting\":\"hide\",\"default_broadcast_title\":\"#Broadcast_default_title_dev\",\"localized_broadcast_title\":[null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null],\"localized_broadcast_left_image\":[null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null],\"localized_broadcast_right_image\":[null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null],\"broadcast_whitelist\":[],\"bScheduleEnabled\":false,\"scheduleEntries\":[]}","announcement_body":{"gid":"4138210213525206575","clanid":"5377070","posterid":"76561198002789398","headline":"Season's Beatings","posttime":1608231680,"updatetime":1608231680,"body":"From everyone at Facepunch, we'd like to wish you all a Merry Christmas and Happy Holidays! The Christmas Event is once again live! If you haven't been around for this before, here's what you can expect:\n\nEvery once in a while you will hear the sound of jingle bells. Run outside and look for a gift! Two gifts are spawned per player, in a radius of about 40m from where you are standing. Run up and bash it open to receive your Christmas presents. They come in three sizes: small, medium, and large. If you have enough small presents stashed, you can \"trade up\" to a medium or large. The contents of each present vary, but you'll find a mix of resources, weapons, and candy. We've also added wrapping paper allowing you to wrap up items as gifts to other players, perhaps sold in your vending machine...\n\nOnce again, you will be able to find Santa hats and reindeer antlers, both of which can be worn and provide a decent amount of protection. There\u2019s also a lickable candy cane club, and two types of stockings. If you hang a stocking inside your base when the jingle bells ring the stocking will fill up with loot. The larger stocking has a higher chance for better items and both last around 5-10 refills.\n\nMore details on the new items can be found on the [url=https:\/\/rust.facepunch.com\/blog\/christmas-2020]link[\/url]\n\n[previewyoutube=Y0ZwJNCkXx8;full][\/previewyoutube]","commentcount":166,"tags":["mod_reviewed","ModAct_444533432_1608232978_0"],"language":0,"hidden":0,"forum_topic_id":"5575984402924129387","event_gid":"4138210213525206574","voteupcount":4071,"votedowncount":81},"published":1,"hidden":0,"rtime32_visibility_start":0,"rtime32_visibility_end":0,"broadcaster_accountid":0,"follower_count":0,"ignore_count":0,"forum_topic_id":"5575984402924129387","rtime32_last_modified":1610481588,"news_post_gid":"0","rtime_mod_reviewed":1608232978,"featured_app_tagid":0,"referenced_appids":[],"votes_up":4071,"votes_down":81,"comment_type":"ForumTopic","gidfeature":"1635292137552441086","gidfeature2":"5575984402924129387"}],"EventWebRowEmbed":{"bPreLoaded":true,"announcementGIDList":["2956017123849366369","4138210213525206575"]}};
					</script>
<div data-featuretarget="events-row"></div>
<div class="game_area_description" id="game_area_reviews">
<h2>Reviews</h2>
<p>“Rust is one of the cruelest games on Steam, and that's what makes it so compelling.”<br/><a href="https://www.pcgamer.com/uk/rust-review/" rel="noreferrer" target="_blank">PC Gamer</a><br/><br/>“Usually, people will just kill you on sight, but not always.”<br/><a href="https://www.rockpapershotgun.com/2018/02/12/rust-review/" rel="noreferrer" target="_blank">Rock Paper Shotgun</a><br/></p>
</div>
<div class="game_page_autocollapse" style="max-height: 300px;">
</div>
<div class="game_page_autocollapse" style="max-height: 850px;">
<div class="game_area_description" id="game_area_description">
<h2>About This Game</h2>
							The only aim in Rust is to survive.<br/>
<br/>
To do this you will need to overcome struggles such as hunger, thirst and cold. Build a fire. Build a shelter. Kill animals for meat. Protect yourself from other players, and kill them for meat. Create alliances with other players and form a town. <br/>
<br/>
Do whatever it takes to survive.						</div>
</div>
<div class="game_page_autocollapse">
<div class="game_area_description" id="game_area_content_descriptors">
<h2>Mature Content Description</h2>
<p>The developers describe the content like this:</p>
<p><i>
			This Game may contain content not appropriate for all ages, or may not be appropriate for viewing at work: Nudity or Sexual Content, Frequent Violence or Gore, General Mature Content				</i>
</p>
</div>
</div>
<div class="game_page_autocollapse sys_req" style="max-height: 300px;">
<h2>System Requirements</h2>
<div class="sysreq_tabs">
<div class="sysreq_tab active" data-os="win">
						Windows					</div>
<div class="sysreq_tab" data-os="mac">
						Mac OS X					</div>
<div style="clear: left;"></div>
</div>
<div class="sysreq_contents">
<div class="game_area_sys_req sysreq_content active" data-os="win">
<div class="game_area_sys_req_leftCol">
<ul>
<strong>Minimum:</strong><br/><ul class="bb_ul"><li>Requires a 64-bit processor and operating system<br/></li><li><strong>OS:</strong> Windows 8.1 64bit<br/></li><li><strong>Processor:</strong> Intel Core i7-3770 / AMD FX-9590 or better<br/></li><li><strong>Memory:</strong> 10 GB RAM<br/></li><li><strong>Graphics:</strong> GTX 670 2GB / AMD R9 280 better<br/></li><li><strong>DirectX:</strong> Version 11<br/></li><li><strong>Network:</strong> Broadband Internet connection<br/></li><li><strong>Storage:</strong> 20 GB available space<br/></li><li><strong>Additional Notes:</strong> SSD is highly recommended or expect longer than average load times.</li></ul> </ul>
</div>
<div class="game_area_sys_req_rightCol">
<ul>
<strong>Recommended:</strong><br/><ul class="bb_ul"><li>Requires a 64-bit processor and operating system<br/></li><li><strong>OS:</strong> Windows 10 64bit<br/></li><li><strong>Processor:</strong> Intel Core i7-4790K / AMD Ryzen 5 1600<br/></li><li><strong>Memory:</strong> 16 GB RAM<br/></li><li><strong>Graphics:</strong> GTX 980 / AMD R9 Fury<br/></li><li><strong>DirectX:</strong> Version 12<br/></li><li><strong>Network:</strong> Broadband Internet connection<br/></li><li><strong>Storage:</strong> 20 GB available space<br/></li><li><strong>Additional Notes:</strong> SSD is highly recommended.</li></ul> </ul>
</div>
<div style="clear: both;"></div>
</div>
<div class="game_area_sys_req sysreq_content" data-os="mac">
<div class="game_area_sys_req_leftCol">
<ul>
<strong>Minimum:</strong><br/><ul class="bb_ul"><li>Requires a 64-bit processor and operating system<br/></li><li><strong>OS:</strong> OS X El Capitan 10.11<br/></li><li><strong>Processor:</strong> Intel Core i7-3770 / AMD FX-9590 or better<br/></li><li><strong>Memory:</strong> 10 GB RAM<br/></li><li><strong>Graphics:</strong> GTX 670 2GB / AMD R9 280 better<br/></li><li><strong>Network:</strong> Broadband Internet connection<br/></li><li><strong>Storage:</strong> 20 GB available space<br/></li><li><strong>Additional Notes:</strong> Metal is required,</li></ul> </ul>
</div>
<div class="game_area_sys_req_rightCol">
<ul>
<strong>Recommended:</strong><br/><ul class="bb_ul"><li>Requires a 64-bit processor and operating system<br/></li><li><strong>OS:</strong> OS X El Capitan 10.11<br/></li><li><strong>Processor:</strong> Intel Core i7-4790K / AMD Ryzen 5 1600<br/></li><li><strong>Memory:</strong> 16 GB RAM<br/></li><li><strong>Graphics:</strong> GTX 980 / AMD R9 Fury<br/></li><li><strong>Network:</strong> Broadband Internet connection<br/></li><li><strong>Storage:</strong> 20 GB available space<br/></li><li><strong>Additional Notes:</strong> SSD is highly recommended or expect longer than average load times.</li></ul> </ul>
</div>
<div style="clear: both;"></div>
</div>
</div>
</div>
<script type="text/javascript">
		$J( function() {
			var $Tabs = $J('.sysreq_tab');
			var $Content = $J('.sysreq_content');

			$Tabs.click( function() {
				var $Tab = $J(this);
				$Tabs.removeClass('active');
				$Tab.addClass('active');

				$Content.removeClass('active');
				$Content.filter('[data-os=' + $Tab.data('os') + ']').addClass('active');

				$Content.trigger('gamepage_autocollapse_expand');
			});
		} );
	</script>
<div class="block">
<div class="block_header">
<div class="right"><a href="https://store.steampowered.com/mods/252490/?snr=1_5_9__game-mods">See All</a></div>
<h4>Community-Made Mods <span class="subh4">For this game</span></h4>
</div>
<div class="block_responsive_horizontal_scroll store_horizontal_autoslider">
<div class="block_content nopad">
<a class="small_cap" data-ds-appid="1222580" data-ds-itemkey="App_1222580" data-ds-tagids="[113,492,87]" href="https://store.steampowered.com/app/1222580/Rustissimo/?snr=1_5_9__game-mods" id="recommendation_cap_0" onmouseout="HideGameHover( this, event, 'global_hover' )" onmouseover="GameHover( this, event, 'global_hover', {&quot;type&quot;:&quot;app&quot;,&quot;id&quot;:1222580,&quot;public&quot;:1,&quot;v6&quot;:1} );">
<img border="0" class="small_cap_img" height="64" src="https://cdn.cloudflare.steamstatic.com/steam/apps/1222580/capsule_184x69.jpg?t=1588283583" width="171"/>
<h4>Rustissimo</h4>
</a>
<a class="small_cap" data-ds-appid="527440" data-ds-itemkey="App_527440" data-ds-tagids="[113,492]" href="https://store.steampowered.com/app/527440/Rustangelo/?snr=1_5_9__game-mods_1" id="recommendation_cap_1" onmouseout="HideGameHover( this, event, 'global_hover' )" onmouseover="GameHover( this, event, 'global_hover', {&quot;type&quot;:&quot;app&quot;,&quot;id&quot;:527440,&quot;public&quot;:1,&quot;v6&quot;:1} );">
<img border="0" class="small_cap_img" height="64" src="https://cdn.cloudflare.steamstatic.com/steam/apps/527440/capsule_184x69.jpg?t=1609524163" width="171"/>
<h4>Rustangelo</h4>
</a>
<a class="small_cap" data-ds-appid="505040" data-ds-itemkey="App_505040" data-ds-tagids="[492,1643,7332,5363,3968,5350,3859]" href="https://store.steampowered.com/app/505040/FORTIFY/?snr=1_5_9__game-mods_2" id="recommendation_cap_2" onmouseout="HideGameHover( this, event, 'global_hover' )" onmouseover="GameHover( this, event, 'global_hover', {&quot;type&quot;:&quot;app&quot;,&quot;id&quot;:505040,&quot;public&quot;:1,&quot;v6&quot;:1} );">
<img border="0" class="small_cap_img" height="64" src="https://cdn.cloudflare.steamstatic.com/steam/apps/505040/capsule_184x69_alt_assets_1.jpg?t=1596645087" width="171"/>
<h4>FORTIFY</h4>
</a>
<div style="clear: left;"></div>
</div>
</div>
</div>
<div class="block" id="recommended_block">
<div class="block_header">
<div class="right">
<a href="https://store.steampowered.com/recommended/morelike/app/252490/?snr=1_5_9__300">See all</a>
</div>
<h2>More like this</h2>
</div>
<div class="block_responsive_horizontal_scroll store_horizontal_autoslider block_content nopad" id="recommended_block_content">
</div>
</div>
<div class="rightcol game_meta_data" id="responsive_apppage_reviewblock_ctn"></div>
<div class="steam_curators_block block responsive_apppage_reviewblock">
<div class="block_header">
<div class="right"><a href="https://store.steampowered.com/curators/curatorsreviewing/?appid=252490&amp;snr=1_5_9__top-curators">View all</a></div>
<h2>What Curators Say</h2>
<div class="no_curators_followed">
					2,573 Curators have reviewed this product. Click <a href="https://store.steampowered.com/curators/curatorsreviewing/?appid=252490&amp;snr=1_5_9__top-curators">here</a> to see them.				</div>
</div>
</div>
</div>
<div style="clear: both;"></div>
</div>
<div class="review_ctn">
<div class="page_content">
<div class="app_reviews_area" id="app_reviews_hash">
<h2 class="user_reviews_header no_bottom_margin">Customer reviews</h2>
<input id="review_appid" type="hidden" value="252490"/>
<input id="review_default_day_range" type="hidden" value="30"/>
<input id="review_start_date" type="hidden" value="-1"/>
<input id="review_end_date" type="hidden" value="-1"/>
<input id="review_summary_num_positive_reviews" type="hidden" value="356535"/>
<input id="review_summary_num_reviews" type="hidden" value="416447"/>
<div class="review_recent_events" id="review_recent_events_container">
</div>
<div class="collapsed" id="review_histograms_container">
<canvas id="review_graph_canvas"></canvas>
<div class="review_histogram_section" id="review_histogram_rollup_section">
<div class="user_reviews_summary_bar">
<div class="summary_section">
<div class="title">Overall Reviews:</div>
<span class="game_review_summary positive" data-tooltip-html="85% of the 416,447 user reviews for this game are positive.">Very Positive</span>
<span>(416,447 reviews)</span>
<a class="tooltip" data-tooltip-text="This summary uses only reviews written by customers that purchased the game directly from Steam."><img src="https://store.cloudflare.steamstatic.com/public/shared/images/ico/icon_questionmark.png"/></a>
</div>
</div>
<div class="review_histogram" id="review_histogram_rollup_container">
<div id="review_histogram_rollup"></div>
</div>
</div><!--
--><div class="review_histogram_section recent" id="review_histogram_recent_section">
<div class="user_reviews_summary_bar">
<div class="summary_section">
<div class="title">Recent Reviews:</div>
<span class="game_review_summary positive" data-tooltip-html="91% of the 23,196 user reviews in the last 30 days are positive.">Very Positive</span>
<span>(23,196 reviews)</span>
<a class="tooltip" data-tooltip-text="This summary uses only reviews written by customers that purchased the game directly from Steam."><img src="https://store.cloudflare.steamstatic.com/public/shared/images/ico/icon_questionmark.png"/></a>
</div>
</div>
<div class="review_histogram">
<div id="review_histogram_recent"></div>
</div>
</div>
</div>
<div class="user_reviews_filter_options flyout graph_collapsed" id="reviews_filter_options">
<div class="user_reviews_filter_menu">
<div class="title">Review Type</div>
<div class="user_reviews_filter_menu_flyout">
<div class="user_reviews_filter_menu_flyout_content">
<input checked="" id="review_type_all" name="review_type" onchange="ShowFilteredReviews()" type="radio" value="all"/>
<label for="review_type_all">All <span class="user_reviews_count">(535,659)</span></label><br/>
<input id="review_type_positive" name="review_type" onchange="ShowFilteredReviews()" type="radio" value="positive"/>
<label for="review_type_positive">Positive <span class="user_reviews_count">(456,516)</span></label><br/>
<input id="review_type_negative" name="review_type" onchange="ShowFilteredReviews()" type="radio" value="negative"/>
<label for="review_type_negative">Negative <span class="user_reviews_count">(79,143)</span></label>
</div>
</div>
</div>
<div class="user_reviews_filter_menu">
<div class="title">Purchase Type</div>
<div class="user_reviews_filter_menu_flyout">
<div class="user_reviews_filter_menu_flyout_content">
<input checked="" id="purchase_type_all" name="purchase_type" onchange="ChangeReviewPurchaseTypeFilter()" type="radio" value="all"/>
<label for="purchase_type_all">All <span class="user_reviews_count">(535,659)</span></label><br/>
<input id="purchase_type_steam" name="purchase_type" onchange="ChangeReviewPurchaseTypeFilter()" type="radio" value="steam"/>
<label for="purchase_type_steam">Steam Purchasers <span class="user_reviews_count">(416,447)</span> <a class="tooltip" data-tooltip-text="These are reviews written by customers that purchased the game directly from Steam."><img src="https://store.cloudflare.steamstatic.com/public/shared/images/ico/icon_questionmark_dark.png"/></a></label><br/>
<input id="purchase_type_non_steam" name="purchase_type" onchange="ChangeReviewPurchaseTypeFilter()" type="radio" value="non_steam_purchase"/>
<label for="purchase_type_non_steam">Other <span class="user_reviews_count">(119,212)</span> <a class="tooltip" data-tooltip-text="These are reviews written by customers that did not purchase the game on Steam. (This may include legitimate sources such as other digital stores, retail stores, testing purposes, or press review purposes. Or, from inappropriate sources such as copies given in exchange for reviews.)"><img src="https://store.cloudflare.steamstatic.com/public/shared/images/ico/icon_questionmark_dark.png"/></a></label>
</div>
</div>
</div>
<div class="user_reviews_filter_menu">
<div class="title">Language</div>
<div class="user_reviews_filter_menu_flyout">
<div class="user_reviews_filter_menu_flyout_content">
<input id="review_language_all" name="review_language" onchange="ShowFilteredReviews()" type="radio" value="all"/>
<label for="review_language_all">All Languages <span class="user_reviews_count">(535,659)</span></label><br/>
<input checked="" id="review_language_mine" name="review_language" onchange="ShowFilteredReviews()" type="radio" value="english"/>
<label for="review_language_mine">Your Languages <span class="user_reviews_count">(275,317)</span> <a class="tooltip" data-tooltip-html="Your preferences are currently set to show content authored in these languages: English.&lt;br&gt;&lt;br&gt; Click 'customize' below to modify your preferences."><img src="https://store.cloudflare.steamstatic.com/public/shared/images/ico/icon_questionmark_dark.png"/></a></label><br/>
<div class="user_reviews_customize_language"><a href="https://store.steampowered.com//account/languagepreferences">Customize</a></div>
</div>
</div>
</div>
<div class="user_reviews_filter_menu" id="reviews_date_range_menu">
<div class="title">Date Range</div>
<div class="user_reviews_filter_menu_flyout">
<div class="user_reviews_filter_menu_flyout_content">
<div class="user_reviews_date_range_explanation">
							To view reviews within a date range, please click and drag a selection on a graph above or click on a specific bar.							<br/><br/>
<span class="btn_darkblue_white_innerfade btn_small_thin" onclick="SetReviewsGraphVisibility( true ); "><span>Show graph</span></span>
</div>
<input checked="" id="review_date_range_all" name="review_date_range" onchange="ClearReviewDateFilter()" type="radio" value="all"/>
<label for="review_date_range_all">Lifetime</label><br/>
<input disabled="" id="review_date_range_histogram" name="review_date_range" onchange="ShowFilteredReviews()" type="radio" value="include"/>
<label for="review_date_range_histogram">Only Specific Range (Select on graph above)&amp;nbsp</label><br/>
<input disabled="" id="review_date_range_exclude_histogram" name="review_date_range" onchange="ShowFilteredReviews()" type="radio" value="exclude"/>
<label for="review_date_range_exclude_histogram">Exclude Specific Range (Select on graph above)&amp;nbsp</label><br/>
</div>
</div>
</div>
<div class="user_reviews_filter_menu">
<div class="title">Playtime</div>
<div class="user_reviews_filter_menu_flyout">
<div class="user_reviews_filter_menu_flyout_content">
<div class="user_reviews_steam_labs_desc">
<a href="https://store.steampowered.com//communityrecommendations/"><img src="https://cdn.cloudflare.steamstatic.com/store/labs/main/images/steam_labs_logo.svg"/><span>Brought to you by Steam Labs</span></a>
</div>
<div class="user_reviews_playtime_filter_explanation">
							Filter reviews by the user's playtime when the review was written:						</div>
<input checked="" id="review_playtime_preset_0" name="review_playtime_preset" onchange="SelectPlaytimeFilterPreset( 0 )" type="radio" value="0"/>
<label for="review_playtime_preset_0">No Minimum</label><br/>
<input id="review_playtime_preset_1" name="review_playtime_preset" onchange="SelectPlaytimeFilterPreset( 1 )" type="radio" value="1"/>
<label for="review_playtime_preset_1">Over 1 hour</label><br/>
<input id="review_playtime_preset_10" name="review_playtime_preset" onchange="SelectPlaytimeFilterPreset( 10 )" type="radio" value="10"/>
<label for="review_playtime_preset_10">Over 10 hours</label><br/>
<input id="review_playtime_preset_100" name="review_playtime_preset" onchange="SelectPlaytimeFilterPreset( 100 )" type="radio" value="100"/>
<label for="review_playtime_preset_100">Over 100 hours</label><br/>
<div id="app_reviews_playtime_range_text">
<span id="app_reviews_playtime_range_text_min">No minimum</span> to <span id="app_reviews_playtime_range_text_max">No maximum</span>
</div>
<input id="app_reviews_playtime_range_min" type="hidden" value="0"/>
<input id="app_reviews_playtime_range_max" type="hidden" value="0"/>
<div id="app_reviews_playtime_slider"></div>
</div>
</div>
</div>
<div class="user_reviews_filter_display_as">
<span class="title">Display As: </span>
<select id="review_context" onchange="ShowFilteredReviews()">
<option value="summary">Summary</option>
<option value="all">Most Helpful</option>
<option value="recent">Recent</option>
<option value="funny">Funny</option>
</select>
</div>
<div class="user_reviews_filter_menu" id="user_reviews_offtopic_activity_menu" style="display: none">
<div class="title">Off-topic Review Activity</div>
<div class="user_reviews_filter_menu_flyout">
<div class="user_reviews_filter_menu_flyout_content">
<div class="user_reviews_offtopic_activity_explanation">
							When enabled, off-topic review activity will be filtered out.  This defaults to your Review Score Setting. Read more about it in the <a href="https://steamcommunity.com/games/593110/announcements/detail/1808664240333155775?snr=1_5_9_">blog post</a>.						</div>
<input checked="" id="reviews_offtopic_activity_checkbox" onchange="ChangedOfftopicReviewActivityFilter()" type="checkbox"/><label for="reviews_offtopic_activity_checkbox">Enabled</label>
</div>
</div>
</div>
<div style="float: right">
<span class="btnv6_blue_hoverfade btn_small_thin review_graph_toggle" id="review_show_graph_button" onclick="SetReviewsGraphVisibility( true ); "><span>Show graph</span> <div class="graph_toggle_icon down"> </div></span>
<span class="btnv6_blue_hoverfade btn_small_thin review_graph_toggle" id="review_hide_graph_button" onclick="SetReviewsGraphVisibility( false ); "><span>Hide graph</span> <div class="graph_toggle_icon up"> </div></span>
</div>
<div style="clear: both"></div>
</div>
<div class="reviews_info_ctn">
<div class="user_reviews_active_filters" id="reviews_active_filters">
<div class="title" id="reviews_filter_title">Filters</div>
<div class="active_filter" id="reviews_filter_type" onclick="ClearReviewTypeFilter()"></div>
<div class="active_filter" id="reviews_filter_purchase_type" onclick="ClearReviewPurchaseTypeFilter()"></div>
<div class="active_filter" id="reviews_filter_language" onclick="ClearReviewLanguageFilter()"></div>
<div class="active_filter" id="reviews_filter_graph" onclick="ClearReviewDateRangeFilter()"><span id="review_selected_histogram_date_range_prefix"></span><span id="review_selected_histogram_date_range_text"></span></div>
<div class="active_filter" id="reviews_filter_offtopic_activity" onclick="ClearOfftopicReviewActivityFilter()">Excluding Off-topic Review Activity</div>
<div class="active_filter" id="reviews_filter_playtime" onclick="ClearReviewPlaytimeFilter()">Playtime: <span id="review_playtime_preset_text"></span></div>
</div>
<div class="user_reviews_filter_score visible" id="user_reviews_filter_score"></div>
</div>
<div id="review_selected_filters"></div>
<div class="loading_more_reviews" id="LoadingMoreReviewsall" style="display: none">
<img class="loading_more_reviews_throbber" src="https://store.cloudflare.steamstatic.com/public/shared/images/throbber.gif"/>
			Loading reviews...		</div>
<div class="loading_more_reviews" id="LoadingMoreReviewsrecent" style="display: none">
<img class="loading_more_reviews_throbber" src="https://store.cloudflare.steamstatic.com/public/shared/images/throbber.gif"/>
			Loading reviews...		</div>
<div class="loading_more_reviews" id="LoadingMoreReviewspositive" style="display: none">
<img class="loading_more_reviews_throbber" src="https://store.cloudflare.steamstatic.com/public/shared/images/throbber.gif"/>
			Loading reviews...		</div>
<div class="loading_more_reviews" id="LoadingMoreReviewsnegative" style="display: none">
<img class="loading_more_reviews_throbber" src="https://store.cloudflare.steamstatic.com/public/shared/images/throbber.gif"/>
			Loading reviews...		</div>
<div class="loading_more_reviews" id="LoadingMoreReviewsfunny" style="display: none">
<img class="loading_more_reviews_throbber" src="https://store.cloudflare.steamstatic.com/public/shared/images/throbber.gif"/>
			Loading reviews...		</div>
<div class="user_reviews_container leftcol" id="Reviews_positive" style="display: none"></div>
<div class="user_reviews_container leftcol" id="Reviews_negative" style="display: none"></div>
<div class="user_reviews_container leftcol" id="Reviews_recent" style="display: none"></div>
<div class="user_reviews_container leftcol" id="Reviews_funny" style="display: none"></div>
<div class="user_reviews_container leftcol" id="Reviews_all" style="display: none"></div>
<div class="user_reviews_container" id="Reviews_summary">
<div>
<div class="leftcol">
</div>
<div class="rightcol recent_reviews">
</div>
<div style="clear:left;"></div>
<div class="view_all_reviews_btn leftcol" id="ViewAllReviewssummary">
<div class="review_box">
<div class="noReviewsYetTitle">There are no more reviews that match the filters set above</div>
<div class="noReviewsYetSub">Adjust the filters above to see other reviews</div>
<div style="clear: left; height: 40px;"></div>
</div>
</div>
<div style="clear: both"></div>
</div>
</div>
<div class="user_reviews_container" id="Reviews_loading">
<div class="LoadingWrapper">
<div class="LoadingThrobber">
<div class="Bar Bar1"></div>
<div class="Bar Bar2"></div>
<div class="Bar Bar3"></div>
</div>
<div class="LoadingText">Loading reviews...</div>
</div>
</div>
<div style="clear: left"></div>
</div>
</div>
</div>
</div>
</div>
<div class="hover game_hover" id="global_hover" style="display: none; left: 0; top: 0;">
<div class="game_hover_box hover_box">
<div class="content" id="global_hover_content">
</div>
</div>
<div class="hover_arrow_left"></div>
<div class="hover_arrow_right"></div>
</div>
<div id="EmbedModal" style="display: none">
<div id="widget_create">
<p>You can use this widget-maker to generate a bit of HTML that can be embedded in your website to easily allow customers to purchase this game on Steam.</p>
<p class="small">Enter up to 375 characters to add a description to your widget:</p>
<div class="app_embed_dialog_description">
<textarea maxlength="375" name="w_text" placeholder="The only aim in Rust is to survive - Overcome struggles such as hunger, thirst and cold. Build a fire. Build a shelter. Kill animals. Protect yourself from other players."></textarea>
</div>
<div class="buttoncontainer">
<a class="btnv6_blue_hoverfade btn_medium" href="#" onclick="CreateWidget(252490); return false;"><span>Create widget</span></a>
</div>
</div>
<div id="widget_finished" style="display: none;">
<div id="widget_container"></div>
<p class="small">Copy and paste the HTML below into your website to make the above widget appear</p>
<textarea id="widget_code" style=""></textarea>
</div>
</div>
<div id="ShareModal" style="display: none">
<div class="share"><a href="https://store.steampowered.com/share/facebook/app/252490" rel="noreferrer" target="_blank" title="Share on Facebook"><img src="https://store.cloudflare.steamstatic.com/public/images/v6/social/facebook.png"/></a><a href="https://store.steampowered.com/share/twitter/app/252490" rel="noreferrer" target="_blank" title="Share on Twitter"><img src="https://store.cloudflare.steamstatic.com/public/images/v6/social/twitter.png"/></a><a href="https://store.steampowered.com/share/reddit/app/252490" rel="noreferrer" target="_blank" title="Share on Reddit"><img src="https://store.cloudflare.steamstatic.com/public/images/v6/social/reddit.png"/></a></div></div>
<div id="application_root"></div>
<div class="app_tag_modal nologin" id="app_tagging_modal" style="display: none;">
<div class="app_tag_modal_content">
<div class="app_tag_modal_seperator"></div>
<div class="app_tag_modal_left">
<h2>Popular user-defined tags for this product:<span class="app_tag_modal_tooltip" data-tooltip-text="These are tags applied to the product by the most users.  You can click a tag to find other products with that tag applied.  Or, you can hit the plus symbol for any existing tags to increase that tag's popularity on this product.">(?)</span></h2>
<div class="app_tags popular_tags">
</div>
</div>
<div class="app_tag_modal_right">
<h2>Sign In</h2>
<p>Sign in to add your own tags to this product.</p>
<p>
<a class="btnv6_blue_hoverfade btn_medium" href="https://store.steampowered.com/login/?redir=app/252490">
<span>Sign In</span>
</a>
</p>
</div>
<div style="clear: both;"></div>
</div>
</div>
<script type="text/javascript">
		$J( function() {
			InitAppTagModal( 252490,
				[{"tagid":1662,"name":"Survival","count":15077,"browseable":true},{"tagid":1702,"name":"Crafting","count":9494,"browseable":true},{"tagid":3859,"name":"Multiplayer","count":9221,"browseable":true},{"tagid":1695,"name":"Open World","count":8717,"browseable":true},{"tagid":1100689,"name":"Open World Survival Craft","count":6652,"browseable":true},{"tagid":1643,"name":"Building","count":6401,"browseable":true},{"tagid":3810,"name":"Sandbox","count":6027,"browseable":true},{"tagid":1775,"name":"PvP","count":5913,"browseable":true},{"tagid":21,"name":"Adventure","count":4808,"browseable":true},{"tagid":3839,"name":"First-Person","count":4027,"browseable":true},{"tagid":19,"name":"Action","count":3843,"browseable":true},{"tagid":1663,"name":"FPS","count":3569,"browseable":true},{"tagid":6650,"name":"Nudity","count":3414,"browseable":true},{"tagid":1685,"name":"Co-op","count":2826,"browseable":true},{"tagid":1774,"name":"Shooter","count":2793,"browseable":true},{"tagid":3843,"name":"Online Co-Op","count":2714,"browseable":true},{"tagid":492,"name":"Indie","count":2674,"browseable":true},{"tagid":493,"name":"Early Access","count":2607,"browseable":true},{"tagid":3835,"name":"Post-apocalyptic","count":2175,"browseable":true},{"tagid":599,"name":"Simulation","count":1963,"browseable":true}],
				[],
				"1_5_9__410",
				"1_5_9__411",
				null			);

						if ( typeof GDynamicStore != 'undefined' )
				GDynamicStore.FixupNamePortion();
			
					});
	</script>
<link href="https://store.cloudflare.steamstatic.com/public/css/applications/store/main.css?v=QMxPHHa6V-nQ&amp;l=english&amp;_cdn=cloudflare" rel="stylesheet" type="text/css"/>
<script src="https://store.cloudflare.steamstatic.com/public/javascript/applications/store/manifest.js?v=aJMxf1liaTKX&amp;l=english&amp;_cdn=cloudflare" type="text/javascript"></script>
<script src="https://store.cloudflare.steamstatic.com/public/javascript/applications/store/libraries.js?v=4tdvttbEqG-y&amp;l=english&amp;_cdn=cloudflare" type="text/javascript"></script>
<script src="https://store.cloudflare.steamstatic.com/public/javascript/applications/store/main.js?v=xxI-KMJ3YKMZ&amp;l=english&amp;_cdn=cloudflare" type="text/javascript"></script>
</div> <!-- responsive_page_legacy_content -->
<div class="" id="footer_spacer" style=""></div>
<div class="" id="footer">
<div class="footer_content">
<div class="rule"></div>
<div id="footer_nav">
<span class="pulldown btnv6_blue_hoverfade btn_small" id="footer_steam_pulldown">
<span>ABOUT STEAM</span>
</span>
<div class="popup_block_new" id="footer_steam_dropdown" style="display: none;">
<div class="popup_body popup_menu">
<a class="popup_menu_item" href="https://store.steampowered.com/about/?snr=1_44_44__22">
					What is Steam?				</a>
<!--
					<a class="popup_menu_item" href="">
						Download Steam now					</a>
					-->
<a class="popup_menu_item" href="https://support.steampowered.com/kb_article.php?p_faqid=549#gifts" rel="noreferrer" target="_blank">
					Gifting on Steam				</a>
<a class="popup_menu_item" href="https://steamcommunity.com/?snr=1_44_44__22">
					The Steam Community				</a>
</div>
</div>
<span class="pulldown btnv6_blue_hoverfade btn_small" id="footer_valve_pulldown">
<span>ABOUT VALVE</span>
</span>
<div class="popup_block_new" id="footer_valve_dropdown" style="display: none;">
<div class="popup_body popup_menu">
<a class="popup_menu_item" href="http://www.valvesoftware.com/about.html" rel="noreferrer" target="_blank">
					About Valve				</a>
<a class="popup_menu_item" href="http://www.valvesoftware.com/business/" rel="noreferrer" target="_blank">
					Business Solutions				</a>
<a class="popup_menu_item" href="http://www.steampowered.com/steamworks/" rel="noreferrer" target="_blank">
					Steamworks				</a>
<a class="popup_menu_item" href="http://www.valvesoftware.com/jobs.html" rel="noreferrer" target="_blank">
					Jobs				</a>
</div>
</div>
<span class="pulldown btnv6_blue_hoverfade btn_small" id="footer_help_pulldown">
<span>HELP</span>
</span>
<div class="popup_block_new" id="footer_help_dropdown" style="display: none;">
<div class="popup_body popup_menu">
<a class="popup_menu_item" href="https://help.steampowered.com/en/?snr=1_44_44__23">
					Support				</a>
<a class="popup_menu_item" href="https://store.steampowered.com/forums/?snr=1_44_44__23" rel="noreferrer" target="_blank">
					Forums				</a>
<a class="popup_menu_item" href="https://store.steampowered.com/stats/?snr=1_44_44__23" rel="noreferrer" target="_blank">
					Stats				</a>
</div>
</div>
<span class="pulldown btnv6_blue_hoverfade btn_small" id="footer_feeds_pulldown">
<span>NEWS FEEDS</span>
</span>
<div class="popup_block_new" id="footer_feeds_dropdown" style="display: none;">
<div class="popup_body popup_menu">
<a class="popup_menu_item" href="https://store.steampowered.com/feeds/news.xml">
<img align="top" alt="" border="0" height="13" src="https://store.cloudflare.steamstatic.com/public/images/ico/ico_rss2.gif" width="13"/>  Steam News				</a>
<a class="popup_menu_item" href="https://store.steampowered.com/feeds/newreleases.xml">
<img align="top" alt="" border="0" height="13" src="https://store.cloudflare.steamstatic.com/public/images/ico/ico_rss2.gif" width="13"/>  Game Releases				</a>
<a class="popup_menu_item" href="https://store.steampowered.com/feeds/daily_deals.xml">
<img align="top" alt="" border="0" height="13" src="https://store.cloudflare.steamstatic.com/public/images/ico/ico_rss2.gif" width="13"/>  Daily Deals				</a>
</div>
</div>
<div style="clear: left;"></div>
<script type="text/javascript">
			RegisterFlyout( 'footer_genre_pulldown', 'footer_genre_dropdown', null, null, true );
			RegisterFlyout( 'footer_steam_pulldown', 'footer_steam_dropdown', null, null, true );
			RegisterFlyout( 'footer_valve_pulldown', 'footer_valve_dropdown', null, null, true );
			RegisterFlyout( 'footer_help_pulldown', 'footer_help_dropdown', null, null, true );
			RegisterFlyout( 'footer_feeds_pulldown', 'footer_feeds_dropdown', null, null, true );
		</script>
</div>
<br/>
<div class="rule"></div>
<div id="footer_logo_steam"><img alt="Valve Software" border="0" src="https://store.cloudflare.steamstatic.com/public/images/v6/logo_steam_footer.png"/></div>
<div id="footer_logo"><a href="http://www.valvesoftware.com" rel="noreferrer" target="_blank"><img alt="Valve Software" border="0" src="https://store.cloudflare.steamstatic.com/public/images/footerLogo_valve_new.png"/></a></div>
<div id="footer_text">
<div>© 2021 Valve Corporation.  All rights reserved.  All trademarks are property of their respective owners in the US and other countries.</div>
<div>VAT included in all prices where applicable.  

            <a href="https://store.steampowered.com/privacy_agreement/?snr=1_44_44_" rel="noreferrer" target="_blank">Privacy Policy</a>
              |  
            <a href="https://store.steampowered.com/legal/?snr=1_44_44_" rel="noreferrer" target="_blank">Legal</a>
              |  
            <a href="https://store.steampowered.com/subscriber_agreement/?snr=1_44_44_" rel="noreferrer" target="_blank">Steam Subscriber Agreement</a>
              |  
            <a href="https://store.steampowered.com/steam_refunds/?snr=1_44_44_" rel="noreferrer" target="_blank">Refunds</a>
</div>
<div class="responsive_optin_link">
<div class="btn_medium btnv6_grey_black" onclick="Responsive_RequestMobileView()">
<span>View mobile website</span>
</div>
</div>
</div>
<div style="clear: left;"></div>
<br/>
<div class="rule"></div>
<div class="valve_links">
<a href="http://www.valvesoftware.com/about.html" rel="noreferrer" target="_blank">About Valve</a>
          |  <a href="http://www.steampowered.com/steamworks/" rel="noreferrer" target="_blank">Steamworks</a>
          |  <a href="http://www.valvesoftware.com/jobs.html" rel="noreferrer" target="_blank">Jobs</a>
          |  <a href="https://partner.steamgames.com/steamdirect" rel="noreferrer" target="_blank">Steam Distribution</a>
        		  |  <a href="https://store.steampowered.com/digitalgiftcards/?snr=1_44_44_" rel="noreferrer" target="_blank">Gift Cards</a>
		  |  <a href="https://steamcommunity.com/linkfilter/?url=http://www.facebook.com/Steam" rel="noopener" target="_blank"><img src="https://store.cloudflare.steamstatic.com/public/images/ico/ico_facebook.gif"/> Steam</a>
		  |  <a href="http://twitter.com/steam" rel="noreferrer" target="_blank"><img src="https://store.cloudflare.steamstatic.com/public/images/ico/ico_twitter.gif"/> @steam</a>
</div>
</div>
</div>
</div> <!-- responsive_page_content -->
</div> <!-- responsive_page_frame -->
</body>
</html>"""