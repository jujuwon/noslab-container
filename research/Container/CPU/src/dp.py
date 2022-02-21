from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import os
import datetime
import time

def printNow():
    now = datetime.datetime.now()
    print(now)

print(os.getpid())
time.sleep(1)
printNow()

import numpy as np
import tensorflow as tf

np.random.seed(3)
tf.random.set_seed(3)

# 준비된 수술 환자 데이터를 로드.
Data_set = np.loadtxt("./dataset/ThoraricSurgery.csv", delimiter=",")

# 환자의 기록과 수술 결과를 X와 Y로 구분하여 저장.
X = Data_set[:,0:17]
Y = Data_set[:,17]

# 딥러닝 구조를 결정(모델을 설정하고 실행).
model = Sequential()
model.add(Dense(30, input_dim=17, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# 딥러닝을 실행.
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X, Y, epochs=100, batch_size=10)

printNow()

time.sleep(1)