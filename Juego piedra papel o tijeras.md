# Ejemplo: Juego Piedra, Papel o Tijeras con Flet

## Descripción general

Este programa implementa el juego de **Piedra, Papel o Tijeras** utilizando Python y la librería **Flet** para crear una interfaz gráfica interactiva.

El usuario puede seleccionar una opción, competir contra la computadora y ver el puntaje actualizado en tiempo real.

Este ejemplo corresponde a la **Unidad 2: Componentes y librerías**, específicamente a:

* 2.2 Uso de librerías
* 2.3 Uso de componentes visuales

---

## Importación de librerías

```python
import flet as ft
import random
```

Se utilizan:

* **Flet**: para crear la interfaz gráfica
* **random**: para generar la elección aleatoria de la computadora

---

## Variables globales

```python
opciones = ["Piedra", "Papel", "Tijeras"]
```

Contiene las posibles elecciones del juego.

---

## Función principal

```python
def main(page: ft.Page):
```

Es el punto de entrada de la aplicación.

### Configuración de la ventana:

* Título
* Tamaño
* Alineación de los elementos

---

## Manejo de puntaje

```python
puntaje = {
    "jugador": 0,
    "computadora": 0
}
```

Se utiliza un diccionario para almacenar el puntaje sin necesidad de variables globales.

---

## Componentes de interfaz

### Título

```python
titulo = ft.Text(...)
```

Muestra el nombre del juego.

---

### Texto de resultado

```python
resultado_texto = ft.Text(...)
```

Muestra el resultado de cada partida.

---

### Texto de puntaje

```python
puntaje_texto = ft.Text(...)
```

Muestra el marcador actualizado.

---

## Función jugar

```python
def jugar(eleccion_jugador):
```

### Función:

* Genera la elección de la computadora
* Compara resultados
* Actualiza el puntaje
* Muestra el resultado en pantalla

Utiliza estructuras condicionales para determinar si el jugador gana, pierde o empata.

---

## Función reiniciar

```python
def reiniciar(e):
```

### Función:

* Reinicia el puntaje a cero
* Restablece los textos iniciales

---

## Función salir

```python
def salir(e):
```

### Función:

* Limpia la pantalla
* Muestra un mensaje de despedida

---

## Botones

```python
ft.ElevatedButton(...)
```

Se crean botones para:

* Piedra
* Papel
* Tijeras
* Reiniciar juego
* Salir

Cada botón ejecuta una función al hacer clic.

---

## Diseño de la interfaz

```python
page.add(
    ft.Column([...])
)
```

Se organiza la interfaz en una columna con:

* Título
* Resultado
* Puntaje
* Botones

---

## Ejecución del programa

```python
ft.app(target=main)
```

Inicia la aplicación y muestra la interfaz gráfica.

---

## Conclusión

Este programa demuestra el uso de librerías y componentes visuales para crear una aplicación interactiva.

Se aplican conceptos como:

* Eventos (botones)
* Actualización de interfaz
* Lógica de control

Esto permite desarrollar aplicaciones dinámicas y fáciles de usar.

---

