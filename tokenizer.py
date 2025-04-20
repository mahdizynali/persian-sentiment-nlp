import re
import string
from stemmer import PersianStemmer

class MaZe_tokenizer:
    def __init__(self):
        self.stem = PersianStemmer(prefix_file="manipulate/stem_prefixes.txt", suffix_file="manipulate/stem_suffixes.txt")

    def remove_extras(self, text):
        text = re.sub(r'\$\w*', '', text)
        text = re.sub(r'^RT[\s]+', '', text)
        text = re.sub(r'https?:\/\/.*[\r\n]*', '', text)
        text = re.sub(r'@\w+', '', text)
        text = re.sub(r'#', '', text)
        text = re.sub(r'\s+', ' ', text).strip() # حذف اسپیس های اضافی
        return text

    def do_tokenize(self, text):
        text = self.preprocess(text)
        text_tokens = text.split()
        tokens_clean = []
        for word in text_tokens:
            word = word.lower()
            if word not in self.stopwords and word not in string.punctuation:
                if self.stemmer:
                    word = self.stemmer.stem(word)
                tokens_clean.append(word)

        return tokens_clean