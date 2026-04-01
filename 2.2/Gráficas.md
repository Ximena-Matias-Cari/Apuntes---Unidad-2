# Ejemplo: Generación de gráficas con Matplotlib y Flet

## Descripción general

Este programa genera diferentes tipos de gráficas utilizando la librería **Matplotlib** y las muestra en una interfaz gráfica creada con **Flet**.

Se presentan cuatro tipos de gráficas:

* Barras
* Líneas
* Dispersión
* Circular

Este ejemplo corresponde a la **Unidad 2: Componentes y librerías**, específicamente al subtema **2.2 Uso de librerías**.

---

## Importación de librerías

```python
import matplotlib.pyplot as plt
import flet as ft
import base64
from io import BytesIO
import random
```

Se utilizan:

* **Matplotlib**: para generar gráficas
* **Flet**: para mostrar la interfaz
* **base64 y BytesIO**: para convertir imágenes
* **random**: para generar datos aleatorios

---

## Conversión de gráfica a imagen

```python
def fig_to_src(fig):
```

### Función:

Convierte una gráfica de Matplotlib en una imagen en formato base64 para poder mostrarla en Flet.

### Proceso:

1. Guarda la imagen en memoria
2. La convierte a base64
3. La regresa como texto compatible con Flet

---

## Funciones de gráficas

### Gráfica de barras

```python
def generar_grafica_barras():
```

Muestra ventas por producto.

---

### Gráfica de líneas

```python
def generar_grafica_lineas():
```

Muestra una tendencia de rendimiento en el tiempo.

---

### Gráfica de dispersión

```python
def generar_grafica_dispersion():
```

Genera datos aleatorios para simular sensores.

---

### Gráfica circular

```python
def generar_grafica_circular():
```

Muestra distribución por categorías.

---

## Función principal

```python
def main(page: ft.Page):
```

Configura:

* Título de la aplicación
* Tema visual

---

## Diseño de la interfaz

```python
tablero = ft.GridView(...)
```

Se utiliza un GridView para organizar las gráficas en forma de cuadrícula.

---

## Mostrar gráficas

```python
img1 = ft.Image(src=generar_grafica_barras())
```

Cada gráfica se convierte en imagen y se muestra en pantalla.

---

## Contenedores

```python
ft.Container(...)
```

Se utilizan para dar estilo:

* Bordes
* Espaciado
* Diseño visual

---

## Agregar a la página

```python
page.add(header, ft.Divider(), tablero)
```

Se agregan:

* Título
* Separador
* Cuadrícula de gráficas

---

## Ejecución del programa

```python
ft.app(target=main)
```

Inicia la aplicación.

---

## Conclusión

Este programa demuestra cómo integrar diferentes librerías para crear aplicaciones visuales completas.

Se combinan:

* Generación de datos
* Visualización gráfica
* Interfaz interactiva

Esto permite desarrollar aplicaciones más dinámicas y funcionales.

---

## Clasificación en la unidad

Este ejemplo pertenece a:

**Unidad 2: Componentes y librerías**

* 2.2 Uso de librerías (Matplotlib, Flet, random)
* 2.3 Uso de componentes visuales
