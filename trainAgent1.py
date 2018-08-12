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
import os,os.path

from keras.callbacks import TensorBoard

tb = TensorBoard(log_dir = "D:\\Mastas\\models\\graphs", histogram_freq = 0, write_graph = True, write_images = True)
#           0   1   2   3   4	5	6
moveSet = ['A','','W','D','Y','DY','DZ']

resize = (84,84)
batchSize = 16
ImGen = ImageDataGenerator(rescale = 1./255)
#ImGen = ImageDataGenerator()
train_data_dir = 'D:\\screenShots\\agent\\moves'
training_data = ImGen.flow_from_directory(directory =train_data_dir,
											target_size=resize,
											batch_size=batchSize,
											class_mode='categorical')

											
	
								
adam = keras.optimizers.Adam(lr=0.00056, beta_1=0.9, beta_2=0.999, epsilon=1e-08, decay=0.00001)		
				
#load pretrained model
model = keras.models.load_model('D:\\Mastas\\models\\agent18')
#used for initializing model
# model= Sequential()
# model.add(Conv2D(32,(3,3), input_shape = (resize[0],resize[1],3)))
# model.add(Activation('relu'))
# #model.add(MaxPooling2D(pool_size=(2,2)))

# model.add(Conv2D(32,(3,3)))
# model.add(Activation('relu'))
# #model.add(MaxPooling2D(pool_size=(2,2)))

# model.add(Conv2D(64,(3,3)))
# model.add(Activation('relu'))
# #model.add(MaxPooling2D(pool_size=(2,2)))

# model.add(Flatten())
# model.add(Dense(32))
# model.add(Activation('relu'))
# model.add(Dropout(0.25))
# model.add(Dense(64))
# model.add(Activation('relu'))
# model.add(Dropout(0.25))
# model.add(Dense(len(moveSet)))

# model.add(Activation('softmax'))

# model.compile(loss = 'categorical_crossentropy',
# 					optimizer = adam,
# 					metrics=['accuracy'])
						
a = len([name for name in os.listdir(train_data_dir+"\\0") if os.path.isfile(os.path.join(train_data_dir+"\\0", name))])
w = len([name for name in os.listdir(train_data_dir+"\\1") if os.path.isfile(os.path.join(train_data_dir+"\\1", name))])
s = len([name for name in os.listdir(train_data_dir+"\\2") if os.path.isfile(os.path.join(train_data_dir+"\\2", name))])
d = len([name for name in os.listdir(train_data_dir+"\\3") if os.path.isfile(os.path.join(train_data_dir+"\\3", name))])
y = len([name for name in os.listdir(train_data_dir+"\\4") if os.path.isfile(os.path.join(train_data_dir+"\\4", name))])
dy = len([name for name in os.listdir(train_data_dir+"\\5") if os.path.isfile(os.path.join(train_data_dir+"\\5", name))])
dz = len([name for name in os.listdir(train_data_dir+"\\6") if os.path.isfile(os.path.join(train_data_dir+"\\6", name))])

totalScreenshotNumber = a + w + s + d + y + dy + dz
print(totalScreenshotNumber)
tb.set_model(model)
model.fit_generator(training_data,
	steps_per_epoch = totalScreenshotNumber/batchSize,
	epochs = 1,
	callbacks = [tb]
	)

model.save("D:\\Mastas\\models\\agent19")


