#! /bin/bash
# Programa para ejemplificar las operaciones de un archivo
# Autor: Harry Israel

echo "Operaciones de un archivo"

mkdir -m 744 backupScripts

echo "\nCopiar los scripts del directorio actual al nuevo directorio backupScripts"
cp *.* backupScripts/

echo "\nMover el directorio backupScripts a otra ubicación"
mkdir -m 744 backupScripts2
mv ./backupScripts/* ./backupScripts2

echo "\nEliminar los archivos .txt"
rm -r ./backupScripts2/*.txt
