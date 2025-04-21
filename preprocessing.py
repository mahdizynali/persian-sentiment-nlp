import os
import numpy as np
import pandas as pd
from tokenizer import MaZe_tokenizer
from sklearn.model_selection import train_test_split

class DataPrep:
    '''کلاس آماده سازی اولیه داده ها برای آموزش'''
    def __init__(self, directory_path) -> None:
        # نوع عواطف را دسته بندی می‌کنیم
        self.categories = {
            "sad": 0,
            "fear": 1,
            "surprise": 2,
            "disgust": 3,
            "anger": 4,
            "joy": 5
        }
        self.data_path = directory_path
        self.toke = MaZe_tokenizer()

    def data_process(self):
        csv_files = [f for f in os.listdir(self.data_path) if f.endswith('.csv')]
        dataframes = {}

        for file in csv_files:
            full_path = os.path.join(self.data_path, file)
            df = pd.read_csv(full_path)

            # فقط توییت و عواطف آن ذخیره شود
            if 'tweet' in df.columns and 'emotion' in df.columns:
                df = df[['tweet', 'emotion']]
                df['emotion'] = df['emotion'].map(self.categories)

            dataframes[file] = df
        
        # تمام دیتا ها را ترکیب و شافل می‌کنیم
        merged_df = pd.concat(dataframes, ignore_index=True)
        shuffled_df = merged_df.sample(frac=1, random_state=42).reset_index(drop=True)

        data = shuffled_df['tweet'].values
        labels = shuffled_df['emotion'].values

        # تقسیم داده ها با نسبت ۸۰ به ۲۰
        return train_test_split(data, labels, test_size=0.2, random_state=42)

    def freqs(self, text, y):
        """ساخت یک مپینگ از(کلمه, عواطف)"""
        label = np.squeeze(y).tolist()
        freqs = {}

        for y, txt in zip(label, text):
            for word in self.toke.do_tokenize(txt):
                pair = (word, y)
                if pair in freqs:
                    freqs[pair] += 1
                else:
                    freqs[pair] = 1
        # with open("freqs.txt", "+a") as tk:
        #     tk.write(str(freqs) + "\n")
        #     tk.close()
        return freqs