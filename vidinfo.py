import cv2 as cv
import glob


videos = glob.glob('./*.mp4')
print(f"Number of videos in the directory: {len(videos)}")


for video in videos:
    cap = cv.VideoCapture(video)
    fps = cap.get(cv.CAP_PROP_FPS)
    fc = int(cap.get(cv.CAP_PROP_FRAME_COUNT))
    dur = fc / fps
    mins = int(dur / 60)
    secs = round(dur % 60)

    print(f"---------------------------------")
    print(f"Video: {video}")
    print(f"Recorded at: {fps} FPS")
    print(f"Total frames: {fc}")
    print(f"Duration: {mins}:{secs}")
    print(f"---------------------------------")

    cap.release()
