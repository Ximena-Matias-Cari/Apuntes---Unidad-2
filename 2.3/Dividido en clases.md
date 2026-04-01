# Ejemplo: Componentes definidos por el usuario con Flet

## Descripción general

Este programa fue desarrollado en Python utilizando la librería **Flet**, la cual permite crear interfaces gráficas modernas.

El objetivo del código es mostrar una lista de usuarios mediante tarjetas visuales, aplicando el uso de clases para dividir el programa en componentes reutilizables.

Este ejemplo corresponde a la **Unidad 2: Componentes y librerías**, específicamente al tema **2.3 Creación de componentes definidos por el usuario**.

---

## Importación de librería

```python
import flet as ft
```

Se importa la librería Flet, la cual proporciona los elementos necesarios para construir la interfaz gráfica, como textos, botones, contenedores y diseño de la página.

---

## Clase Usuario (Componente no visual)

```python
class Usuario:
    def __init__(self, nombre, rol, color_borde=ft.Colors.BLUE):
        self.nombre = nombre
        self.rol = rol
        self.color_borde = color_borde
```

Esta clase representa un **componente no visual**, ya que solo almacena datos.

### Función:

Guardar la información de cada usuario.

### Atributos:

* `nombre`: Nombre del usuario
* `rol`: Puesto o función del usuario
* `color_borde`: Color del borde de la tarjeta (por defecto azul)

---

## Clase TarjetaPerfil (Componente visual)

```python
class TarjetaPerfil(ft.Container):
```

Esta clase representa un **componente visual personalizado**, ya que hereda de `Container` de Flet.

### Función:

Mostrar la información del usuario en forma de tarjeta dentro de la interfaz.

---

### Constructor

```python
def __init__(self, usuario, pagina):
```

Recibe:

* `usuario`: objeto de la clase Usuario
* `pagina`: referencia a la página donde se mostrará el contenido

---

### Contenido de la tarjeta

```python
self.content = ft.Column(
    controls=[
        ft.Text(usuario.nombre, weight=ft.FontWeight.BOLD, size=20),
        ft.Text(usuario.rol, italic=True),
        ft.ElevatedButton("Ver perfil", on_click=self.saludar)
    ],
    tight=True
)
```

Se crea una columna que contiene:

* El nombre del usuario (en negritas)
* El rol del usuario (en cursiva)
* Un botón para interactuar

---

### Estilo de la tarjeta

```python
self.border = ft.border.all(2, usuario.color_borde)
self.padding = 10
self.border_radius = 10
self.width = 200
```

Se define la apariencia del componente:

* Borde con color personalizado
* Espaciado interno (padding)
* Bordes redondeados
* Tamaño fijo

---

### Método saludar

```python
def saludar(self, e):
    print(f"Interactuando con {self.usuario.nombre}")
```

### Función:

Se ejecuta cuando el usuario presiona el botón.

Muestra en consola un mensaje indicando con qué usuario se está interactuando.

---

## Clase App (Control principal)

```python
class App:
```

Esta clase controla el funcionamiento general de la aplicación.

---

### Constructor

```python
def __init__(self, page: ft.Page):
```

Configura la página principal:

* Título de la aplicación
* Alineación de los elementos

---

### Método iniciar

```python
def iniciar(self):
```

### Función:

* Crear objetos de tipo Usuario
* Crear tarjetas de perfil
* Agregar los elementos a la interfaz

---

### Creación de usuarios

```python
usuario1 = Usuario("Ana Garcia", "Desarrolladora Senior", ft.Colors.PURPLE)
usuario2 = Usuario("Carlos Ruiz", "Arquitecto de Software", ft.Colors.PINK)
```

Se crean dos usuarios con diferente información.

---

### Creación de tarjetas

```python
tarjeta1 = TarjetaPerfil(usuario1, self.page)
tarjeta2 = TarjetaPerfil(usuario2, self.page)
```

Cada usuario se representa mediante una tarjeta visual.

---

### Agregar elementos a la página

```python
self.page.add(
    ft.Text("Lista de Usuarios", size=30, weight="bold"),
    ft.Row([tarjeta1, tarjeta2], alignment=ft.MainAxisAlignment.CENTER)
)
```

Se agregan:

* Un título
* Las tarjetas organizadas en fila

---

## Función principal

```python
def main(page: ft.Page):
    App(page)

ft.app(target=main)
```

### Función:

Es el punto de entrada del programa.

Se encarga de iniciar la aplicación y mostrar la interfaz en pantalla.

---

## Conclusión

Este programa demuestra el uso de componentes definidos por el usuario mediante clases en Python.

Se separa la lógica en:

* Componentes no visuales (Usuario)
* Componentes visuales (TarjetaPerfil)

Esto permite:

* Mejor organización del código
* Reutilización de componentes
* Mayor facilidad de mantenimiento

---

---
