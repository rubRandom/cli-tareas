"""Interfaz de línea de comandos del proyecto tareas."""

from __future__ import annotations

from datetime import datetime
from pathlib import Path

import typer
from rich.console import Console
from rich.table import Table

from tareas import __version__

app = typer.Typer(help="Automatiza tareas con ficheros.")
consola = Console()


def _tamano_legible(num_bytes: int) -> str:
    """Devuelve el tamaño en bytes, KB, MB, GB o TB con una sola decimal."""
    unidades = ("B", "KB", "MB", "GB", "TB")
    tamano = float(num_bytes)
    indice = 0
    while tamano >= 1024 and indice < len(unidades) - 1:
        tamano /= 1024
        indice += 1
    if unidades[indice] == "B":
        return f"{int(tamano)} B"
    return f"{tamano:.1f} {unidades[indice]}"


@app.command()
def version() -> None:
    """Muestra la versión instalada de tareas."""
    consola.print(f"tareas {__version__}")


@app.command()
def listar(
    carpeta: Path = typer.Argument(Path("."), help="Carpeta a listar (por defecto, la actual)."),
) -> None:
    """Muestra los ficheros y carpetas de CARPETA en una tabla."""
    ruta = carpeta.expanduser()
    if not ruta.is_dir():
        consola.print(f"[red]Error:[/red] no se puede listar '{ruta}': la carpeta no existe.")
        raise typer.Exit(1)

    tabla = Table(title=str(ruta))
    tabla.add_column("Nombre")
    tabla.add_column("Tipo")
    tabla.add_column("Tamaño", justify="right")
    tabla.add_column("Fecha")

    for entrada in sorted(ruta.iterdir(), key=lambda ruta: ruta.name.casefold()):
        datos = entrada.stat()
        if entrada.is_dir():
            tipo = "Carpeta"
            tamano = "-"
        elif entrada.is_file():
            tipo = "Fichero"
            tamano = _tamano_legible(datos.st_size)
        else:
            tipo = "Otro"
            tamano = "-"
        fecha = datetime.fromtimestamp(datos.st_mtime).strftime("%Y-%m-%d %H:%M")
        tabla.add_row(entrada.name, tipo, tamano, fecha)

    consola.print(tabla)
