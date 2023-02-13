# Python GST Recorder
The scripts provided in this repository can be used to record and analyze videos using GStreamer and OpenCV. The only prerequisite is your GStreamer pipeline that you want to obtain the stream through, which should be written in a new file named `gstpipeline.txt`. The pipeline looks something like this:

```
videotestsrc num-buffers=100 ! capsfilter caps=video/x-raw,format=RGB,width=640,height=480 ! appsink emit-signals=True
```

