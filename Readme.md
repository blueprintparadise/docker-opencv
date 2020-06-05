# About
Bleeding edge docker container for CPU only useage. For running opencv / python in docker with access to web cam and display of the host computer (Ubuntu). 
Since Tensorflow requires GPU for training, this setup only allows for inference.
Not tested on windows or Mac.
### Current version: (May 2020 - the year of COVID19)
* Python 3.8.2
* Tensorflow 2.2.0
* OpenCV 4.3.0
* Numpy 1.18.4
* scipy 1.4.1
* Matplotlib 3.2.1
* FFmpeg 4.1.4-1
* sklearn 0.23.0
* seaborn 0.10.1
* openai gym 0.17.2
* pytorch 1.5.0

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
sudo docker run -it -v my-vol:/home --device=/dev/video0:/dev/video0  -e DISPLAY=$DISPLAY  -v /tmp/.X11-unix:/tmp/.X11-unix --name testbench randhawp/opencv-python bash
```
6) Inside the container shell, goto  /examples

- to test camera : dockercam.py (press q to exit)
- to test a videofor opencv from youtube : youtube.py (press q to exit )
- to test the gym environment : cartpole0.py
- to test gym atari env :atari0.py
- to test TF2.0 / Keras training and prediction example: tf-image-0.py



To upgrade just do a docker pull randhawp/opencv-python:latest
