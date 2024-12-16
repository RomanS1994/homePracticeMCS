import kagglehub
import pandas as pd

# Download latest version
path = kagglehub.dataset_download("iamsouravbanerjee/house-rent-prediction-dataset")

# print("Path to dataset files:", path)


data = pd.read_csv(path)  # заміни 'your_file_name.csv' на фактичну назву файлу

# Перегляд перших 5 рядків даних
print(data.head())
