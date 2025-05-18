from config import *
from tokenizer import MaZe_tokenizer
from preprocessing import DataPrep
from trainer import naive_bayes, naive_bayes_predict

data_prep = DataPrep(DATASET_PATH)
print("\npreparing data ...\n")
X_train, X_test, y_train, y_test = data_prep.data_process()
tokenizer = MaZe_tokenizer()

print("\nGenerating frequency ...\n")
freqs = data_prep.freqs(X_train, y_train)

print("\ncalculating loglikelihood ...\n")
logprior, loglikelihood = naive_bayes(freqs, y_train)

print("\nModel is ready. Enter text to classify (CTRL+C to quit):\n")
while True:
    try:
        txt = input("متن را وارد کنید: ").strip()
        if not txt:
            continue

        score = naive_bayes_predict(txt, logprior, loglikelihood)

        print(f"Log-probability score: {score:.4f}")
        sentiment = "مثبت" if score > 0 else "منفی"
        print(f"پیش‌بینی احساس: {sentiment}\n")

    except KeyboardInterrupt:
        print("\nخروج از برنامه. موفق باشید!")
        break