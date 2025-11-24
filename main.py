import pyautogui as pg
import actions
import keyboard
import constants
import json

#Abrir OBS                    
#Deixar OBS em modo janela grande
#Rodar window.py para diminuir opacidade do Tibia
#Rodar o main.py

pg.useImageNotFoundException(False)

def run():
    actions.run_skill_gnarlhound()

keyboard.wait('h')
while True:
    run()


     