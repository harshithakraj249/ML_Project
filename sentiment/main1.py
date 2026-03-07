import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

# runtime-safe backend detection: prefer tensorflow, fallback to standalone keras
import types
try:
    import tensorflow as tf
    backend_name = "tensorflow"
except Exception:
    try:
        import keras as _keras
        # expose a minimal tf-like object so existing code using tf.keras works
        tf = types.SimpleNamespace(keras=_keras)
        backend_name = "keras"
    except Exception:
        raise RuntimeError(
            "Neither tensorflow nor keras is importable in this environment. "
            "Install TensorFlow (recommended) or Keras: pip install tensorflow    "
            "or pip install keras"
        )

print(f"Using backend: {backend_name}")

# now import other packages (numpy, flask, etc.)
import numpy as np
from flask import Flask, request, jsonify, render_template, session
import pickle
import re
# tokenizer / pad_sequences / LSTM obtained from chosen backend
Tokenizer = tf.keras.preprocessing.text.Tokenizer
pad_sequences = tf.keras.preprocessing.sequence.pad_sequences
_KerasLSTM = tf.keras.layers.LSTM

import matplotlib.pyplot as plt
import string
from nltk.corpus import stopwords
import nltk
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from nltk.tokenize.treebank import TreebankWordDetokenizer
from collections import Counter
from gensim.utils import simple_preprocess
import gensim
try:
    from sklearn.model_selection import train_test_split
except Exception:
    train_test_split = None
import warnings
warnings.filterwarnings('ignore')
import seaborn as sns
from sklearn.metrics import confusion_matrix
import pandas as pd
from flask_cors import CORS 
# from nltk.corpus import stopwords
# from nltk.stem import SnowballStemmer

app = Flask(__name__)

CORS(app)
file = open('/home/harshitha/Downloads/kannada_sentiment/stop_word.txt', 'r')
stopword = file.read()
# print(stopword)

# Compatibility wrapper to ignore legacy kwargs like 'time_major'
class CompatLSTM(_KerasLSTM):
    def __init__(self, *args, **kwargs):
        # drop legacy/unsupported kwargs present in older saved configs
        kwargs.pop('time_major', None)
        kwargs.pop('unroll', None)
        super().__init__(*args, **kwargs)

# load model using the backend object (tf.keras or keras)
best_model = None
model_path = "/home/harshitha/Downloads/kannada_sentiment/best_new.hdf5"
try:
    # try to use keras load_model from the available backend
    best_model = tf.keras.models.load_model(model_path, custom_objects={'LSTM': CompatLSTM}, compile=False)
    print("Model loaded from", model_path)
except Exception as e:
    print("Model load failed:", e)
    best_model = None

def preprocess(text):
    text = re.sub("@[0-9]", ' ', str(text).lower()).strip()
    tokens = []
    for token in text.split():
        if token not in stopword:
            tokens.append(token)
    return " ".join(tokens)

def remove_punc(string):
    # make punc a raw string to avoid SyntaxWarning
    punc = r'''!()-[]{};:'"\, <>./?@#$%^&*_~'''
    for ele in string:
        if ele in punc:
            string = string.replace(ele, " ")
    return string

def detokenize(text):
    return TreebankWordDetokenizer().detokenize(text)

@app.route('/')
def home():
    return render_template('index1.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    sentiment = ['neutral', 'happy', 'sad', 'angry', 'fear', 'surprise']
    try:
        read_file = pd.read_excel('/home/harshitha/Downloads/kannada_sentiment/new_kannada.xls', engine='xlrd')
    except ImportError as e:
        raise RuntimeError("xlrd is required to read .xls files. Install it with: pip install 'xlrd>=2.0.1'") from e
    except Exception as e:
        raise
    read_file.to_csv("Test2.csv", index=None, header=True)
    df = pd.DataFrame(pd.read_csv("Test2.csv"))
    df.groupby('Sentiment').nunique()
    # print(df)
    temp = []
    data_to_list = df['Text'].values.tolist()
    # print(len(data_to_list))
    for i in range(len(data_to_list)):
        temp.append(preprocess(data_to_list[i]))
    lis = [remove_punc(i) for i in temp]
    # print(len(lis))
    text3 = []
    for sentence in lis:
        text4 = sentence.split()
        text3.append(text4)
        # print(text3[:5])
        # print(len(text3))
    data = []
    for i in range(len(text3)):
        data.append(detokenize(text3[i]))
    # print(data[:5])
    labels = np.array(df['Sentiment'])
    y = []
    for i in range(len(labels)):
        if labels[i] == 'neutral':
            y.append(0)
        if labels[i] == 'happy':
            y.append(1)
        if labels[i] == 'sad':
            y.append(2)
        if labels[i] == 'angry':
            y.append(3)
        if labels[i] == 'fear':
            y.append(4)
        if labels[i] == 'surprise':
            y.append(5)
    y = np.array(y)
    # some TF/Keras builds don't accept the 'dtype' kwarg — cast after conversion
    labels = tf.keras.utils.to_categorical(y, 6).astype("float32")
    # print(y)
    max_words = 5000
    max_len = 200
    tokenizer = Tokenizer(num_words=max_words)
    tokenizer.fit_on_texts(data)
    sequences = tokenizer.texts_to_sequences(data)
    tdata = pad_sequences(sequences, maxlen=max_len)
    # print(tdata)
    pattern = r"[a-zA-Z0-9]"
    if request.method == "POST":
        body = request.get_json(force=True, silent=True) or {}
        data_in = body.get('title', '') if isinstance(body, dict) else ''
        text1 = re.sub(pattern, "", data_in, flags=re.I)
        print(text1)
        if len(text1) > 0 and best_model is not None:
            tokens = []
            for token in text1.split():
                tokens.append(token)
                data1 = [" ".join(tokens)]
            sequence = tokenizer.texts_to_sequences(data1)
            test = pad_sequences(sequence, maxlen=max_len)
            # use backend model predict
            preds = best_model.predict(test)
            output = sentiment[np.around(preds, decimals=0).argmax(axis=1)[0]]
            print(output)
        elif best_model is None:
            output = "Model not loaded on server."
        else:
            output = "enter valid statement in form['ನಾನು ತುಂಬ ಸಂತೋಷವಾಗಿದ್ದೇನೆ']"
        return {"class": output}
      
if __name__ == "__main__":
    app.run(port=5000, debug=True)
