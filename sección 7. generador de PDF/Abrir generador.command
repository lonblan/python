#!/bin/bash
# Doble clic: abre el generador de certificados en el navegador.
cd "$(dirname "$0")" || exit 1
".venv/bin/python" "app_certificados.py"
estado=$?
if [ "$estado" -ne 0 ]; then
  echo ""
  echo "El programa terminó con un error (código $estado)."
  read -r -p "Pulsa Enter para cerrar..."
fi
