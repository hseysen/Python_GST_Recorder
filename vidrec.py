import os
import cv2
import threading
import time
import datetime


EXIT_APP = False
FILENAME_TAIL = "_".join(str(datetime.datetime.now()).split()[0].split("-") + str(datetime.datetime.now()).split()[1].split(":")).split(".")[0]
RECORD_DURATION = 300 
FPS = 60.0
RESOLUTION = (720, 480)

if not os.path.exists("gstpipeline.txt"):
    raise OSError("Please provide the file \"gstpipeline.txt\" in the same directory as this script.")
with open("gstpipeline.txt", "r") as rf:
    PIPELINE = rf.read()
    print(PIPELINE)


class AppThread(threading.Thread):
    def __init__(self, name, func):
        super().__init__()
        self.name = name
        self.func = func
    
    def run(self):
        print(f"Starting {self.name} thread")
        self.func()
        print(f"Exiting {self.name} thread")


def video_record_thread():
    global thread2
    started = False
    cap = cv2.VideoCapture(PIPELINE, cv2.CAP_GSTREAMER)
    
    fourcc = cv2.VideoWriter_fourcc(*'MP4V')
    out = cv2.VideoWriter(f"output_{FILENAME_TAIL}.mp4", fourcc, FPS, RESOLUTION)

    while True:
        ret, frame = cap.read()
    
        cv2.imshow("Stream", frame)

        if not started:
            thread2 = AppThread("Time Keeping", time_keep_thread)
            thread2.start()
            started = True
        out.write(frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
        if EXIT_APP:
            break
    
    cap.release()
    out.release()
    cv2.destroyAllWindows()


def time_keep_thread():
    global EXIT_APP
    time.sleep(RECORD_DURATION)
    EXIT_APP = True


if __name__ == "__main__":
    thread1 = AppThread("Video Recording", video_record_thread)
    thread1.start()

    thread1.join()
    thread2.join()
