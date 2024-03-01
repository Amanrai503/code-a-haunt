import cv2
import numpy
from win_capture import win_cap
import tkinter as tk


def run_dect(a, w_name):
    cascade_t = cv2.CascadeClassifier(a)  # 'csds\\cascade.xml'
    while True:
        screenshot = win_cap(w_name)
        # screenshot = numpy.array(screenshot)
        rect = cascade_t.detectMultiScale(screenshot)
        for i in rect:
            x, y, w, h = i
            cv2.rectangle(screenshot, (x, y), (x + w, y + h), color=(0, 0, 225), thickness=3)
        cv2.imshow("gold_storage", screenshot)
        key = cv2.waitKey(1)
        if key == ord("q"):
            cv2.destroyAllWindows()
            break


def detect_and_count(a, w_name):
    cascade_t = cv2.CascadeClassifier(a)
    while True:

        screenshot = win_cap(w_name)
        rect = cascade_t.detectMultiScale(screenshot)
        for i in range(len(rect)):

            x, y, w, h = rect[i]
            cv2.rectangle(screenshot, (x, y), (x + w, y + h), color=(0, 0, 225), thickness=3)
            cv2.putText(screenshot, str(i+1), (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,0),3)
        cv2.imshow("gold_storage", screenshot)
        key = cv2.waitKey(1)
        if key == ord("q"):
            cv2.destroyAllWindows()
            break



