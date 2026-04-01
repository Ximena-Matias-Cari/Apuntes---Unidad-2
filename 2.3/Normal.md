# Ejemplo: Componente personalizado con Flet

## Descripción general

Este programa fue desarrollado en Python utilizando la librería **Flet**. Su objetivo es crear un componente visual reutilizable que represente una tarjeta de perfil de usuario.

Este ejemplo corresponde a la **Unidad 2: Componentes y librerías**, específicamente al subtema **2.3 Creación de componentes definidos por el usuario**.

---

## Importación de librería

```python
import flet as ft
```

Se importa la librería Flet, que permite crear interfaces gráficas mediante componentes como textos, botones y contenedores.

---

## Clase TarjetaPerfil (Componente visual)

```python
class TarjetaPerfil(ft.Container):
```

Esta clase define un **componente visual personalizado**, ya que hereda de `Container` de Flet.

### Función:

Representar una tarjeta que muestra información de un usuario.

---

## Constructor

```python
def __init__(self, nombre, rol, color_borde=ft.Colors.BLUE):
```

Recibe:

* `nombre`: nombre del usuario
* `rol`: puesto del usuario
* `color_borde`: color del borde (por defecto azul)

---

## Contenido del componente

```python
self.content = ft.Column(
    controls=[
        ft.Text(nombre, weight=ft.FontWeight.BOLD, size=20),
        ft.Text(rol, italic=True),
        ft.ElevatedButton("Ver Perfil", on_click=self.saludar)
    ],
    tight=True
)
```

Se crea una columna que contiene:

* Nombre del usuario en negritas
* Rol en cursiva
* Un botón para interactuar

---

## Estilo del componente

```python
self.border = ft.border.all(2, color_borde)
self.padding = 10
self.border_radius = 10
self.width = 200
```

Se personaliza la apariencia de la tarjeta:

* Borde con color
* Espaciado interno
* Bordes redondeados
* Tamaño fijo

---

## Método saludar

```python
def saludar(self, e):
    print(f"Interactuando con el componente de {self.content.controls[0].value}")
```

### Función:

Se ejecuta cuando se presiona el botón.

Muestra en consola el nombre del usuario con el que se interactúa.

---

## Función principal

```python
def main(page: ft.Page):
```

Configura la página principal:

* Título
* Alineación de los elementos

---

## Creación de componentes

```python
usuariol = TarjetaPerfil("Ana Garcia", "Desarrolladora Senior", ft.Colors.GREEN)
usuario2 = TarjetaPerfil("Carlos Ruiz", "Arquitecto de Software")
```

Se crean dos instancias del componente `TarjetaPerfil`, demostrando su reutilización.

---

## Agregar elementos a la interfaz

```python
page.add(
    ft.Text("Lista de Usuarios", size=30, weight="bold"),
    ft.Row([usuariol, usuario2], alignment=ft.MainAxisAlignment.CENTER)
)
```

Se agregan:

* Un título
* Las tarjetas organizadas en fila

---

## Ejecución del programa

```python
ft.app(target=main)
```

Inicia la aplicación y muestra la interfaz gráfica.

---

## Conclusión

Este programa demuestra cómo crear y reutilizar componentes visuales personalizados en Python utilizando Flet.

Esto permite:

* Reutilizar código
* Mejorar la organización
* Facilitar el mantenimiento del programa

--
