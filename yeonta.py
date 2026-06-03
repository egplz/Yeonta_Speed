'''
레밀리아 연타 속도 측정 프로그램
초당 입력 수에 따라 레밀님 얼굴 바뀜
'''
import tkinter as tk
import time
from PIL import Image, ImageTk

times = []

def press(event):
    now = time.time()

    times.append(now)

    while times and now - times[0] > 1:
        times.pop(0)

    kps = len(times)

    label.config(text=f"{kps} KPS")

def change_image(kps):
    if kps >= 7:
        img = Image.open("level2.png")
    

root = tk.Tk()

img = Image.open("level1.png")
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