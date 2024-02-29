import cv2
import numpy
from win_capture import win_cap
import tkinter as tk
cascade_t = cv2.CascadeClassifier('csds\\cascade.xml')

#def run_dect():
while True:
    screenshot = win_cap()
    #screenshot = numpy.array(screenshot)
    rect = cascade_t.detectMultiScale(screenshot)
    for i in rect:
        x, y, w, h = i
        cv2.rectangle(screenshot, (x, y), (x + w, y + h), color=(0, 0, 225), thickness=3)
    cv2.imshow("gold_storage", screenshot)
    key = cv2.waitKey(1)
    if key == ord("q"):
        cv2.destroyAllWindows()
        break
