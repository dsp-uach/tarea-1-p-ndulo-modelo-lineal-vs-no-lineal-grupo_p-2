#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
create_project_structure.py

Crea la estructura base del proyecto:
pendulo_lineal_vs_nolineal
"""

from pathlib import Path


def main():

    project_name = "pendulo_lineal_vs_nolineal"

    base_dir = Path.cwd() / project_name

    print(f"Creando proyecto en: {base_dir}")

    # Carpetas
    folders = [
        base_dir / "data",
        base_dir / "scripts",
        base_dir / "notebooks",
        base_dir / "results",
        base_dir / "results" / "plots"
    ]

    for folder in folders:
        folder.mkdir(parents=True, exist_ok=True)
        print(f"✔ Carpeta creada: {folder}")
    
        # Crear .gitkeep en cada carpeta
        gitkeep_file = folder / ".gitkeep"
        gitkeep_file.touch(exist_ok=True)

    # Archivos base
    files = {
        base_dir / "README.md": "# Péndulo: modelo lineal vs no lineal\n",
        base_dir / "requirements.txt": "numpy\nmatplotlib\nscipy\n",
        base_dir / ".gitkeep": ""
    }

    for file_path, content in files.items():
        file_path.write_text(content)
        print(f"✔ Archivo creado: {file_path}")

    print("\n Proyecto creado correctamente")


if __name__ == "__main__":
    main()