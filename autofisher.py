import pyautogui
import time
import keyboard

level = int(input("Input your Fishing skill level (1-5): ")[0])
toss_time = 1.0
if level == 1:
    toss_time = 1.1
elif level == 2:
    toss_time = 1.307
elif level == 3:
    toss_time = 1.5
elif level == 4:
    toss_time = 1.7
elif level == 5:
    toss_time = 1.9

screen_size = pyautogui.size()

# TODO: Add support for different resolutions.. somehow
x = int(screen_size.width / 2 + 380) # 1340
y = int(screen_size.height / 2 + 400) # 940

print("Gotcha! Please open Unturned and make sure a bob is already in the water. Press \"p\" to toggle pause.")
time.sleep(5)
last_color = (0,0,0)

start_time = time.time()  # start timer
fishcount = 0
paused = False
p_pressed = False
while(True):
    if not paused:
        current_color = pyautogui.pixel(x,y) # read color at pixel at location
        print(f"\rElapsed Time: {round(time.time() - start_time, 2)}", end="")
        # check for drastic change in color of pixel at location
        if (abs(last_color[0] - current_color[0]) > 5 or abs(last_color[1] - current_color[1]) > 5 or abs(last_color[2] - current_color[2]) > 5) and last_color != (0, 0, 0):
            fishcount += 1
            print(f"\n𓆝 𓆟 𓆞 𓆝 𓆟FISHHHHHHHHHHHHHH {fishcount}!!!!!!!𓆝 𓆟 𓆞 𓆝 𓆟")
            
            pyautogui.click(button='left') # reel in fish

            time.sleep(3)
            
            # throw rod out again
            pyautogui.mouseDown()
            time.sleep(toss_time)
            pyautogui.mouseUp()
            
            start_time = time.time() # reset timer
            last_color = (0,0,0) 
            time.sleep(2)
        else:
            last_color = current_color

    # check for the "p" keypress to toggle pause
    if keyboard.is_pressed("p"):
        if not p_pressed:
            paused = not paused
            p_pressed = True
            if paused:
                print("\nPaused. Press 'p' again to resume.")
            else:
                print("Resumed.")
    else:
        p_pressed = False  # reset the flag when "p" key is released, ensures that one keydown = one pause/unpause
