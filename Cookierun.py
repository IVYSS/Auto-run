import pyautogui
import time
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def play():
    start_button_location = pyautogui.locateCenterOnScreen('C:/Users/iiii/Desktop/Autorun/start_btn.png', confidence=0.6)
    if start_button_location is not None:
        print(f"✅ Found start button: {start_button_location}")
        pyautogui.click(start_button_location)    
        time.sleep(3)
    return start_button_location


def randomBoots():
    random_boots_btn = pyautogui.locateCenterOnScreen('C:/Users/iiii/Desktop/Autorun/random_boots.png', confidence=0.6)
    if random_boots_btn is not None:
        pyautogui.click(random_boots_btn)
    time.sleep(2)

    small_random_boots_btn = pyautogui.locateCenterOnScreen('C:/Users/iiii/Desktop/Autorun/small_random_boots.png' , confidence=0.8)
    if (small_random_boots_btn is not None):
        print(f"✅ Found small random boots button: {small_random_boots_btn}")
        pyautogui.click(small_random_boots_btn)

        time.sleep(2)

        multi_buy_btn = pyautogui.locateCenterOnScreen('C:/Users/iiii/Desktop/Autorun/multi_buy.png' , confidence=0.8)
        if (multi_buy_btn  is not None):
            print(f"✅ Found multi buy button: {multi_buy_btn}")
            pyautogui.click(multi_buy_btn)

    time.sleep(30)

    double_coins_text_box = pyautogui.locateCenterOnScreen('C:/Users/iiii/Desktop/Autorun/double_coins_text.png' , confidence=0.8)
    if double_coins_text_box is not None:
        print(f"✅ Found double coins text box: {double_coins_text_box}")
        play()
        return True

    else:
        print("❌ Double coins text box not found")
        play()
        return True


def second_run():
    second_run_btn = pyautogui.locateCenterOnScreen('C:/Users/iiii/Desktop/Autorun/second_run.png' , confidence=0.8)
    if second_run_btn is not None:
        print(f"✅ Found second run button: {second_run_btn}")
        pyautogui.click(second_run_btn)
    time.sleep(15)

    submit_btn = pyautogui.locateCenterOnScreen('C:/Users/iiii/Desktop/Autorun/submit.png' , confidence=0.8)
    if (submit_btn is not None):
        print(f"✅ Found ok button: {submit_btn}")
        pyautogui.click(submit_btn)
    time.sleep(2)


    open_all_btn = pyautogui.locateCenterOnScreen('C:/Users/iiii/Desktop/Autorun/open_all.png' , confidence=0.8)
    if (open_all_btn is not None):
        print(f"✅ Found open all button: {open_all_btn}")
        pyautogui.click(open_all_btn)

    time.sleep(2)

    confirm_btn = pyautogui.locateCenterOnScreen('C:/Users/iiii/Desktop/Autorun/confirm.png' , confidence=0.8)
    if (confirm_btn is not None):
        print(f"✅ Found confirm button: {confirm_btn}")
        pyautogui.click(confirm_btn)

    time.sleep(2)



def main():
    for i in range(10):
        play()
        time.sleep(3)
        randomBoots()
        time.sleep(202)
        second_run()
        time.sleep(3)
        

if __name__ == "__main__":
    main()

