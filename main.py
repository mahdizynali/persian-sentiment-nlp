from preprocessing import DataPrep

persian_label = {
    0: "ناراحت",
    1: "ترس",
    2: "شگفت زده",
    3: "منزجر",
    4: "عصبانیت",
    5: "ترکیبی"
}


data_prep = DataPrep(directory_path="dataset")

X_train, X_test, y_train, y_test = data_prep.data_process()

freqs = data_prep.freqs(X_train, y_train)
# print(freqs)


# for key, value in list(freqs.items())[:10]:
#     print(f"Word-Sentiment Pair: {key}, Frequency: {value}")
