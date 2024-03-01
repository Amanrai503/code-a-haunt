from win_capture import win_cap
from time import time
import cv2
import numpy


def get_ss():
    while True:
        screenshot = win_cap()
        screenshot = numpy.array((screenshot))
        # cv2.rectangle(screenshot, (0, 0), (100, 100), (0, 0, 255), 3)
        cv2.imshow("CV", screenshot)

        loop_time = time()
        key = cv2.waitKey(1)
        if key == ord("q"):
            cv2.destroyAllWindows()
            break
        elif key == ord("p"):
            cv2.imwrite("positive_data/{}.jpg".format(loop_time), screenshot)
        elif key == ord("n"):
            cv2.imwrite("negetive_data/{}.jpg".format(loop_time), screenshot)


print("Done")
