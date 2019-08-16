

//网易云评论解密
var CryptoJS = require('crypto-js');
var Rsa = require('rsa-js-java');
var JSON = require('JSON');
var d = '{"csrf_token":""}';

var i4m = {
    csrf_token: "",
    limit: "20",
    offset: "20",
    rid: "R_SO_4_28310081",
    total: "false",
};
i4m = JSON.stringify(i4m);
var e = "010001";
var f = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7";
var g = "0CoJUm6Qyw8W8jud";

function a(a) {
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1)
            e = Math.random() * b.length,
            e = Math.floor(e),
            c += b.charAt(e);
        return c
    };
function b(a, b) {
        var c = CryptoJS.enc.Utf8.parse(b)
          , d = CryptoJS.enc.Utf8.parse("0102030405060708")
          , e = CryptoJS.enc.Utf8.parse(a)
          , f = CryptoJS.AES.encrypt(e, c, {
            iv: d,
            mode: CryptoJS.mode.CBC
        });
        return f.toString()
    };
function c(a, b, c) {
        var d, e;
        return Rsa.setMaxDigits(131),
        d = new Rsa.RSAKeyPair(b,"",c),
        e = Rsa.encryptedString(d, a)
    };






function dd(d) {
        // d = JSON.stringify(d);
        var h = {}
          , i = a(16);
        encText = b(d, g);
        encText = b(encText, i);
        encSecKey = c(i, e, f);
        return [encText,encSecKey]
    }

    function e(a, b, d, e) {
        var f = {};
        return f.encText = c(a + e, b, d),
        f
    }
    // window.asrsea = d,
    // window.ecnonasr = e
data01 = dd(i4m);
console.log(i4m,typeof i4m);
// console.log(data01);