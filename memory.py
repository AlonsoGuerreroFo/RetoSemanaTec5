"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.
"""

from random import *
from turtle import *

from freegames import path

car = path('car.gif')
tiles = tiles = ['★', '☆', '♡', '♢', '♧', '♤', '✓', '✕', '☯', '☸', '☮', '♨', '✈', '♔', '♕', '♖', '♗', '♘', '♙', '☀', '☁', '❀', '✿', '☂', '☃', '♚', '♛', '♜', '♝', '♞', '♟', '☹'] * 2
state = {'mark': None}
hide = [True] * 64
state = {'mark': None, 'taps': 0}  # Añadir contador de taps aquí

def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    spot = index(x, y)
    mark = state['mark']
    state['taps'] += 1  # Incrementar contador de taps

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None


def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 26, y - 6)
        color('purple')
        write(tiles[mark], align = "center", font=('Arial', 35, 'normal'))

    # Muestra el número de taps en la esquina superior derecha
    goto(160, 160)  # Ajusta la posición según sea necesario
    color('black')
    write(f"Taps: {state['taps']}", font=('Arial', 20, 'normal'))

    # Comprobar si todos los cuadros están descubiertos
    if all(not h for h in hide):
        # Todos los cuadros han sido destapados
        goto(-100, 0)  # Ajusta la posición según sea necesario para el mensaje
        color('green')
        write("¡Todos los cuadros descubiertos!", font=('Arial', 20, 'bold'))

    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
