import numpy as np
import cv2
import pyautogui
import tkinter as tk

from PIL import Image,ImageTk
from tkinter import *
from tkinter import filedialog

root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

screen_size = (screen_width, screen_height)

fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("output.avi", fourcc, 20.0, screen_size)

while True:
    img = pyautogui.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    out.write(frame)
    resize = cv2.resize(frame, (100, 100))
    cv2.imshow("screenshot", resize)
    if cv2.waitKey(1) == ord("q"):
        break

cv2.destroyAllWindows()
out.release()
