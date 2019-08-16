var pako = require('pako');
var btoa = require('btoa');
var  str = "[\"{\\\"qcertificatenum\\\":\\\"\\\",\\\"enterprisename\\\":\\\"\\\",\\\"qualificationlevel\\\":\\\"\\\",\\\"areacn\\\":\\\"\\\",\\\"approvaldate1\\\":\\\"\\\",\\\"approvaldate2\\\":\\\"\\\",\\\"firstcertificationdate1\\\":\\\"\\\",\\\"firstcertificationdate2\\\":\\\"\\\",\\\"keywords\\\":\\\"\\\",\\\"type\\\":\\\"1\\\"}\",\"8\"]";
function geta(str) {
    const binaryString = pako.deflate(str, { to: 'string' });
    re1 =  btoa(binaryString);
    return [re1,str]
}
console.log(geta(str)[0]);
