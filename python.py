import keras
import numpy as np

x_test = np.random.random((100,20))
y_test = keras.utils.to_categorical(np.random.randint(10,size=(100,1)))


new_model = keras.models.load_model("saving_file")
score = new_model.evaluate(x_test, y_test, batch_size=128,)