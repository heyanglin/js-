var document = {};
document.cookie = '';
var _J = {};
document.createElement = function () {
    return _J
};
_J.innerHTML='';
_J.firstChild={};
_J.firstChild.href='http://www.jiuxian.com/';
var location = {};
location.href = '';
var window = {};
document.addEventListener = function (a, b) {
    return true
};
document.attachEvent = function (a, b) {
    return true
};
setTimeout = function (s) {

};
function getcookie(s) {
// var x = eval(a),
//     y = b,
    aa = s.match(/var x=.*?}"/g,s)[0];
    // console.log(aa);
    eval(aa);
    f = function (x, y) {
        var a = 0, b = 0, c = 0;
        x = x.split("");
        y = y || 99;
        while ((a = x.shift()) && (b = a.charCodeAt(0) - 77.5))
            c = (Math.abs(b) < 13 ? (b + 48.5) : parseInt(a, 36)) + y * c;
        return c
    }, z = f(y.match(/\w/g).sort(function (x, y) {
        return f(x) - f(y)
    }).pop());
    var list = [];
    while (z++) try {
        hhh = y.replace(/\b\w+\b/g, function (y) {
            return x[f(y, z) - 1] || ("_" + y)
        });
        break
    } catch (_) {
        console.log(_)
    }

    cookie = hhh.match(/document.cookie(.*?Path=\/;')/g)[0];
    console.log(cookie);
    eval(cookie);
    console.log(document.cookie);
    return document.cookie
};
getcookie(
    "<script>var x=\"@try@parseInt@@fromCharCode@innerHTML@@e@var@Lh@JhhDWD5@@@catch@01@window@@36@@D@reverse@location@div@while@@@toString@@1500@@@else@split@JgSe0upZ@charAt@match@document@1565658101@DOMContentLoaded@@@setTimeout@f@@@02@@@attachEvent@9@g@@1@@@toLowerCase@href@@@BFU@pathname@eval@0@function@charCodeAt@createElement@0xFF@length@@@@onreadystatechange@3ErZ@@RegExp@@__jsl_clearance@d@@AZhD@19@@Tue@8@638@GMT@false@replace@@@addEventListener@0xEDB88320@3@@@rOm9XFMtA3QKV7nYsPGT4lifyWwkq5vcjH2IdxUoCbhERLaz81DNB6@2@for@@return@if@13@new@join@a@@Path@Aug@@@chars@cookie@firstChild@Array@41@@@@String@@captcha@@https@@substr@challenge@search@Expires\".replace(/@*$/,\"\").split(\"@\"),y=\"9 j=1o(){12('m.1h=m.1l+m.37.28(/[\\\\?|&]31-36/,\\\\'\\\\')',t);B.2w='1B=C.25|1n|'+(1o(){9 2B=[1o(j){2k j},1o(2B){2k 2B},(1o(){9 j=B.1q('n');j.6='<2p 1h=\\\\'/\\\\'>7</2p>';j=j.2x.1h;9 2B=j.A(/33?:\\\\/\\\\//)[1n];j=j.35(2B.1s).1g();2k 1o(2B){2i(9 7=1n;7<2B.1s;7++){2B[7]=j.z(2B[7])};2k 2B.2o('')}})(),1o(j){2i(9 2B=1n;2B<j.1s;2B++){j[2B]=3(j[2B]).r(i)};2k j.2o('')}],j=['1x',[(-~{}+[]+[[]][1n])+[-~(-~{}+(-~!{}<<-~!{}))]],'20',[(2h+[]+[[]][1n])+[(-~!{}<<-~!{})+[(-~!{}<<-~!{})]*(-~[-~{}-~{}])]],[[-~(-~{}+(-~!{}<<-~!{}))]],'a',[(-~{}+[]+[[]][1n])+[-~(-~{}+(-~!{}<<-~!{}))]],'1a',((-~{}+[-~-~{}]>>-~-~{})+[]),'b',((-~{}+[-~-~{}]>>-~-~{})+[]),'1k%',((-~{}+[-~-~{}]>>-~-~{})+[]),'k'];2i(9 7=1n;7<j.1s;7++){j[7]=2B[[1d,2d,1d,2d,2h,1d,2d,1d,1n,1d,1n,1d,1n,1d][7]](j[7])};2k j.2o('')})()+';38=23, 2m-2s-21 16:f:2z 26;2r=/;'};2l((1o(){2{2k !!g.2b;}e(8){2k 27;}})()){B.2b('D',j,27)}w{B.19('1w',j)}\",f=function(x,y){var a=0,b=0,c=0;x=x.split(\"\");y=y||99;while((a=x.shift())&&(b=a.charCodeAt(0)-77.5))c=(Math.abs(b)<13?(b+48.5):parseInt(a,36))+y*c;return c},z=f(y.match(/\\w/g).sort(function(x,y){return f(x)-f(y)}).pop());while(z++)try{eval(y.replace(/\\b\\w+\\b/g, function(y){return x[f(y,z)-1]||(\"_\"+y)}));break}catch(_){}</script>"

    );
