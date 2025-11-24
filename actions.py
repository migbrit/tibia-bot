import pyautogui as pg
import constants
import time
import threading
import json

# -------------- Scripts -----------------
def run_wasp_ab_script():
    with open(f'{constants.FOLDER_NAME}\\infos.json', 'r') as file:
        coordinates = json.loads(file.read())
    for coordinate in coordinates:
        kill_monster()
        pg.sleep(1)
        get_loot()
        go_to_flag(coordinate['path'], coordinate['wait'])
        if check_player_position:
            kill_monster()
            pg.sleep(1)
            get_loot()
            go_to_flag(coordinate['path'], coordinate['wait'])
        eat_food()
        down_hole(coordinate['down_hole'])
        up_hole(coordinate['up_hole'], f'{constants.FOLDER_NAME}\\anchor-floor-02.png', 420, 0)
        up_hole(coordinate['up_hole'], f'{constants.FOLDER_NAME}\\anchor-floor-03.png', 147, 120)

def run_skill_gnarlhound():
    print("Iniciando skill Gnarlhound...")
    
    # Iniciar thread do anti-AFK (agora a cada 8 minutos)
    anti_afk_thread = threading.Thread(target=anti_afk_worker, daemon=True)
    anti_afk_thread.start()
    
    print("Anti-AFK thread iniciada. Pressione Ctrl+C para parar.")
    
    # Loop principal foca apenas em skillar
    while True:
        kill_monster()
        pg.sleep(1)

def anti_afk_worker():
    print("Anti-AFK worker iniciado.")
    while True:
        time.sleep(600) 
        print("Executando anti-AFK...")
        execute_anti_afk()

# -------------- Scripts -----------------


# -------------- Functions -----------------

def execute_anti_afk():
    print("Iniciando sequência anti-AFK...")
    
    # Método 1: CTRL + Setas (mais comum)
    print("Método 1: CTRL + Setas")
    pg.keyDown('ctrl')
    time.sleep(0.2)
    pg.press('left')
    time.sleep(0.5)
    pg.press('right')
    time.sleep(0.5)
    pg.keyUp('ctrl')
    time.sleep(1)
    
    # Método 2: Apenas setas (backup)
    print("Método 2: Apenas setas")
    pg.press('up')
    time.sleep(0.3)
    pg.press('down')
    time.sleep(0.3)
    
    # Método 3: ALT + Teclas (outra opção)
    print("Método 3: ALT + Teclas")
    pg.hotkey('alt', '1')
    time.sleep(0.5)
    pg.hotkey('alt', '2')
    time.sleep(0.5)

    pg.press('o')
    time.sleep(0.5)
    
    print("Sequência anti-AFK completa!")

def battle_empty():
    return pg.locateOnScreen('imgs\\empty-battle.png', region=constants.BATTLE_REGION, confidence=0.8)

def pixelMatchesColor(position, rgb):
    x, y = position
    if pg.pixelMatchesColor(x, y, rgb): 
        return True
    return False
  
def kill_monster(): 
    while battle_empty() == None:
        pg.press('l')
        print('monstro alvejado.')  
        x, y = constants.POSITION_MONSTER_TARGET                         
        while pg.pixelMatchesColor(x, y, constants.RED_TARGET_COLOR, tolerance=99): 
            pg.sleep(1)
            print('esperando monstro morrer...')
        print('procurando outro monstro...')

def go_to_flag(path, wait):
    flag = pg.locateOnScreen(path, region=constants.MINI_MAP_REGION, confidence=0.8)
    print('going to... ', path)
    if flag:
        x, y = pg.center(flag)
        pg.moveTo(x, y)
        pg.click()
        pg.sleep(wait)

def check_player_position():
    return pg.locateOnScreen('imgs\\point-player.png', region=constants.MINI_MAP_REGION, confidence=0.8)

def get_loot():
    pg.hotkey("alt","q")

def check_status(name, delay, position, rgb, button):
    print(f'checando {name}...')
    pg.sleep(delay)
    x, y = position
    if pg.pixelMatchesColor(x, y, rgb):
        pg.press(button)

def eat_food():
    print('comendo food...')
    pg.press('9')

def down_hole(should_down):
    if should_down:
        box = pg.locateOnScreen('imgs\\hole-down.png', region=constants.GAME_ACTION_REGION, confidence=0.8)
        if box:
            x, y = pg.center(box)
            pg.moveTo(x, y)
            pg.click()
            pg.sleep(2)

def up_hole(should_up, anchor, plus_x, plux_y):
    if should_up:
        box = pg.locateOnScreen(anchor, region=constants.GAME_ACTION_REGION, confidence=0.8)
        if box:
            x, y = pg.center(box)
            pg.moveTo(x + plus_x, y + plux_y)
            pg.press('F12')
            pg.click()
# -------------- Functions -----------------