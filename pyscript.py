# %%
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


# %%
# file = "sat-data.h5"
# sat_data = pd.read_hdf(file)
filex = "sat-data.npy"
filey = "sat-labels.npy"

sat_data = np.load( filex )
sat_labels = np.load( filey, allow_pickle=True )

# %%
## Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(sat_data, sat_labels, test_size=0.2, random_state=42)

# %%
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Softmax, Conv1D, MaxPooling1D

# Define the CNN model
model = Sequential()

# input_shape = (20, 6, 1)
# First convolutional layer (assuming 1D data)
model.add(Conv1D(filters=128, kernel_size=2, activation='relu'))

# Second convolutional layer
model.add(Conv1D(filters=128, kernel_size=2, activation='relu'))

# Max pooling layer
model.add(MaxPooling1D(pool_size=2))

# Flatten the output
model.add(Flatten())

# Fully connected layers
model.add(Dense(units=192, activation='relu'))
model.add(Dense(units=89, activation='relu'))

# Output layer with 3 units for maneuver classification (no maneuver, beginning of maneuver, during maneuver)
model.add(Dense(units=3, activation='softmax'))

# Compile the model (loss function and optimizer might be different in the paper)
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Implement 10-fold cross-validation (code not shown here, refer to Kera's documentation)
model.build(input_shape=sat_data.shape)

model.summary()
# Train the model (refer to Keras documentation for training with validation sets)
# model.fit(X_train, y_train, epochs=5)


# %%
sat_data = sat_data.astype('float32')
sat_labels = np.array([label[0] for label in sat_labels]).astype('int32')

# %%

model.fit(sat_data, sat_labels, epochs=50, batch_size=32, validation_split=0.2)

# %%
# Evaluate the model
# model.evaluate(X_test, y_test)
model.evaluate(sat_data, sat_labels)

# show trustworthiness of the model
# model.predict(X_test)
model.predict(sat_data[:1])


