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
tiles = list(range(32)) * 2
state = {'mark': None, 'taps': 0, 'pairs': 0}
hide = [True] * 64

def square(x, y):
    "Draw white square with black outline at (x, y)."
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
    "Convert (x, y) coordinates to tiles index."
    return int((x + 240) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 240, (count // 8) * 50 - 200

def tap(x, y):
    "Update mark and hidden tiles based on tap."
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        state['pairs'] = state['pairs'] + 1
    
    state['taps'] = state['taps'] + 1

def draw():
    "Draw image and tiles."
    clear()
    goto(-40, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        num = tiles[mark]
        off_x = 3 if num > 9 else 14
        up()
        goto(x + off_x, y - 2)
        color('black')
        write(tiles[mark], font=('Monospace', 30, 'normal'))
    pairs = state['pairs']
    if pairs >= 32:
        up()
        goto(-20, 0)
        color('green')
        write('Great!! you got all the 32 pairs', font=('Arial', 20, 'normal'))
    
    up()
    goto(200, 100)
    color('black')
    write(state['taps'], font=('Monospace', 30, 'normal'))


    update()
    ontimer(draw, 100)

shuffle(tiles)
setup(500, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
