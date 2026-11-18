# tareas · CLI para automatizar tareas con ficheros (proyecto de 1º DAM)

Herramienta de terminal que ejecuta acciones definidas en `acciones.json` (mover, copiar,
renombrar, borrar y, más adelante, acciones con IA). La temática de ejemplo es la producción
de vídeos de un canal: guiones, voces, imágenes y renders.

## Stack y órdenes
- Python 3.12 + Typer + Rich, gestionado con uv (src layout, paquete `src/tareas`).
- Ayuda: `uv run tareas --help` · Validar config: `uv run tareas validar` · Pruebas: `uv run pytest`.
- El alumno desarrolla en Windows (PowerShell); tiene que funcionar también en Linux y macOS.

## Estructura
- `cli.py`: solo la interfaz con Typer (órdenes, opciones, salida con Rich).
- `config.py`: lee y valida `acciones.json`. `errores.py`: excepciones propias.
- `motor.py` y `acciones.py`: la lógica, sin saber nada de Typer.
- Si se pasa una CARPETA en la orden, sustituye al `origen` de la acción.

## Normas
- Mensajes, comentarios y docstrings en español; código claro antes que listo.
- pathlib siempre, `expanduser()` para `~`, `encoding="utf-8"`, shutil para mover y copiar.
  Nada de os.system ni shell=True.
- Nunca un traceback ante errores previsibles: mensaje claro y código de salida
  (0 bien · 1 fallo al ejecutar · 2 error de uso · 3 configuración inválida).
- Nunca sobrescribir un fichero existente.
- Las acciones solo se prueban en `~/pruebas-tareas` y primero con `--simular`.
- No toques `.env` ni escribas claves en ningún fichero. No hagas commits ni push: los hace el alumno.
- Tareas pequeñas. Antes de cambiar un fichero, explica en 2-3 líneas qué vas a hacer.
