



`   `
var crypto = require('crypto');
var t = "214c37a6e3aec941422786d95ff9a5a143fb2da34f60fd72a0513311671ddb35ff4fe8117e1fcf0923681af39227db7ee0b7a291f62954febe8a71f57b98550db891ce70e5683a7b4ab67ee10245acbead1c81b319ebe6c8618fb992dcf6163ba73373d0aa52e9e5035108b8bde9dd202c8328c7e18a56b823093363ec37e77b060f34c86887052b7b9535f60c26a89987e5c5f14e35d478e6d9bb28e16be8f3b9875d45d0f95efb9893c2511aa5c35e";
var post_t = "{\"typeNum\":0,\"limit\":20,\"start\":9,\"title\":\"\"}";
var salt = "WBNMpy";

function a(t,salt) {
            var n = Buffer.from(salt + "0123456789qwerasdf")
              , r = Buffer.from("yibiao12" || 0)
              , o = t
              , a = crypto.createDecipheriv("des-ede3-cbc", n, r)
              , i = a.update(o, "hex", "utf-8");
            i += a.final("utf-8");
            // return encodeURIComponent(i)
            return i
        };

function r() {
            for (var e = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : 6, t = "ABCDEFGHJKMNPQRSTWXYZabcdefhijkmnprstwxyz2345678", n = t.length, r = "", o = 0; o < e; o++)
                r += t.charAt(Math.floor(Math.random() * n));
            return r
        };

function o(t,salt) {
            console.log(t);
            // dt = decodeURIComponent(t);
            var n = Buffer.from(salt + "0123456789qwerasdf")
              , r = Buffer.from("yibiao12" || 0)
              , o = t
              , a = crypto.createCipheriv("des-ede3-cbc", n, r);
            a.setAutoPadding(true);
            var i = a.update(o, "utf8", "hex");
            return i += a.final("hex")
        };

function print(i,a){
    console.log(i);
    return [i,a]

}
// console.log(a(t,salt));
// console.log(r());
// console.log(o(post_t,"2rtfZB"));