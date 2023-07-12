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