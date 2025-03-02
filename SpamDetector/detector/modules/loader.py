from tensorflow.keras.models import load_model
from joblib import load
import json

model = load_model('detector/modules/model.h5')

with open('detector/modules/tokenizer.h5', 'rb') as f:
    tokenizer = load(f)

with open('detector/modules/params.json', 'r') as f:
    params = json.load(f)
    max_len = params['max_len']
