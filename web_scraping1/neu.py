import pandas as pd
import numpy as np
import pickle
from keras.preprocessing.text import Tokenizer
from keras.models import Sequential
from keras.layers import Activation, Dense, Dropout
from sklearn.preprocessing import LabelBinarizer
import sklearn.datasets as skds
from pathlib import Path

# For reproducibility
np.random.seed(1237)
 
# Source file directory
path_train = "/home/arushi/toi_news_articles/'85% Raj rural women don’t know about HIV-AIDS'"
 
files_train = skds.load_files(path_train,load_content=False)
 
label_index = files_train.target
label_names = files_train.target_names
labelled_files = files_train.filenames
 
data_tags = ["filename","category","news"]
data_list = []
 
# Read and add data from file to a list
i=0
for f in labelled_fmodel = Sequential()
model.add(Dense(512, input_shape=(vocab_size,)))
model.add(Activation('relu'))
model.add(Dropout(0.3))
model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.3))
model.add(Dense(num_labels))
model.add(Activation('softmax'))
model.summary()
 
model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
 
history = model.fit(x_train, y_train,
                    batch_size=batch_size,
                    epochs=30,
                    verbose=1,
                    validation_split=0.1)iles:
    data_list.append((f,label_names[label_index[i]],Path(f).read_text()))
    i += 1
 
# We have training data available as dictionary filename, category, data
data = pd.DataFrame.from_records(data_list, columns=data_tags)

encoder = LabelBinarizer()
encoder.fit(train_tags)
y_train = encoder.transform(train_tags)
y_test = encoder.transform(test_tags)


