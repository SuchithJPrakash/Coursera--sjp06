function resp(){
 $ajaxUtils.sendGetRequest("plain.txt",hand);
}
function hand(txts){
	document.getElementById("f").value=txts
}