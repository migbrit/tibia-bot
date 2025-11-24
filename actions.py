import pyautogui as pg
import constants

def battle_empty():
    return pg.locateOnScreen('imgs\\empty-battle.png', grayscale=True, confidence=0.8)

def pixelMatchesColor(position, rgb):
    x, y = position
    if pg.pixelMatchesColor(x, y, rgb): 
        return True
    return False

def is_monster_losing_hp(pixel_pos, previous_color):
    current_color = pg.pixel(*pixel_pos)
    return current_color != previous_color
  
def is_monster_targeted():
    r, g, b = pg.pixel(*constants.POSITION_MONSTER_TARGET)
    return r > 150 and g < 100 and b < 100 # Monster targeted when this pixel is red

def kill_monster(): 
    while battle_empty() is None:
        if not is_monster_targeted():
            pg.press('space')
            print('monster targeted.')  

        while is_monster_targeted(): 
            color = pg.pixel(*constants.POSITION_MONSTER_HP)
            print('waiting monster to die...')
            get_loot()
            pg.sleep(2)
            if not is_monster_losing_hp(constants.POSITION_MONSTER_HP, color):
                pg.press('space')

        print('searching another monster...')

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
        print('anchor -> ', box)
        if box:
            x, y = pg.center(box)
            pg.moveTo(x + plus_x, y + plux_y)
            pg.press('F12')
            pg.click()
