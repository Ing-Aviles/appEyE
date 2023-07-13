 // Crear eventos automáticamente
  const eventContainer = document.getElementById("eventContainer");
  eventos.forEach(evento => {
    const eventElement = document.createElement("div");
    eventElement.classList.add("event");

    const imageElement = document.createElement("img");
    imageElement.classList.add("event-image");
    imageElement.src = evento.imagen;
    imageElement.alt = "Imagen del Evento";

    const nameElement = document.createElement("h2");
    nameElement.classList.add("event-name");
    nameElement.textContent = evento.nombre;

    const descriptionElement = document.createElement("p");
    descriptionElement.classList.add("event-description");
    descriptionElement.textContent = evento.descripcion;

    const dateElement = document.createElement("p");
    dateElement.classList.add("event-details");
    dateElement.textContent = "Fecha de Registro: " + evento.fechaRegistro;

    const cuposElement = document.createElement("p");
    cuposElement.classList.add("event-details");
    cuposElement.textContent = "Cupos Disponibles: " + evento.cuposDisponibles;

    eventElement.appendChild(imageElement);
    eventElement.appendChild(nameElement);
    eventElement.appendChild(descriptionElement);
    eventElement.appendChild(dateElement);
    eventElement.appendChild(cuposElement);

    eventContainer.appendChild(eventElement);
  });

  // Cambiar el color de fondo al desplazarse
  window.addEventListener("scroll", function() {
    const body = document.body;
    const scrollY = window.scrollY;

    if (scrollY > 0) {
      body.classList.add("scroll-background");
    } else {
      body.classList.remove("scroll-background");
    }
  });

  $(document).ready(function() {
    // Agregar evento de clic al botón
    $("#sidebar-toggle").click(function() {
      // Alternar la clase "active" en la barra lateral
      $(".sidebar").toggleClass("active");
    });
  });

  const wrapper = document.querySelector('.wrapper');
const loginLink = document.querySelector('.login-link');
const registroLink = document.querySelector('.registro-link');
const btnPopup = document.querySelector('.btnLogin-popup');

const iconClose = document.querySelector('.icon-close');
const iconClosed = document.querySelector('.btn-close');

const contenedor = document.querySelector('.contenedor');
const empLink = document.querySelector('.emp-link');
const empresaLink = document.querySelector('.empresa-link');
const btnRegistrar = document.querySelector('.btnRegistrar-popup');
const boton = document.querySelector('.boton');

const vista = document.querySelector('.vista');
const btnLoginPopup = document.querySelector('.btnLogin-popup');
const btnRegistrarPopup = document.querySelector('.btnRegistrar-popup');

const btnCerrarLogin = document.querySelector('.wrapper .icon-close');
const btnCerrarRegistro = document.querySelector('.wrapper .icon-close');

const BtnCerrarLogin = document.querySelector('.contenedor .btn-close');
const BtnCerrarRegistro = document.querySelector('.contenedor .btn-close');

/*BtnPopup.addEventListener('click', () => {
  vista.classList.remove('desactivar');
});
Btnpopup.addEventListener('click', () => {
  vista.classList.remove('desactivar-popup');
})*/

//Eventos para que desaparezca el div vista al clikear empresa o estudinte
btnLoginPopup.addEventListener('click', () => {
  vista.style.display = 'none';
});
btnRegistrarPopup.addEventListener('click', () => {
  vista.style.display = 'none';
});

registroLink.addEventListener('click', () => {
    wrapper.classList.add('active');
});
loginLink.addEventListener('click', () => {
    wrapper.classList.remove('active');
});

btnPopup.addEventListener('click', () => {
    wrapper.classList.add('active-popup');
});
iconClose.addEventListener('click', () => {
    wrapper.classList.remove('active-popup');
});


btnRegistrar.addEventListener('click', () => {
  contenedor.classList.add('activo-popup');
});
iconClosed.addEventListener('click', () => {
  contenedor.classList.remove('activo-popup');
});
empresaLink.addEventListener('click', () => {
  contenedor.classList.add('activo');
});
empLink.addEventListener('click', () => {
  contenedor.classList.remove('activo');
});

btnCerrarLogin.addEventListener('click', () => {
  vista.style.display = 'block';
});
btnCerrarRegistro.addEventListener('click', () => {
  vista.style.display = 'block';
});

BtnCerrarLogin.addEventListener('click', () => {
  vista.style.display = 'block';
});
BtnCerrarRegistro.addEventListener('click', () => {
  vista.style.display = 'block';
});

const yearSelect = document.getElementById("year");

// obtener el año actual
const currentYear = new Date().getFullYear();

// generar opciones de años y agregarlas al elemento select
for (let year = currentYear; year >= 2010; year--) {
  const option = document.createElement("option");
  option.text = year;
  option.value = year;
  yearSelect.add(option);
}

function validarFormulario() {
  // obtener los campos del formulario del primer registro
  const programa = document.getElementsByName("programa")[0];
  const proceso = document.getElementsByName("proceso")[0];
  const periodo = document.getElementsByName("periodo")[0];
  const ano = document.getElementsByName("año")[0];
  const razon = document.getElementsByName("razon")[0];
  const nombre = document.getElementsByName("nombre")[0];
  const cargo = document.getElementsByName("cargo")[0];

  // validar que los campos no estén vacíos
  if (nombre.value === "" || programa.value === "" || proceso.value === "" || periodo.value === "" || ano.value === "" || razon.value === "" || cargo.value === "") {
    alert("Por favor complete todos los campos del registro 1.");
  } else {
    // si los campos están completos, enviar al usuario al formulario del segundo registro
    document.getElementById("form-box.direccion").submit();
  }
}


var prevScrollpos = window.pageYOffset;
window.onscroll = function() {
  var currentScrollPos = window.pageYOffset;
  if (prevScrollpos > currentScrollPos) {
    document.getElementById("header").style.top = "0";
  } else {
    document.getElementById("header").style.top = "-60px";
  }
  prevScrollpos = currentScrollPos;
}
