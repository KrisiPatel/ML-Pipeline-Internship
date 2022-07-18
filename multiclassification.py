#https://www.youtube.com/watch?v=oOSXQP7C7ck&t=38s


import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.optimizers import SGD
import numpy as np
import pickle


#generate dummy data
x_train = np.random.random((1000, 20))
y_train = keras.utils.to_categorical(np.random.randint(10,size=(1000,1)),num_classes=10)
x_test = np.random.random((100,20))
y_test = keras.utils.to_categorical(np.random.randint(10,size=(100,1)),num_classes=10)

x_train[50:51]
y_train[50:51]
x_test[0]
y_test[0]


model = Sequential()
#Dense(64) is a fully-connected layer with 64 hidden units
#in the first layer, you must specify the expected input data shape
#here, 20 dimensional vectors
model.add(Dense(64, activation='relu', input_dim=20))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(10,activation='softmax'))

sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)

model.compile(loss='categorical_crossentropy',optimizer=sgd,metrics=['accuracy'])

model.fit(x_train, y_train, epochs=1000, batch_size=128)

score = model.evaluate(x_test, y_test, batch_size=128,)

model.metrics_names

score

#to save the whole model  https://www.youtube.com/watch?v=NVY0FucNRU4
model.save("saving_file")

new_model = keras.models.load_model("saving_file")
score = model.evaluate(x_test, y_test, batch_size=128,)


#pickle_out = open("flask_deployment.pkl")
#pickle.dump(model, pickle_out)
#loaded_model = pickle.load(open("flask_deployment.pkl","rb"))
#result = loaded_model.score(x_test,y_test)
#print(result)