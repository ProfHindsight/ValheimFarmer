import pynput
import keyboard
import time

def plant(mouse:pynput.mouse.Controller):
    mouse.press(pynput.mouse.Button.left)
    time.sleep(0.1)
    mouse.release(pynput.mouse.Button.left)

def press_key(keyboard:pynput.keyboard.Controller, key:str, move_time:float):
    keyboard.press(key)
    time.sleep(move_time)
    keyboard.release(key)

def right(keyboard:pynput.keyboard.Controller, move_time:float):
    press_key(keyboard, 'd', move_time)

def left(keyboard:pynput.keyboard.Controller, move_time:float):
    press_key(keyboard, 'a', move_time)

def down(keyboard:pynput.keyboard.Controller, move_time:float):
    press_key(keyboard, 's', move_time)

def up(keyboard:pynput.keyboard.Controller, move_time:float):
    press_key(keyboard, 'w', move_time)

def plant_row(pyn_keyboard:pynput.keyboard.Controller, pyn_mouse:pynput.mouse.Controller, numcols:int, direction:str, move_time:float, wait_time:float):
    for i in range(numcols):
        start_time = time.time()
        plant(pyn_mouse)
        if i != numcols - 1:
            if (direction == "right"):
                right(pyn_keyboard, move_time)
            elif (direction == "left"):
                left(pyn_keyboard, move_time)
            time.sleep(wait_time - (time.time() - start_time))

        # Check if user wants to stop by pressing 'n'
        if keyboard.is_pressed('n'):
            print(f"Stopping valfarmer!")
            return False
        
    return True

def plant_field(pyn_keyboard:pynput.keyboard.Controller, pyn_mouse:pynput.mouse.Controller, numrows:int, numcols:int, move_time:float, wait_time:float):
    current_direction = "left"
    for i in range(numrows):
        if (current_direction == "right"):
            if not plant_row(pyn_keyboard, pyn_mouse, numcols, "right", move_time, wait_time):
                return
            # Move half duration to the right
            right(pyn_keyboard, move_time/2)
            current_direction = "left"
        elif (current_direction == "left"):
            if not plant_row(pyn_keyboard, pyn_mouse, numcols, "left", move_time, wait_time):
                return
            # Move half duration to the left
            left(pyn_keyboard, move_time/2)
            current_direction = "right"

        time.sleep(move_time)
        # Move down
        down(pyn_keyboard, move_time*0.9)
        time.sleep(wait_time)

        # Check if user wants to stop by pressing 'n'
        if keyboard.is_pressed('n'):
            print(f"Stopping valfarmer!")
            return

def main():
    keyboard = pynput.keyboard.Controller()
    mouse = pynput.mouse.Controller()
    print(f"Starting valfarmer!")
    for i in range(3, 0, -1):
        print(f"{i}")
        time.sleep(1)
    
    print(f"Press and hold 'n' to stop valfarmer!")
    
    # Plant field
    numrows = 12
    numcols = 17
    move_time = 0.35
    wait_time = 1.7
    plant_field(keyboard, mouse, numrows, numcols, move_time, wait_time)
    print(f"Finished valfarmer!")

if __name__ == "__main__":
    main()