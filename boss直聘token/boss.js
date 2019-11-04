

function get_token(tss,seedd,js) {
    const jsdom = require('jsdom');
    const {JSDOM} = jsdom;
    const dom = new JSDOM(`<html><head><body>hh</body></head></html>`);
    window = dom.window;
    document = window.document;
    window.navigator = {
        userAgent: "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
};
    js = js.replace(/setInterval(.*?);function/g,'function');
    eval(js);
    var seed = seedd;
    var ts = tss;
    gg = new ABC().z(seed, parseInt(ts) + (480 + new Date().getTimezoneOffset()) * 60 * 1000);
    return gg
}
