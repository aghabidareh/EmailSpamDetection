from keras_preprocessing.sequence import pad_sequences

from detector.modules.loader import *


def predictor(text):
    sequence = tokenizer.texts_to_sequences([text])
    padded_sequences = pad_sequences(sequence, maxlen=max_len)

    prediction = model.predict(padded_sequences)

    return "Spam" if prediction > 0.5 else "Safe"
