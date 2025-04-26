from config import *
from tokenizer import MaZe_tokenizer
from preprocessing import DataPrep
from trainer import Numpy_Trainer

data_prep = DataPrep(DATASET_PATH)
X_train, X_test, y_train, y_test = data_prep.data_process()
tokenizer = MaZe_tokenizer()

print("\npreparing data ...\n")
freqs = data_prep.freqs(X_train, y_train)

trainer = Numpy_Trainer(freqs)
trainer.train(X_train, y_train, tokenizer)

# ارزیابی روی تست
correct = 0
for tweet, label in zip(X_test, y_test):
    pred = trainer.predict(tweet, tokenizer)
    if pred == label:
        correct += 1

accuracy = correct / len(y_test)
print(f"✅ Test Accuracy: {accuracy:.2f}")


print("\nمدل آماده‌ی پیش‌بینی هست!")
while True:
    text = input("\n➤ یک متن برای تشخیص عواطف وارد کن (یا 'exit' برای خروج): ")
    if text.lower() == 'exit':
        break
    pred_class = trainer.predict(text, tokenizer)
    print(f"کلاس پیش‌بینی شده: {pred_class}")