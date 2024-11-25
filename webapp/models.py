from django.db import models
#from keras.models import load_model
#import cv2
import numpy as np
import pickle
#from tensorflow.keras.preprocessing import image
#import tensorflow as tf
import json
from PIL import Image
import joblib
import numpy as np


svm = pickle.load(open(r'D:\python\DRUG PREDICTION\DRUG PREDICTION\FRONTEND\rf_drug.pkl', 'rb'))
xgb = pickle.load(open(r'D:\python\DRUG PREDICTION\DRUG PREDICTION\FRONTEND\x_gb_drug.pkl', 'rb'))


def predict(lst,algo):
	test = np.array(lst)
	test = np.reshape(test, (1, -1))
	print(test.shape)
	if algo=='svm':
		y_pred=svm.predict(test)
		return y_pred
	else:
		y_pred=xgb.predict(test)
		return y_pred

