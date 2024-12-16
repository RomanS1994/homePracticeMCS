import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Завантаження даних
file_path = '/path/to/your/House_Rent_Prediction.xlsx'
data = pd.read_excel(file_path)

# Перетворення стовпця 'Posted On' у формат дати
data['Posted On'] = pd.to_datetime(data['Posted On'], errors='coerce')

# Перевірка на пропущені значення
missing_values = data.isnull().sum()

# Перетворення категоріальних змінних у числові
label_encoder = LabelEncoder()

categorical_columns = ['Floor', 'Area Type', 'Area Locality', 'City', 'Furnishing Status', 'Tenant Preferred', 'Point of Contact']
for col in categorical_columns:
    data[col] = label_encoder.fit_transform(data[col])

# Визначення ознак та цільової змінної
X = data[['BHK', 'Size', 'Floor', 'Area Type', 'Area Locality', 'City', 'Furnishing Status', 'Tenant Preferred', 'Bathroom']]
y = data['Rent']

# Розподіл даних на тренувальну та тестову вибірки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Створення моделі лінійної регресії
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)

# Прогнози та оцінка моделі лінійної регресії
y_pred_lr = lr_model.predict(X_test)
mse_lr = mean_squared_error(y_test, y_pred_lr)
r2_lr = r2_score(y_test, y_pred_lr)

# Створення моделі дерева рішень
dt_model = DecisionTreeRegressor(random_state=42)
dt_model.fit(X_train, y_train)

# Прогнози та оцінка моделі дерева рішень
y_pred_dt = dt_model.predict(X_test)
mse_dt = mean_squared_error(y_test, y_pred_dt)
r2_dt = r2_score(y_test, y_pred_dt)

# Результати моделей
print(f"Linear Regression - MSE: {mse_lr}, R2: {r2_lr}")
print(f"Decision Tree - MSE: {mse_dt}, R2: {r2_dt}")

# Графік залишків для лінійної регресії
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_test - y_pred_lr, color='blue', label='Residuals (Linear Regression)')
plt.axhline(y=0, color='red', linestyle='--')
plt.title('Residuals of Linear Regression Model')
plt.xlabel('Actual Rent')
plt.ylabel('Residuals')
plt.legend()
plt.show()

# Графік залишків для дерева рішень
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_test - y_pred_dt, color='green', label='Residuals (Decision Tree)')
plt.axhline(y=0, color='red', linestyle='--')
plt.title('Residuals of Decision Tree Model')
plt.xlabel('Actual Rent')
plt.ylabel('Residuals')
plt.legend()
plt.show()
