from config import *

class PersianStemmer:
    '''از این کلاس به منظور ریشه یابی کلمات استفاده می‌کنیم'''
    def __init__(self):
        self.prefixes, self.suffixes = self.load_affixes(STEMMER_PREFIX_PATH, STEMMER_SUFFIX_PATH)

    def load_affixes(self, prefix_path, suffix_path):
        with open(prefix_path, encoding='utf-8') as f:
            prefixes = [line.strip() for line in f if line.strip()]
        with open(suffix_path, encoding='utf-8') as f:
            suffixes = [line.strip() for line in f if line.strip()]
        return sorted(prefixes, key=len, reverse=True), sorted(suffixes, key=len, reverse=True)

    def stem(self, word):

        # حذف تمام پیشوند های لغات
        for prefix in self.prefixes:
            if word.startswith(prefix):
                word = word[len(prefix):]
                break

        # حذف تمام پسوند های لغات
        for suffix in self.suffixes:
            if word.endswith(suffix):
                word = word[:-len(suffix)]
                break

        return word