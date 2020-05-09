# About
Bleeding edge docker container for CPU only useage. For running opencv / python in docker with access to web cam and display of the host computer (Ubuntu). 
Not tested on windows or Mac.
### Current version: (May 2020 - the year of COVID19)
* Python 3.8.2
* Tensorflow 2.2.0
* OpenCV 4.3.0
* Numpy 1.18.4
* scipy 1.4.1
* Matplotlib 3.2.1
* FFmpeg 4.1.4-1

# Setup
1) Download the docker image on your PC
```
docker pull randhawp/opencv-python:latest
```
2) Create a docker volume
```
sudo docker volume create my-vol
```
3) Copy the dockercam.py file to the volume 
```
sudo cp dockercam.py /var/lib/volumes/my-vol/_data
```
4) Allow screen sharing by executing xhost on host pc
```
xhost +
```
5) Run the container
```
sudo docker run -it -v my-vol:/home --device=/dev/video0:/dev/video0  -e DISPLAY=$DISPLAY  -v /tmp/.X11-unix:/tmp/.X11-unix --name testbench randhawp/opencv-python sh
```
6) Inside the container shell
```
cd /home
python3 dockercam.py

```

You should see the camera view open up in a window
Press q to quit.

To upgrade just do a docker pull randhawp/opencv-python
