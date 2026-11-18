// Botón "Limpiar": vacía los campos del formulario y oculta el resultado anterior.
"use strict";

document.querySelectorAll("[data-limpiar]").forEach((boton) => {
  boton.addEventListener("click", () => {
    const formulario = boton.closest("form");

    // vaciar cajas de texto / número / contraseña
    formulario.querySelectorAll("input").forEach((campo) => {
      campo.value = "";
    });

    // regresar las listas desplegables a su primera opción
    formulario.querySelectorAll("select").forEach((lista) => {
      lista.selectedIndex = 0;
    });

    // quitar la salida o el mensaje de error que estuviera en pantalla
    document.querySelectorAll("[data-resultado]").forEach((bloque) => bloque.remove());

    // dejar el cursor en el primer campo
    const primero = formulario.querySelector("input, select");
    if (primero) primero.focus();
  });
});
