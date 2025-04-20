import os
import pandas as pd
from sklearn.model_selection import train_test_split

# نوع عواطف را دسته بندی می‌کنیم
categories = {
    "sad": 0,
    "fear": 1,
    "surprise": 2,
    "disgust": 3,
    "anger": 4,
    "joy": 5
}

def read_csv_dataset(directory_path):
    csv_files = [f for f in os.listdir(directory_path) if f.endswith('.csv')]
    dataframes = {}

    for file in csv_files:
        full_path = os.path.join(directory_path, file)
        df = pd.read_csv(full_path)

        # فقط توییت و عواطف آن ذخیره شود
        if 'tweet' in df.columns and 'emotion' in df.columns:
            df = df[['tweet', 'emotion']]
            df['emotion'] = df['emotion'].map(categories)

        dataframes[file] = df
    
    # تمام دیتا ها را ترکیب و شافل می‌کنیم
    merged_df = pd.concat(dataframes, ignore_index=True)
    shuffled_df = merged_df.sample(frac=1, random_state=42).reset_index(drop=True)
    return shuffled_df


dataframes = read_csv_dataset("dataset")
# print(dataframes.head())

# تقسیم داده ها با نسبت ۸۰ به ۲۰
train_data, test_data = train_test_split(dataframes, test_size=0.2, random_state=42)

# print("Train Set:")
# print(train_data.head())
# print("\nTest Set:")
# print(test_data.head())