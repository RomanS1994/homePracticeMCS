import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats


url = 'https://docs.google.com/spreadsheets/d/18WCpPS96Tb3cB0FCsIA92PEhcmBkp08sjYhS9DsQfJE/edit#gid=954244094' 
url = url[:url.find('/edit')] + '/export?format=csv'
df = pd.read_csv(url)
# print(df.head(5)) # Вивід даних
# print(df.info()) # Перевірка даних
# print(df)


df.isnull().sum()
df.dropna(inplace=True)

normality_results = {}
# побудови гістограм
for column in df.columns:


    plt.figure(figsize=(8, 6))  #розмір графіка
    plt.hist(df[column], bins=20, alpha=0.7, edgecolor='black')  # побудова гістограми
    plt.title(f'Гістограма для колонки: {column}', fontsize=14)  
    plt.xlabel('Значення', fontsize=12)  
    plt.ylabel('Частота', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)  #  сітка
    plt.show()  
    stat, p_value = stats.normaltest(df[column])
    normality_results[column] = {'Статистика': stat, 'P-value': p_value}

    print('-'*80)
    if p_value < 0.05:
        print(f"{column}: не є нормальним (p-value = {p_value:})")
    else:
        print(f"{column}: нормальний (p-value = {p_value:.4f})")
    print('-'*80)


correlation_with_product_sold = df.corr()['Product_Sold']
print("\nКореляція з Product_Sold:\n", correlation_with_product_sold)



summary = pd.DataFrame({
    'Середнє': df.mean(),
    'Дисперсія': df.var(),
    'Стандартне відхилення': df.std()
})
print("Статисти характеристики:")
print(summary)




sns.heatmap(df.corr(), annot=True)
plt.title("Матриця кореляції", fontsize=16)
plt.show()  




