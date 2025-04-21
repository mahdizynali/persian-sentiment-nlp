from config import *
from stemmer import PersianStemmer

class MaZe_tokenizer:
    '''کلاس توکنایزر برای حذف حروف اضافه و توکن بندی لغات'''
    def __init__(self):
        self.stemmer = PersianStemmer()

        with open(STOPWORDS_PATH, encoding='utf-8') as f:
            self.stopwords = [line.strip() for line in f if line.strip()]
        with open(PUNCTUATIONS_PATH, encoding='utf-8') as f:
            self.punctuations = [line.strip() for line in f if line.strip()]
        with open(NUMBERS_PATH, encoding='utf-8') as f:
            self.numbers = [line.strip() for line in f if line.strip()]


    def remove_extras(self, text):
        '''حذف موارد اضافی مثل لینک، منشن، هشتگ و غیره'''
        text = re.sub(r'\$\w*', '', text)  # حذف نمادهای بورسی
        text = re.sub(r'^RT[\s]+', '', text)  # حذف متن RT
        text = re.sub(r'https?:\/\/.*[\r\n]*', '', text)  # حذف لینک‌ها
        text = re.sub(r'@\w+', '', text)  # حذف منشن‌ها
        text = re.sub(r'#', '', text)  # حذف علامت #
        text = re.sub(r'\s+', ' ', text).strip()  # حذف فاصله‌های اضافی
        return text


    def do_tokenize(self, text):
        '''توکن بندی متن با حذف موارد اضافی، استمر و فیلتر'''
        text = self.remove_extras(text)
        text_tokens = text.split()
        tokens_clean = []

        for word in text_tokens:
            
            # word = word.strip().lower()

            if word in self.stopwords:
                continue
            if word in self.punctuations:
                continue
            if word in self.numbers:
                continue
            if word in string.punctuation:
                continue

            if self.stemmer:
                word = self.stemmer.stem(word)

            tokens_clean.append(word)

        # with open("tokens.txt", "+a") as tk:
        #     tk.write(str(text_tokens) + "\n")
        #     tk.close()
        return tokens_clean
