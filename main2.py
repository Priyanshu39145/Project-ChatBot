import pyautogui
import pyperclip
import openai


import time

# Code for finding position
# while(True):
#     a = pyautogui.position()
#     print(a)
    
pyautogui.click(1178,1041)
time.sleep(2)

def copy():
    

    pyautogui.moveTo(1216,826)
    pyautogui.rightClick(1216,826)
    time.sleep(1)
    pyautogui.moveTo(1259,917)
    pyautogui.click(1259,917)
    time.sleep(1)

    text = pyperclip.paste()
    return text

def paste(str):
    pyperclip.copy("Niggggerrrrr")
    pyautogui.moveTo(1194,955)
    pyautogui.rightClick(1194,955)
    time.sleep(1)
    pyautogui.click(1241,876)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    
# while True:
#     pyautogui.scroll(-5000, x=1440, y=497)
#     c = copy()
    
#    

#     response = openai.ChatCompletion.create(
#     model="gpt-3.5-turbo",  # specify your model here
#     messages=[
#         {"role": "You are an AI. You will talk with another AI. Have a nice conversation", "content": c}
#     ]
# )


#     print(response['choices'][0]['message']['content'])

#     # paste(p)
#     time.sleep(5)

for i in range(1,100):
    paste(i)
    