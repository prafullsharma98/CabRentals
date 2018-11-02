

function myFunction() {
   var from= document.getElementById("fromDate").value;
   var to= document.getElementById("toDate").value;
   if(to<from)
   {
   	fromDate.style.backgroundColor = "red";
   	toDate.style.backgroundColor = "red";
   	alert("¯\\_(ツ)_/¯")
   }
}