# Google Forms Spammer

Este repositorio contiene dos scripts escritos en Python diseñados para automatizar el envío de respuestas a un formulario de Google. Su propósito es realizar múltiples envíos automáticos.

## Contenido

- **`spammer_for_kiraaab.py`**  
  Script que envía **la misma respuesta fija** múltiples veces al formulario. Requiere configurar correctamente los campos `entry.X` y las cabeceras HTTP, incluyendo cookies.

- **`random_spam_for_kiraaab.py`**  
  Variante del script anterior, pero genera respuestas **aleatorias** a partir de listas predefinidas. Esto ayuda a simular diferentes usuarios o entradas variadas en cada ejecución. Requiere configurar manualmente el numero de preguntas, las posibles respuestas y la parte de `data`.

## Requisitos

- Python 3
- Módulo `requests` (puedes instalarlo con `pip install requests`)
