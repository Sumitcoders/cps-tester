from ursina import *
import threading

app = Ursina()
def update():
    print(x)
global x
x = 0
def timer():
    global button
    time.sleep(5)
    destroy(button)
    time.sleep(2)
    score = str(x / 5) + str(' Clicks per second')
    score = Button(model = 'quad', scale=(1,0.5), text = score)
def a():
    global x
    global button
    if x == 0:
        t = threading.Thread(target=timer)
        t.start()
    x += 1
    destroy(button)
    button = Button(model='quad', scale = (1,0.5), text = str(x))
    button.on_click = a 
    button.tooltip = Tooltip('Click Me')
    
    
button = Button(model='quad', scale = (1,0.5), text = str(x))
button.on_click = a
button.tooltip = Tooltip('Click Me')

app.run()