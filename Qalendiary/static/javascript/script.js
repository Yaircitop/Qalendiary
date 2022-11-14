document.addEventListener("DOMContentLoaded", () => {
	const $tiempoRestante = document.querySelector("#tiempoRestante"),
		$btnIniciar = document.querySelector("#btnIniciar"),
		$btnPausar = document.querySelector("#btnPausar"),
		$btnDetener = document.querySelector("#btnDetener"),
		$minutos = document.querySelector("#minutos"),
		$segundos = document.querySelector("#segundos"),
		$contenedorInputs = document.querySelector("#contenedorInputs"),
		$reloj1 = document.querySelector("#rel-norm"),
		$reloj2 = document.querySelector("#rel-alarm");
	let idInterval = null, diferenciaTemporal = 0,
		fechaFuturo = null;
	// Carga un sonido a través de su fuente y lo inyecta de manera oculta
	// Tomado de: https://parzibyte.me/blog/2020/09/28/reproducir-sonidos-javascript/
	const cargarSonido = function (fuente) {
		const sonido = document.createElement("audio");
		sonido.src = fuente;
		sonido.loop = true;
		sonido.setAttribute("preload", "auto");
		sonido.setAttribute("controls", "none");
		sonido.style.display = "none"; // <-- oculto
		document.body.appendChild(sonido);
		return sonido;
	};

	const sonido = cargarSonido('../../static/javascript/timer.mp3');
	const ocultarElemento = elemento => {
		elemento.style.display = "none";
	}

	const mostrarElemento = elemento => {
		elemento.style.display = "";
	}

	const iniciarTemporizador = (minutos, segundos) => {
		ocultarElemento($contenedorInputs);
		mostrarElemento($btnPausar);
		ocultarElemento($btnIniciar);
		ocultarElemento($btnDetener);
		mostrarElemento($reloj1);
		ocultarElemento($reloj2);
		if (fechaFuturo) {
			fechaFuturo = new Date(new Date().getTime() + diferenciaTemporal);
			diferenciaTemporal = 0;
		} else {
			const milisegundos = (segundos + (minutos * 60)) * 1000;
			fechaFuturo = new Date(new Date().getTime() + milisegundos);
		}
		clearInterval(idInterval);
		idInterval = setInterval(() => {
			const tiempoRestante = fechaFuturo.getTime() - new Date().getTime();
			if (tiempoRestante <= 0) {
				clearInterval(idInterval);
				sonido.play();
				ocultarElemento($btnPausar);
				mostrarElemento($btnDetener);
				ocultarElemento($reloj1);
				mostrarElemento($reloj2);
			} else {
				$tiempoRestante.textContent = milisegundosAMinutosYSegundos(tiempoRestante);
			}
		}, 50);
	};

	var fotoMostrada = "relojito-alarma.png"

	function relojito(){
		var elemento = document.getElementById("rel-norm");
		elemento.src = "../../static/relojito-alarma.png";
	}

	const pausarTemporizador = () => {
		ocultarElemento($btnPausar);
		mostrarElemento($btnIniciar);
		mostrarElemento($btnDetener);
		diferenciaTemporal = fechaFuturo.getTime() - new Date().getTime();
		clearInterval(idInterval);
	};

	const detenerTemporizador = () => {
		ocultarElemento($reloj2);
		ocultarElemento($reloj1);
		clearInterval(idInterval);
		fechaFuturo = null;
		diferenciaTemporal = 0;
		sonido.currentTime = 0;
		sonido.pause();
		$tiempoRestante.textContent = "00:00.0";
		init();
	};

	const agregarCeroSiEsNecesario = valor => {
		if (valor < 10) {
			return "0" + valor;
		} else {
			return "" + valor;
		}
	}
	const milisegundosAMinutosYSegundos = (milisegundos) => {
		const minutos = parseInt(milisegundos / 1000 / 60);
		milisegundos -= minutos * 60 * 1000;
		segundos = (milisegundos / 1000);
		return `${agregarCeroSiEsNecesario(minutos)}:${agregarCeroSiEsNecesario(segundos.toFixed(1))}`;
	};
	const init = () => {
		$minutos.value = "";
		$segundos.value = "";
		mostrarElemento($contenedorInputs);
		mostrarElemento($btnIniciar);
		ocultarElemento($btnPausar);
		ocultarElemento($btnDetener);
	};


	$btnIniciar.onclick = () => {
		const minutos = parseInt($minutos.value);
		const segundos = parseInt($segundos.value);
		if (isNaN(minutos) || isNaN(segundos) || (segundos <= 0 && minutos <= 0)) {
			return;
		}
		iniciarTemporizador(minutos, segundos);
	};
	init();
	$btnPausar.onclick = pausarTemporizador;
	$btnDetener.onclick = detenerTemporizador;
});
