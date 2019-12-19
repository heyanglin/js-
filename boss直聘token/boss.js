function get_token(tss,seedd,js) {
var atob = require('atob');
var document = {};
var window  = {};
window.document = document;
window.Date=Date;
window.decodeURIComponent = decodeURIComponent;
window.document.cookie = '';
window.document.title = '';
window.document.getElementById = function(a){};
window.document.createElement  = function(a){};
window.open = function () {};
window.open.toString = function(){
    return "function open() { [native code] }"
};
window.moveTo = function () {};
window.atob = atob;
var top = {};
top.location = {
    hash: "",
    host: "www.zhipin.com",
    hostname: "www.zhipin.com",
    href: "https://www.zhipin.com/web/common/security-check.html?seed=Z40akQ3mr0iw2XiV1DqnIuq7LdSKwWYzWvctpwo9660%3D&name=efef8ea9&ts=1576577448207&callbackUrl=%2Fjob_detail%2F30d92ad98a4acd891XB529u5FFM%7E.html%3Fka%3Dsearch_list_1&srcReferer=https%3A%2F%2Fwww.zhipin.com%2Fweb%2Fcommon%2Fsecurity-check.html%3Fseed%3DZ40akQ3mr0iw2XiV1DqnIjH4c%252FDfgzPSKOpY%252FqwBiKQ%253D%26name%3Defef8ea9%26ts%3D1576571154326%26callbackUrl%3D%252Fjob_detail%252F30d92ad98a4acd891XB529u5FFM%257E.html%253Fka%253Dsearch_list_1%26srcReferer%3Dhttps%253A%252F%252Fwww.zhipin.com%252Fweb%252Fcommon%252Fsecurity-check.html%253Fseed%253DZ40akQ3mr0iw2XiV1DqnIiZSeUznrlS6j7g%25252FCKGFlZQ%25253D%2526name%253Defef8ea9%2526ts%253D1576571127362%2526callbackUrl%253D%25252Fjob_detail%25252F30d92ad98a4acd891XB529u5FFM%257E.html%25253Fka%25253Dsearch_list_1%2526srcReferer%253D",
    origin: "https://www.zhipin.com",
    pathname: "/web/common/security-check.html",
    port: "",
    protocol: "https:",
};
var location = {
    host: "id.163yun.com",
    hostname: "id.163yun.com",
    href: "https://id.163yun.com/register",
    jsRoot: "/js/",
    origin: "https://id.163yun.com",
    pathname: "/register",
    protocol: "https:"
};
window.location=location;
window.screen = {
    availHeight: 1057,
    availLeft: 50,
    availTop: 23,
    availWidth: 1870,
    colorDepth: 24,
    height: 1080,
    width: 1920,
};
window.outerWidth = 1870;
window.innerWidth = 0;
window.outerHeight = 1057;
window.innerHeight = 0;
window.moveBy = function(){};
window.navigator = {
    appCodeName: "Mozilla",
    appName: "Netscape",
    appVersion: "5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36",
    browserLanguage: "zh-CN",
    cookieEnabled: true,
    language: "zh",
    maxTouchPoints: 0,
    msManipulationViewsEnabled: true,
    msMaxTouchPoints: 0,
    msPointerEnabled: true,
    onLine: true,
    platform: "MacIntel",
    pointerEnabled: true,
    product: "Gecko",
    systemLanguage: "zh",
    userAgent: "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36",
    userLanguage: "zh",
    vendor: "",
    vendorSub: "",
    webdriver: false,
    doNotTrack: "1"
};
    js = js.replace(/setInterval(.*?);function/g,'function').replace(/{}\.constructor/g,'{}\.\.constructor(');
    eval(js);
    var seed = seedd;
    var ts = tss;
    gg = new ABC().z(seed, parseInt(ts) + (480 + new Date().getTimezoneOffset()) * 60 * 1000);
    console.log(gg);
    return gg
}



