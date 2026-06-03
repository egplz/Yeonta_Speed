'''
레밀리아 연타 속도 측정 프로그램
초당 입력 수에 따라 레밀님 얼굴 바뀜
'''
import tkinter as tk
import time
from PIL import Image, ImageTk

# 기본 변수 설정
times = []
# effect = []
current_state = 1

# 기본 이미지 설정


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

    if kps >= 7:
        state = 2
    if state != current_state:
        
        current_state = state

        canvas.itemconfig(
            image=

        )
    

root = tk.Tk()

img = Image.open("level1.png")
img = img.resize((800,600))
photo = ImageTk.PhotoImage(img)

canvas = tk.Canvas(root)
canvas.pack(fill= "both", expand=True)

canvas.create_image(
    0, 0,
    image=photo,
    anchor="nw"
)

label = tk.Label(root, text="0 KPS", font=("Arial", 40))
label.pack()

root.bind("<space>", press)

root.mainloop()