function login(){
    var user, password
    user = document.getElementById("usuario").value;
    password = document.getElementById("password").value;
    if( user == "admin" && password == "1234"){
        window.location = "../crudP.html"
    }
	if( user == "juan" && password == "tumama"){
		window.location = "../index.html"
	}else{
		alert('datos erroneos')
	}  
}

