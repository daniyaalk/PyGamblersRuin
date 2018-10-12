import random

(x, y) = (100, 100)
pointer = 0

n = 0

while abs(pointer) != 100:

    step = random.choice([-1, +1])
    if step == +1:
        print("x wins", n, end='')
    else:
        print("y wins", n, end='')
    pointer = pointer + step
    (x, y) = (x+step, y-step)

    print("(x, y) =", (x,y))
    n += 1
