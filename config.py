import os
import re
import string
import numpy as np
import pandas as pd
from tqdm import tqdm
from sklearn.model_selection import train_test_split

DATASET_PATH = "dataset"
NUMBERS_PATH = "manipulate/numbers.txt"
STOPWORDS_PATH = "manipulate/stopwords.txt"
PUNCTUATIONS_PATH = "manipulate/punctuations.txt"
STEMMER_SUFFIX_PATH = "manipulate/stem_suffixes.txt"
STEMMER_PREFIX_PATH = "manipulate/stem_prefixes.txt"

English_categories = {
    "sad": 0,
    "fear": 1,
    "surprise": 2,
    "disgust": 3,
    "anger": 4,
    "joy": 5
}

Persian_categories = {
    0: "ناراحت",
    1: "ترس",
    2: "شگفت زده",
    3: "منزجر",
    4: "عصبانیت",
    5: "ترکیبی"
}

LEARNING_RATE=0.01
CLASSES=6 # تعداد عواطف بر اساس دیتاست
ITRATION=1