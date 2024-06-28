import sklearn
import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.model_selection import train_test_split
from gensim.models import Word2Vec

import tensorflow as tf
from keras._tf_keras.keras.preprocessing.sequence import pad_sequences
from keras._tf_keras.keras.layers import Embedding , LSTM ,Dense,Dropout
from keras._tf_keras.keras.models import Sequential
from keras._tf_keras.keras.preprocessing.text import one_hot


nltk.download('stopwords')
ps = PorterStemmer()


from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix,ConfusionMatrixDisplay



real = pd.read_csv("islenmis_dogru_haberler.csv")
fake = pd.read_csv("islenmis_sahte_haberler.csv")


real['label'] = 1
fake['label'] = 0



