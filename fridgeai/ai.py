from os import path
import numpy as np
from keras.models import load_model


def predict(images):
    """Given a list of images, output the most likely prediction."""
    data = np.array(images).astype("float") / 255.0
    model = load_model(path.join(".", "data"))
    preds = model.predict(data, batch_size=32).argmax(axis=1)
    print(preds)
    prediction = np.argmax(np.bincount(preds))

    if prediction == 0:
        prediction = "Coke"
    elif prediction == 1:
        prediction = "Emborg"
    elif prediction == 2:
        prediction = "Pepsi"

    return prediction
