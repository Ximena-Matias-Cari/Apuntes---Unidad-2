# Ejemplo: Catálogo de productos con componentes reutilizables

## Descripción general

Este programa simula una tienda en línea utilizando Python y la librería **Flet**, donde se muestra un catálogo de productos en forma de tarjetas visuales.

Cada producto se representa mediante un componente reutilizable, permitiendo una estructura organizada y escalable.

Este ejemplo corresponde a la **Unidad 2: Componentes y librerías**, específicamente a:

* 2.2 Uso de librerías
* 2.3 Creación de componentes definidos por el usuario
* 2.4 Organización tipo paquete

---

## Importación de librería

```python
import flet as ft
```

Se utiliza Flet para crear la interfaz gráfica del catálogo.

---

## Datos de productos

```python
productos = [
    {"id":1,"nombre":"Laptop Gamer","descripcion":"Laptop con alto rendimiento","precio":25000,"ruta_imagen":"laptop.jpg"},
    ...
]
```

### Función:

Almacenar la información de los productos en una lista de diccionarios.

Cada producto contiene:

* ID
* Nombre
* Descripción
* Precio
* Imagen

---

## Clase TarjetaProducto (Componente visual)

```python
class TarjetaProducto(ft.Container):
```

Esta clase define un **componente visual reutilizable** para mostrar cada producto.

---

## Constructor

```python
def __init__(self, producto):
```

Recibe un diccionario con la información del producto.

---

## Diseño del componente

```python
self.content = ft.Column(
    controls=[ ... ]
)
```

Se construye una tarjeta con:

* Imagen del producto
* Nombre
* Descripción
* Precio
* Botones de interacción

---

## Imagen del producto

```python
ft.Image(
    src=producto["ruta_imagen"],
    width=230,
    height=150,
    fit="cover"
)
```

Muestra la imagen del producto desde la carpeta de recursos.

---

## Información del producto

```python
ft.Text(producto["nombre"], ...)
ft.Text(producto["descripcion"], ...)
ft.Text(f"${producto['precio']}", ...)
```

Se muestran los datos principales del producto.

---

## Botones

```python
ft.Row(
    controls=[
        ft.IconButton(icon=ft.Icons.FAVORITE_BORDER),
        ft.ElevatedButton("Agregar al carrito")
    ]
)
```

Se incluyen botones para:

* Marcar como favorito
* Agregar al carrito (simulado)

---

## Aplicación principal

```python
def main(page: ft.Page):
```

Configura:

* Título
* Color de fondo
* Scroll automático

---

## Creación de componentes

```python
tarjetas = []

for producto in productos:
    tarjetas.append(TarjetaProducto(producto))
```

Se generan múltiples tarjetas reutilizando el mismo componente.

---

## Diseño responsivo

```python
ft.ResponsiveRow(
    controls=tarjetas
)
```

Permite que las tarjetas se acomoden automáticamente según el tamaño de la pantalla.

---

## Agregar elementos a la página

```python
page.add(
    ft.Text("TechStore", ...),
    ft.Text("Catálogo de productos", ...),
    ft.ResponsiveRow(...)
)
```

Se agregan:

* Título
* Subtítulo
* Catálogo de productos

---

## Ejecución del programa

```python
ft.app(target=main, assets_dir="assets")
```

Inicia la aplicación y permite cargar imágenes desde la carpeta **assets**.

---
<img width="1890" height="1070" alt="image" src="https://github.com/user-attachments/assets/5d71ab59-1e28-4e42-a167-e46fa63de823" />
<img width="1872" height="1060" alt="image" src="https://github.com/user-attachments/assets/b39c817e-f619-4acb-932e-f4bada68ca8f" />


## Conclusión

Este programa demuestra cómo crear componentes reutilizables para construir interfaces complejas.

Se aplican conceptos como:

* Reutilización de código
* Separación de datos y vista
* Diseño responsivo

Esto facilita:

* Escalabilidad del proyecto
* Organización del código
* Desarrollo de aplicaciones reales

---

## Clasificación en la unidad

Este ejemplo pertenece a:

**Unidad 2: Componentes y librerías**

* 2.2 Uso de librerías (Flet)
* 2.3 Creación de componentes definidos por el usuario
* 2.4 Organización del código en estructuras reutilizables
