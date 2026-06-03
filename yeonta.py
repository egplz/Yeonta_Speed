'''
레밀리아 연타 속도 측정 프로그램
초당 입력 수에 따라 레밀님 얼굴 바뀜
'''
import tkinter as tk
import time

times = []

def press(event):
    now = time.time()

    times.append(now)

    while times and now - times[0] > 1:
        times.pop(0)

    kps = len(times)

    label.config(text=f"{kps} KPS")

root = tk.Tk()

label = tk.Label(root, text="0 KPS", font=("Arial", 40))
label.pack()

root.bind("<space>", press)

root.mainloop()