class PersianStemmer:
    '''از این کلاس به منظور ریشه یابی کلمات استفاده می‌کنیم'''
    def __init__(self, prefix_file, suffix_file):
        self.prefixes, self.suffixes = self.load_affixes(prefix_file, suffix_file)

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

# prefix_file = "manipulate/stem_prefixes.txt"
# suffix_file = "manipulate/stem_suffixes.txt"
# stemmer = PersianStemmer(prefix_file, suffix_file)
# words = ["می‌نویسم", "کتاب‌ها", "بهترین", "دوستانم", "نمی‌دانند"]
# for word in words:
#     print(f"ریشه {word} = {stemmer.stem(word)}")