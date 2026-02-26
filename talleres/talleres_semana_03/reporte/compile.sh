#!/bin/bash
echo "🚀 Compilando reporte técnico..."
# Compilación (requiere texlive instalado en el container/sistema)
pdflatex -interaction=nonstopmode reporte.tex
# Limpieza de basura de LaTeX
rm -f *.aux *.log *.out *.toc
echo "✅ Proceso finalizado."
