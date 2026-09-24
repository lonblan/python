const formulario = document.querySelector("#formulario");
const fecha = document.querySelector("#fecha");
const excelRuta = document.querySelector("#excel-ruta");
const carpetaRuta = document.querySelector("#carpeta-ruta");
const elegirExcel = document.querySelector("#elegir-excel");
const elegirCarpeta = document.querySelector("#elegir-carpeta");
const generar = document.querySelector("#generar");
const resultado = document.querySelector("#resultado");
const mensaje = document.querySelector("#mensaje");
const lista = document.querySelector("#lista");
const avisos = document.querySelector("#avisos");
const listaAvisos = document.querySelector("#lista-avisos");
const abrir = document.querySelector("#abrir");

let carpetaElegidaAMano = false;

function rutaDe(elemento) {
  return elemento.dataset.ruta || "";
}

function ponerRuta(elemento, texto, vacio) {
  elemento.dataset.ruta = vacio ? "" : texto;
  elemento.textContent = texto;
  elemento.classList.toggle("ruta--vacia", vacio);
}

function limpiarListas() {
  lista.replaceChildren();
  listaAvisos.replaceChildren();
  avisos.hidden = true;
  abrir.hidden = true;
}

function mostrar(texto, tipo) {
  resultado.classList.remove("resultado--ok", "resultado--error");
  if (tipo) {
    resultado.classList.add(tipo);
  }
  mensaje.textContent = texto;
}

function llenarLista(elemento, textos) {
  elemento.replaceChildren();
  for (const texto of textos) {
    const item = document.createElement("li");
    item.textContent = texto;
    elemento.appendChild(item);
  }
}

async function leerJson(respuesta) {
  const datos = await respuesta.json();
  if (!respuesta.ok) {
    throw new Error(datos.error || "No se pudo completar la acción.");
  }
  return datos;
}

elegirExcel.addEventListener("click", async () => {
  elegirExcel.disabled = true;
  elegirCarpeta.disabled = true;
  const textoOriginal = elegirExcel.textContent;
  elegirExcel.textContent = "Eligiendo…";
  try {
    const datos = await leerJson(await fetch("/api/elegir-excel", { method: "POST" }));
    if (datos.cancelado) {
      return;
    }
    ponerRuta(excelRuta, datos.ruta, false);
    if (!carpetaElegidaAMano && datos.carpetaSugerida) {
      ponerRuta(carpetaRuta, datos.carpetaSugerida, false);
    }
  } catch (error) {
    limpiarListas();
    mostrar(error.message, "resultado--error");
  } finally {
    elegirExcel.disabled = false;
    elegirCarpeta.disabled = false;
    elegirExcel.textContent = textoOriginal;
  }
});

elegirCarpeta.addEventListener("click", async () => {
  elegirExcel.disabled = true;
  elegirCarpeta.disabled = true;
  const textoOriginal = elegirCarpeta.textContent;
  elegirCarpeta.textContent = "Eligiendo…";
  try {
    const datos = await leerJson(await fetch("/api/elegir-carpeta", { method: "POST" }));
    if (datos.cancelado) {
      return;
    }
    carpetaElegidaAMano = true;
    ponerRuta(carpetaRuta, datos.ruta, false);
  } catch (error) {
    limpiarListas();
    mostrar(error.message, "resultado--error");
  } finally {
    elegirExcel.disabled = false;
    elegirCarpeta.disabled = false;
    elegirCarpeta.textContent = textoOriginal;
  }
});

formulario.addEventListener("submit", async (evento) => {
  evento.preventDefault();
  limpiarListas();

  const excel = rutaDe(excelRuta);
  const carpeta = rutaDe(carpetaRuta);
  if (!excel) {
    mostrar("Elige el archivo Excel con los alumnos.", "resultado--error");
    return;
  }
  if (!fecha.value.trim()) {
    mostrar("Escribe la fecha que debe aparecer en los certificados.", "resultado--error");
    fecha.focus();
    return;
  }
  if (!carpeta) {
    mostrar("Elige la carpeta donde se guardarán los PDF.", "resultado--error");
    return;
  }

  generar.disabled = true;
  const textoOriginal = generar.textContent;
  generar.textContent = "Generando…";
  mostrar("Generando certificados…");

  try {
    const datos = await leerJson(await fetch("/api/generar", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        excel,
        fecha: fecha.value.trim(),
        carpeta,
      }),
    }));
    const cuantos = datos.archivos.length === 1 ? "1 certificado" : `${datos.archivos.length} certificados`;
    mostrar(`Listo. Se crearon ${cuantos}.`, "resultado--ok");
    llenarLista(lista, datos.archivos);
    if (datos.avisos && datos.avisos.length) {
      avisos.hidden = false;
      llenarLista(listaAvisos, datos.avisos);
    }
    abrir.hidden = false;
  } catch (error) {
    mostrar(error.message, "resultado--error");
  } finally {
    generar.disabled = false;
    generar.textContent = textoOriginal;
  }
});

abrir.addEventListener("click", async () => {
  abrir.disabled = true;
  try {
    await leerJson(await fetch("/api/abrir-carpeta", { method: "POST" }));
  } catch (error) {
    mostrar(error.message, "resultado--error");
  } finally {
    abrir.disabled = false;
  }
});

fetch("/api/inicio")
  .then((respuesta) => respuesta.json())
  .then((datos) => {
    if (datos.fecha) {
      fecha.value = datos.fecha;
    }
  })
  .catch(() => {
    mostrar("No pude conectar con el programa. Ábrelo de nuevo con doble clic.", "resultado--error");
  });
