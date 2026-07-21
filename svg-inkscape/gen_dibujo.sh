#!/bin/bash

# Definir la variable base (sin extensión)
x="dibujo1"

# Ejecutar pdflatex e Inkscape
pdflatex "${x}.tex" && inkscape "${x}.pdf" --pdf-poppler --export-area-drawing --export-type=svg --export-filename="${x}.svg"

# Verificar si los comandos anteriores fueron exitosos
if [ $? -eq 0 ]; then
    # Eliminar archivos intermedios si el proceso fue exitoso
    rm -f "${x}.aux" "${x}.log" "${x}.pdf"
    echo "Proceso completado y archivos limpiados: ${x}.aux, ${x}.log, ${x}.pdf"
else
    echo "Error en el proceso. Los archivos intermedios se han conservado para depuración."
fi