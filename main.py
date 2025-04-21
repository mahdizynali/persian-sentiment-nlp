from config import *
from tokenizer import MaZe_tokenizer
from preprocessing import DataPrep
from trainer import Numpy_Trainer


data_prep = DataPrep(DATASET_PATH)
X_train, X_test, y_train, y_test = data_prep.data_process()
tokenizer = MaZe_tokenizer()
freqs = data_prep.freqs(X_train, y_train)


trainer = Numpy_Trainer(freqs)
trainer.train(X_train, y_train, tokenizer)



# correct = 0
# for tweet, label in zip(X_test, y_test):
#     pred = trainer.predict(tweet, tokenizer)
#     if pred == label:
#         correct += 1

# accuracy = correct / len(y_test)
# print(f"Test Accuracy: {accuracy:.2f}")