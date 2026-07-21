#!/bin/bash
x="dibujo1"
pdflatex -interaction=batchmode "${x}.tex" >/dev/null 2>&1 && inkscape "${x}.pdf" --pdf-poppler --export-area-drawing --export-type=svg --export-filename="${x}.svg" && rm -f "${x}.aux" "${x}.log" "${x}.pdf" && echo "Completado" || echo "Error"
