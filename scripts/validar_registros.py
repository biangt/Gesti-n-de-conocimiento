#!/usr/bin/env python3
"""Valida los registros de conocimiento.

Comprueba que cada archivo de decisiones/, errores/, lecciones/, reuniones/ y
guias/ tenga los campos obligatorios, que autor y revisor sean personas
distintas, que el estado y la confidencialidad tengan un valor permitido y que
no haya registros de nivel rojo.
"""
import pathlib
import re
import sys

CARPETAS = ["decisiones", "errores", "lecciones", "reuniones", "guias"]
CAMPOS = ["tipo", "id", "titulo", "fecha", "autor", "revisor", "estado",
          "etiquetas", "confidencialidad", "fuentes"]
ESTADOS = {"vigente", "revisar", "obsoleto"}
NIVELES = {"equipo", "restringido"}  # rojo no se sube nunca


def leer_campos(texto):
    m = re.match(r"^---\n(.*?)\n---\n", texto, re.S)
    if not m:
        return None
    campos = {}
    for linea in m.group(1).splitlines():
        if ":" in linea:
            k, v = linea.split(":", 1)
            campos[k.strip()] = v.strip()
    return campos


def main(raiz):
    errores = []
    for carpeta in CARPETAS:
        for ruta in sorted((raiz / carpeta).glob("*.md")):
            campos = leer_campos(ruta.read_text(encoding="utf-8"))
            if campos is None:
                errores.append(f"{ruta}: falta el bloque de campos al inicio")
                continue
            for c in CAMPOS:
                if c not in campos:
                    errores.append(f"{ruta}: falta el campo '{c}'")
            if campos.get("autor") and campos.get("autor") == campos.get("revisor"):
                errores.append(f"{ruta}: autor y revisor deben ser personas distintas")
            if campos.get("estado") and campos["estado"] not in ESTADOS:
                errores.append(f"{ruta}: estado '{campos['estado']}' no permitido")
            if campos.get("confidencialidad") and campos["confidencialidad"] not in NIVELES:
                errores.append(f"{ruta}: confidencialidad '{campos['confidencialidad']}' no permitida en este repositorio")
            if campos.get("id") and campos["id"] != ruta.stem:
                errores.append(f"{ruta}: el id '{campos['id']}' no coincide con el nombre del archivo")
    for e in errores:
        print("ERROR", e)
    if errores:
        return 1
    print("Registros válidos.")
    return 0


if __name__ == "__main__":
    sys.exit(main(pathlib.Path(__file__).resolve().parent.parent))
