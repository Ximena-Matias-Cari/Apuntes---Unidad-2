# Ejemplo: Uso de dataclass para componentes en Flet

## Descripción general

Este programa fue desarrollado en Python utilizando la librería **Flet** y el decorador **dataclass**.

El objetivo es crear un componente de tipo tarjeta de perfil utilizando una estructura más simple y organizada para almacenar datos.

Este ejemplo corresponde a la **Unidad 2: Componentes y librerías**, específicamente a:

* 2.2 Uso de librerías
* 2.3 Creación de componentes definidos por el usuario

---

## Importación de librerías

```python
import flet as ft
from dataclasses import dataclass
```

Se importan:

* **Flet**: para la interfaz gráfica
* **dataclass**: para simplificar la creación de clases que almacenan datos

---

## Uso de @dataclass

```python
@dataclass
class TarjetaPerfil:
```

El decorador `@dataclass` permite crear clases automáticamente con constructor, evitando escribir código repetitivo.

---

## Atributos de la clase

```python
nombre : str
rol : str
color_borde : str = ft.Colors.BLUE
```

### Función:

Definir la información del componente.

* `nombre`: nombre del usuario
* `rol`: puesto del usuario
* `color_borde`: color del borde (valor por defecto azul)

---

## Método build (Componente visual)

```python
def build(self):
```

### Función:

Construir el componente visual que se mostrará en la interfaz.

---

## Contenido del componente

```python
ft.Column(
    controls=[
        ft.Text(self.nombre, weight=ft.FontWeight.BOLD, size=20),
        ft.Text(self.rol, italic=True),
        ft.ElevatedButton("Ver perfil", on_click=self.saludar)
    ],
    tight=True
)
```

Se crea una columna con:

* Nombre del usuario
* Rol
* Botón de interacción

---

## Estilo del componente

```python
border=ft.border.all(2, self.color_borde),
padding=10,
border_radius=10,
width=200
```

Se define la apariencia de la tarjeta:

* Borde con color
* Espaciado interno
* Bordes redondeados
* Tamaño fijo

---

## Método saludar

```python
def saludar(self, e):
    print(f"Interactuando con {self.nombre}")
```

### Función:

Se ejecuta cuando se presiona el botón y muestra un mensaje en consola.

---

## Función principal

```python
def main(page: ft.Page):
```

Configura la aplicación:

* Título de la página
* Alineación de elementos

---

## Creación de componentes

```python
usuario1 = TarjetaPerfil("Ana García", "Desarrolladora senior", ft.Colors.GREEN)
usuario2 = TarjetaPerfil("Carlos Ruiz", "Arquitecto de Software")
```

Se crean dos instancias del componente utilizando dataclass.

---

## Renderizado en pantalla

```python
page.add(
    ft.Text("Lista de usuarios", size=30, weight="bold"),
    ft.Row([usuario1.build(), usuario2.build()], alignment=ft.MainAxisAlignment.CENTER)
)
```

Se agregan los componentes a la interfaz.

---

## Ejecución del programa

```python
ft.app(target=main)
```

Inicia la aplicación y muestra la interfaz gráfica.

---

## Conclusión

El uso de `@dataclass` permite simplificar la creación de componentes no visuales, facilitando la organización del código.

Además, al combinarlo con Flet, se logra separar:

* La estructura de datos (dataclass)
* La interfaz visual (método build)

Esto mejora:

* La claridad del código
* La reutilización
* El mantenimiento

---
