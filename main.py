import pgzrun
from pgzhelper import *


WIDTH = 900
HEIGHT = 700
run_imgs = ['zombie/run/tile002', 'zombie/run/tile003',
           'zombie/run/tile004', 'zombie/run/tile005']

run_igs = ['wizard/run/tile000','wizard/run/tile001','wizard/run/tile002','wizard/run/tile003','wizard/run/tile004','wizard/run/tile005','wizard/run/tile006','wizard/run/tile007']

attack_imgs = ['wizard/attack/tile000','wizard/attack/tile001','wizard/attack/tile002','wizard/attack/tile003','wizard/attack/tile004','wizard/attack/tile005','wizard/attack/tile006','wizard/attack/tile007']
fire_imgs= 
zombie = Actor(run_imgs[0])
wizard = Actor(run_igs[0])

zombie.images = run_imgs
wizard.images = run_igs

zombie.scale = 6
zombie.right=WIDTH
zombie.bottom = HEIGHT -10
zombie.fps = 10

wizard.scale = 2
wizard.left= -10 
wizard.bottom = HEIGHT + 90
wizard.fps = 10

question = "type to attack"
typed=""

def on_key_down(key):
    global typed
    print(f'keycode:{key}')

    if key == keys.SPACE or key in range(97,123):
        typed +=chr(key)
        if typed == question:
                typed=""
                wizard.images = attack_imgs
    elif key == keys.BACKSPACE:
            typed =typed[0:-1]
attacks=[]

def update():

    zombie.animate()
    wizard.animate()
    if wizard.image == attack_imgs[-1]:
         wizard.images = run_igs
def draw():
    screen.clear()
    zombie.draw()
    wizard.draw()
    screen.draw.text(question,(WIDTH/3,HEIGHT/10),color="white", fontsize=60)
    screen.draw.text(typed,(WIDTH/3,HEIGHT/10),color="orange", fontsize=60)

pgzrun.go()

