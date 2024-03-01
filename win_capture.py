import cv2
import numpy as np
import win32gui
import win32con
import win32ui
from time import time


def win_cap(w_name):
    hwnd = win32gui.FindWindow(None,w_name )#'Clash of Clans'
    win_rect = win32gui.GetWindowRect(hwnd)
    w = (win_rect[2] - win_rect[0]) - 12
    h = (win_rect[3] - win_rect[1]) - 32
    wDC = win32gui.GetWindowDC(hwnd)
    dcObj = win32ui.CreateDCFromHandle(wDC)
    cDC = dcObj.CreateCompatibleDC()
    dataBitMap = win32ui.CreateBitmap()
    dataBitMap.CreateCompatibleBitmap(dcObj,w,h)
    cDC.SelectObject(dataBitMap)
    cDC.SelectObject(dataBitMap)
    cDC.BitBlt((0, 0), (w, h), dcObj, (6, 28), win32con.SRCCOPY)

    signedIntsArray = dataBitMap.GetBitmapBits(True)
    img = np.fromstring(signedIntsArray, dtype=np.uint8)
    img.shape = (h, w, 4)

    dcObj.DeleteDC()
    cDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, wDC)
    win32gui.DeleteObject(dataBitMap.GetHandle())

    img = np.ascontiguousarray(img)

    return img

