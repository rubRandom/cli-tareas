# Spec de `tareas`

1. **Para quién:** para mí, que preparo vídeos para un canal de curiosidades y acabo con todo mezclado.
2. **Problema:** guiones, voces, imágenes y renders se quedan revueltos y los ordeno a mano cada vez.
3. **Qué hace:** ejecuta acciones que defino en `acciones.json` sin tocar el código.
4. **Órdenes:** `--help`, `version`, `listar [CARPETA]`, `acciones`, `validar` y `ejecutar NOMBRE [CARPETA]`.
5. **Opciones:** `--simular` para ver qué haría sin tocar nada, `--si` para no preguntar y `--config` para usar otro JSON.
6. **Tipos de acción:** mover, copiar, renombrar y borrar. En la semana 3, dos acciones con IA.
7. **Seguridad:** lo que borra pide confirmación, y nunca se sobrescribe un fichero que ya existe.
8. **Errores:** mensaje claro y código de salida, nunca un traceback.
9. **Qué NO hará:** no sube nada a internet (salvo la IA), no toca carpetas fuera de las que indique y no edita el contenido de los ficheros.
10. **Funciona en:** Windows, Linux y macOS, y se instala con una orden (`uv tool install`).
