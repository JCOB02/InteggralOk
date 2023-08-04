function integrar_js() {
/* ---------------------------------------- *
 * FUNCION integrar_js()                    *
 * 	Recopila las entradas del usuario   *
 * 	y las manda a una funcion de python *
 * ---------------------------------------- */
	// Declaracion de las variables
	let ecuacion1 = document.getElementById("ecuacion1").value
	let ecuacion2 = document.getElementById("ecuacion2").value
	let lim_a = document.getElementById("limite_a").value
	let lim_b = document.getElementById("limite_b").value;

	// Comprobar que las variables no esten vacias
	if ( ecuacion1.length === 0 ) { ecuacion1 = 0 }
	if ( ecuacion2.length === 0 ) { ecuacion2 = 0 }
	if ( lim_a.length === 0 ) { lim_a = 0 }
	if ( lim_b.length === 0 ) { lim_b = 0 }

	// Llamar integrar() desde python
	eel.integrar(ecuacion1, ecuacion2, lim_a, lim_b)(function(x) {
		// Actualizar la respuesta con el resultado
		document.getElementById("respuesta").innerHTML = x;
	})
}

function volumen_js() {
/* ---------------------------------------- * 
 * FUNCION volumen_js()                     *
 *      Recopila las entradas del usuario   *
 *      y las manda a una funcion de python *
 * ---------------------------------------- */
	// Declaracion de las variables
	let ecuacion1 = document.getElementById("ecuacion1").value;
	let ecuacion2 = document.getElementById("ecuacion2").value;
	let lim_a = document.getElementById("limite_a").value;
	let lim_b = document.getElementById("limite_b").value;

	if ( ecuacion1.length === 0 ) { ecuacion1 = 0 }
	if ( ecuacion2.length === 0 ) { ecuacion2 = 0 }
	if ( lim_a.length === 0 ) { lim_a = 0 }
	if ( lim_b.length === 0 ) { lim_b = 0 }

	// Llamar volumen() desde python
	eel.volumen(ecuacion1, ecuacion2, lim_a, lim_b)(function(x) {
		// Actualizar la respuesta con el resultado
		document.getElementById("respuesta").innerHTML = x;
	})
}
