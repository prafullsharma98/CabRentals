function show()
	{
		var x = document.getElementById("pwd");
	    if (x.type === "password") {
	        x.type = "text";
	    } else {
	        x.type = "password";
	    }
	}

function go()
	{
		
		var name=document.getElementById('name').value;
		var lname=document.getElementById('lastname').value;
		var email=document.getElementById('email').value;
		var pwd=document.getElementById('pwd').value;
		var cpwd=document.getElementById('cpwd').value;
		var pno=document.getElementById('pno').value;

		var error=0;
	      if(!check(name))
	      	{
	      		alert("error in name");
	      		document.getElementById('name').style.backgroundColor="#e2483d";
	      		error++;
	      	}

	      if(check(name))
	      {
	      	document.getElementById('name').style.backgroundColor="#7aef56";	
	      }	

	      if(!check(lname))
	      	{
	      		alert("error in last name");
	      		document.getElementById('lastname').style.backgroundColor="#e2483d";
	      		error++;
	      	}

	      if(check(lname))
	      {
	      	document.getElementById('lastname').style.backgroundColor="#7aef56";	
	      }	
	      		// document.getElementById('name').style.backgroundColor="#4ed145";

	      if(!validate(pwd))
	      	{
	      		alert("error in password");
	      		document.getElementById('pwd').style.backgroundColor="#e2483d";
	      		error++;

	      	}
	      if(validate(pwd))
	      {
	      	document.getElementById('pwd').style.backgroundColor="#7aef56";	
	      }	
	      	

	 	  if(!emailcheck(email))
	      	{
	      		alert("error in email");
	      		document.getElementById('email').style.backgroundColor="#e2483d";
	      		error++;

	      	}
	      if(emailcheck(email))
	      {
	      	document.getElementById('email').style.backgroundColor="#7aef56";	
	      }	
	      	if(!phonenumber(pno))
	      	{
	      		alert("error in phone number");
	      		document.getElementById('pno').style.backgroundColor="#e2483d";
	      		error++;
	      	}

	      	if(phonenumber(pno))
	      {
	      	document.getElementById('pno').style.backgroundColor="#7aef56";	
	      }

	      	if(pwd!=cpwd)
	      	{
	      		alert("confirm password not same as set password");
	      		document.getElementById('cpwd').style.backgroundColor="#e2483d";
	      		error++;
	      	}
	      	if(pwd==cpwd)
	      {
	      	document.getElementById('cpwd').style.backgroundColor="#7aef56";	
	      }
	      		
	      	if(error==0)
            	document.getElementById('sub').click();
	      		
	      	
	}





	function emailcheck(obj)
	{		var str=obj;
			var count=0;
			for(var i=0;i<str.length;i++)
			{
				if(str[i]=='@')count++;
			}

			if(str.indexOf('@')==-1||str.indexOf('.')==0||str.indexOf('@')==0||str.indexOf('.')==str.length-1||str.indexOf('@')==str.length-1||str.indexOf('.@')!=-1||str.indexOf('@.')!=-1||str.indexOf('..')!=-1||count!=1||str.indexOf(" ")!=-1)
				return false;
			else
				return true;
				
	}

	//*********************************************************************
	function validate(pwd)
	{
		
		if(pwd.length<5 || !(/[A-Z]/.test(pwd)) || !(/[0-9]/.test(pwd)))
			return false;
		else
			return true;

	}
//*********************************************************************************

	function check(obj)
	{
		if(/[0-9]/.test(obj))
			return false;
		else
			return true;
	}
//*********************************************************************************
function rating(obj)
{
	var str=obj.value;
    
	
	if(str.length<3)
		document.getElementById('strength').innerHTML="<i style='color:red'>invalid</i>";			
	else if(str.length>=3 && str.length<6)
		document.getElementById('strength').innerHTML="<i style='color:yellow'>weak</i>";
	else if(str.length>=6 && str.length<10)
		document.getElementById('strength').innerHTML="<i style='color:orange'>Decent</i>";
	else
		document.getElementById('strength').innerHTML="<i style='color:green'>Strong</i>";

}

function phonenumber(inputtxt)
{
  var phoneno = /^\d{10}$/;

  if(inputtxt.match(phoneno))
  {
  	return true;
  }
  else
  	return false;
}

