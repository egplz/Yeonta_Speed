'''
레밀리아 연타 속도 측정 프로그램
초당 입력 수에 따라 레밀님 얼굴 바뀜
'''
import os
import tkinter as tk
import time
from PIL import Image, ImageTk

# 기본 변수 설정
times = []
# effect = []
current_state = 1
state = 1

# kps 계산
def press(event):
    now = time.time()

    times.append(now)

    while times and now - times[0] > 1:
        times.pop(0)

    kps = len(times)

    label.config(text=f"{kps} KPS")

    change_image(kps)

# def update_effect():

# 이미지 바꾸기
def change_image(kps):

    global current_state
    global state

    if kps == 7:
        state = 2
    
    if kps == 8:
        state = 3
    
    if kps == 9:
        state = 4
    
    if kps == 10:
        state = 5
    
    elif kps <= 6:
        state = 1
    
    if state != current_state:
        
        current_state = state

        canvas.itemconfig(
            change,
            image= images[current_state-1]
        )

root = tk.Tk()

# 기본 이미지 설정
images = []

for file in os.listdir("assets"):
    if file.endswith(".png"):
        path = os.path.join("assets", file)

        img = Image.open(path)
        img = ImageTk.PhotoImage(img)

        images.append(img)

photo = images[0]

canvas = tk.Canvas(root)
canvas.pack(fill= "both", expand=True)

change = canvas.create_image(
    0, 0,
    image=photo,
    anchor="nw"
)

label = tk.Label(root, text="0 KPS", font=("Arial", 40))
label.pack()

root.bind("<space>", press)

root.mainloop()