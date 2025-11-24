import pyautogui as pg
import time

print("Passe o mouse sobre o pixel desejado... (CTRL+C para sair)")
time.sleep(2)

try:
    while True:
        x, y = pg.position()
        r, g, b = pg.screenshot().getpixel((x, y))
        print(f"Pos: ({x}, {y})  Cor: ({r}, {g}, {b})", end="\r")
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nFinalizado.")
