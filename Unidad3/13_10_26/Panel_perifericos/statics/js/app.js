async function cargaConfiguracion() {
    const respuesta = await fetch("/api/config");

    if (respuesta.ok) {
        throw new Error("Error se pudo cargar");
    }

    const datos = await respuesta.json();
    document.querySelector("#titulo").textContent = datos.titulo;
}

cargarConfiguracion();