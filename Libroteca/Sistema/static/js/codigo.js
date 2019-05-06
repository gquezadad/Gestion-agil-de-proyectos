//Funcion que le da las caracteristicas al carrusel
$(document).ready(function(){
    $("#carrusel").bxSlider({
		captions:true,
		speed: 1000,
		auto:true
    }
        
    );    
})

$(function(){
   //sacar los mensajes de error
    $("errornombreUsuario").hide();
    $("erroremail").hide();
	$("errorfono").hide();
    
    //variables que indican valor de estado validacion
    var error_username = false;
	var error_email = false;
	var error_fono = false;
    
    $("#nombreUsuario").focusout(function() {

		check_username();
		
	});

    $("#numcontacto").focusout(function() {

		check_fono();
		
	});
	

	$("#email").focusout(function() {

		check_email();
		
	});

	/*funcion que genera mensaje en caso de que el nombre contenga caracteres que no sean letras o espacios */
	
	function check_username() {
		
		var pattern = new RegExp(/^[a-zA-Zñ\s]+$/);
	
		if(pattern.test($("#nombreUsuario").val())) {
				$("#errornombreUsuario").hide();
			} else {
				$("#errornombreUsuario").html("el nombre solo debe tener letras");
				$("#errornombreUsuario").show();
				error_nombreUsuario = true;
		}	

	}
    
	/*funcion que genera mensaje en caso de que el telefono contenga caracteres que no sean numeros */
	
	function check_fono() {
		
		if(isNaN($("#numcontacto").val())){
			$("#errorfono").html("El telefono solo deben contener numeros");
			$("#errorfono").show();
			error_fono = true;
		} else {
			$("#errorfono").hide();
		}
	
	}
	
	/*funcion que genera mensaje en caso de que el correo haya sido ingresado incorrectamente*/
	
	function check_email() {

		var pattern = new RegExp(/^[+a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/i);
	
		if(pattern.test($("#email").val())) {
				$("#erroremail").hide();
			} else {
				$("#erroremail").html("Direccion inválida");
				$("#erroremail").show();
				error_email = true;
		}
	
	}
	
	
	
	
	$("#registration_form").submit(function() {
											
		error_username = false;
		error_email = false;
		error_fono = false;
		error_rut = false;
											
		check_username();
		check_email();
		check_fono();
		check_rut();
		
		if(error_username == false && error_email == false && error_fono == false) {
			return true;
		} else {
			return false;	
		}
		
		

	});



});