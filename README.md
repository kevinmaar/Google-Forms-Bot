# Google Form Spammer (Kiraaab Edition)

Este repositorio contiene dos scripts escritos en Python diseñados para automatizar el envío de respuestas a un formulario de Google. Su propósito es realizar múltiples envíos automáticos, útil para pruebas, demostraciones o fines educativos.

## Contenido

- **`spammer_for_kiraaab.py`**  
  Script que envía **la misma respuesta fija** múltiples veces al formulario. Requiere configurar correctamente los campos `entry.X` y las cabeceras HTTP, incluyendo cookies.

- **`random_spam_for_kiraaab.py`**  
  Variante del script anterior, pero genera respuestas **aleatorias** a partir de listas predefinidas. Esto ayuda a simular diferentes usuarios o entradas variadas en cada ejecución.

## Requisitos

- Python 3
- Módulo `requests` (puedes instalarlo con `pip install requests`)

## Advertencia ⚠️

> Estos scripts fueron desarrollados con fines **educativos y de pruebas** únicamente.  
> El mal uso de estas herramientas puede violar los Términos de Servicio de Google Forms u otras plataformas.  
> **Úsalos bajo tu responsabilidad.**
