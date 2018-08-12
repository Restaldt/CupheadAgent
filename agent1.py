import keras #machine learning api using tf
import numpy as np
from keras.utils.np_utils import to_categorical
import keras.backend as K
from PIL import Image
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential,Model
from keras.layers import Dense, Activation,Conv2D , MaxPooling2D, Flatten,Dropout, Lambda
from tensorflow.python import debug as tf_debug
from keras.layers import Input, RepeatVector
from keras.engine.topology import Layer
from keras.layers.wrappers import TimeDistributed
from keras import backend as K
import tensorflow as tf
from keras.layers.merge import concatenate
from tensorflow.contrib import distributions
import cv2
import os,os.path
from pyautogui import press,keyUp,keyDown
import pyautogui
agent = keras.models.load_model('D:\\Mastas\\models\\agent18')
moveSet = ['A','','W','D','DY','DZY','DZ']

#print("Test")
ss_data_dir = 'D:\\screenShots\\agent\\ss'
train_data_dir = 'D:\\screenShots\\agent\\moves'
a = len([name for name in os.listdir(train_data_dir+"\\0") if os.path.isfile(os.path.join(train_data_dir+"\\0", name))])
w = len([name for name in os.listdir(train_data_dir+"\\1") if os.path.isfile(os.path.join(train_data_dir+"\\1", name))])
s = len([name for name in os.listdir(train_data_dir+"\\2") if os.path.isfile(os.path.join(train_data_dir+"\\2", name))])
d = len([name for name in os.listdir(train_data_dir+"\\3") if os.path.isfile(os.path.join(train_data_dir+"\\3", name))])
y = len([name for name in os.listdir(train_data_dir+"\\4") if os.path.isfile(os.path.join(train_data_dir+"\\4", name))])
dy = len([name for name in os.listdir(train_data_dir+"\\5") if os.path.isfile(os.path.join(train_data_dir+"\\5", name))])
dz = len([name for name in os.listdir(train_data_dir+"\\6") if os.path.isfile(os.path.join(train_data_dir+"\\6", name))])
totalScreenshotNumber = a + w + s + d + y + dy + dz

#lower the sleep between keystrokes
pyautogui.PAUSE = 0.045


varMove = ''

while True:
	keyDown('X')
	
	resize = (84,84)
	batchSize = 1
	ImGen = ImageDataGenerator(rescale = 1./255)
#ImGen = ImageDataGenerator()
	predict_data_dir = "D:\\screenShots\\agent\\ss\\ss2\\"+str(totalScreenshotNumber + len([name for name in os.listdir(ss_data_dir) if os.path.isfile(os.path.join(ss_data_dir, name))]))
	
	#print(predict_data_dir)
	
	if os.path.isdir(predict_data_dir):

		predict_data = ImGen.flow_from_directory(directory =predict_data_dir,
												target_size=resize,
												batch_size=batchSize,
												class_mode=None)
		prediction = agent.predict_generator(predict_data,1,verbose=0)
		index = np.argmax(prediction[0])
	else:
		index = 1
	if index == 4:
		keyUp(varMove)
		varMove = 'D'
		keyDown(varMove)
		keyDown('Y')
		keyUp('Y')
	if index == 5:
		keyUp(varMove)
		varMove = 'D'
		keyDown(varMove)
		pyautogui.PAUSE = 0.1
		keyDown('Z')
		keyUp('Z')
		pyautogui.PAUSE = 0.045
		keyDown('Y')
		keyUp('Y')
		
	elif index == 6:
		keyUp(varMove)
		varMove = 'D'
		keyDown(varMove)
		pyautogui.PAUSE = 0.1
		keyDown('Z')
		keyUp('Z')
		pyautogui.PAUSE = 0.045
	elif index == 0:
		keyUp(varMove)
		varMove = 'A'
		keyDown(varMove)
		pyautogui.PAUSE = 0.1
		keyDown('Z')
		keyUp('Z')
		keyUp(varMove)
		pyautogui.PAUSE = 0.045
	else:
		keyUp(varMove)
		varMove = moveSet[index]
		keyDown(varMove)

	# else:
	# 	varMove = ''
	# 	keyDown(varMove)			
	#print(index)
	