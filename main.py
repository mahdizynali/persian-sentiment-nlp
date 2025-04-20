from preprocessing import DataPrep

persian_label = {
    0: "ناراحت",
    1: "ترس",
    2: "شگفت زده",
    3: "منزجر",
    4: "عصبانیت",
    5: "ترکیبی"
}

train_set, test_set = DataPrep("dataset").data_process()
# print(train_set.shape)