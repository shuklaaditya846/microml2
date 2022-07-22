# Continuous Physical Motion Detection
https://user-images.githubusercontent.com/23453334/180441656-d343efc4-038b-4250-9f0e-4fa6b16f0a51.mp4



## Project Description
Let's keep it simple; This is a project where I used an accelerometer with a microcontroller to classify and detect motions and gestures.

## What things did it involve?
### Hardware
A NodeMCU-12E (ESP8266)
An MPU6050: 6-axis accerometer [https://www.google.com/search?q=mpu6050]

### Software
Python module ```everywhereml```
Little bit Python and C++

## Get Started
1. First flash the file inside the folder "[simple-logging-of-data](https://github.com/shuklaaditya846/microml2/tree/main/simple_logging_of_data)".
You can check if things are working fine by taking a look at Serial Monitor.
![image1](https://user-images.githubusercontent.com/23453334/180440388-0ad01f60-d482-4236-b1fa-c5367becee36.jpg)


2. In order to use it, you have to have the module 'everywhereml'.
It can be installed by ```pip3 install everywhereml>=0.0.3```

3. You can start collecting the data once you've installed all the dependencies. Go to the [Jupyter notebook linked above](https://github.com/shuklaaditya846/microml2/blob/main/continous-motion-classification.ipynb). The python script will lead you through.

* You can run it as a simple python file in any terminal. You don't necessarily have to use Jupyter.

4. Once data collection is done, it will automatically start classification. You don't have to do anything here.

5. 2 files will be generated once the process is complete; Classifier.h and Pipeline.h inside a filder 'mpuClassify'. This is also presented as an Example here.

6. Now you're done with this part. Go ahaead and flash it onto your microcontroller. Fire up the serial monitor and see things in action.


https://user-images.githubusercontent.com/23453334/180442386-5c94c7df-bf06-44b5-b436-1f378a59d19d.mp4

