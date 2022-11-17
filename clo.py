from datetime import *
from time import sleep
import pyglet
y = input('int time like 12:32: ').split(':')
y[1]= int(y[1])
y[0]= int(y[0])
while datetime.now().time().hour != y[0] or y[1] != datetime.now().time().minute:
    sleep(0.1)
print('asidasodwkalfkajofjfisgo;lsdgnhsidogh')
sound = pyglet.media.load('m.mp3', streaming=False)
sound.play()
pyglet.app.run()


