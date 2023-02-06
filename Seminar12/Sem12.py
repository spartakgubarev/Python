import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# df = pd.read_csv('Seminar12\california_housing_train.csv')

# print(df.head())

# Изображения точек долготы по отношению к широте.
# Можно заметить, что дома расположены в определенной "полосе" долготы и широты
# sns.scatterplot(data=df, x="longitude", y="latitude")
# plt.show()

# Самостоятельная работа №1
# Изобразите отношение households к population
# sns.scatterplot(data=df, x="households", y="population")
# plt.show()

# sns.scatterplot(data=df, x="households", y="population",  hue="total_rooms")
# plt.show()

# Самостоятельная работа №2
# Добавьте total_rooms используя дополнительное измерение size
# sns.scatterplot(data=df, x="households", y="population",  size="total_rooms")
# plt.show()

# cols = ['population', 'median_income', 'housing_median_age', 'median_house_value']
# g = sns.PairGrid(df[cols])
# g.map(sns.scatterplot)
# plt.show()
# линейная зависимость по диагонали потому, что х и у одинаковы

# sns.relplot(x="latitude", y="median_house_value", kind="line", data=df)
# plt.show()

# Самостоятельная работа №3
# Визуализировать longitude по отношения к median_house_value
# Используя линейный график
# sns.relplot(x="longitude", y="median_house_value", kind="line", data=df)
# plt.show()

# sns.scatterplot(data=df, x="latitude", y="longitude",  hue="median_house_value")
# plt.show()

# sns.histplot(data=df, x="median_income")
# plt.show()

# Самостоятельная работа №5
# Изобраить гистограмму по housing_median_age
# sns.histplot(data=df, x="housing_median_age")
# plt.show()

# sns.histplot(data=df[df['housing_median_age']<15], x="median_income")
# plt.show()

# sns.histplot(data=df, x="population", binwidth=1000)
# plt.show()

# df.loc[df['housing_median_age'] <= 20, 'age_group'] = 'Молодые'
# df.loc[(df['housing_median_age'] > 20) & (df['housing_median_age'] <= 50), 'age_group'] = 'Ср. возраст'
# df.loc[df['housing_median_age'] > 50, 'age_group'] = 'Пожилые'

# df.groupby('age_group')['median_income'].mean().plot(kind='bar')
# plt.show()

# df.loc[df['median_income'] > 6, 'income_group'] = 'rich'
# df.loc[df['median_income'] < 6, 'income_group'] = 'everyone_else'
# sns.displot(df, x="median_house_value", hue="income_group")
# plt.show()

# Самостоятельная работа 
# Изобразить гистограмму по median_house_value с оттенком age_group
# df.loc[df['median_income'] > 6, 'age_group'] = 'rich'
# df.loc[df['median_income'] < 6, 'age_group'] = 'everyone_else'
# sns.displot(df, x="median_house_value", hue="age_group")
# plt.show()

# corr = df.corr()

# mask = np.triu(np.ones_like(corr, dtype=bool))

# Создаем полотно для отображения большого графика
# f, ax = plt.subplots(figsize=(11, 9))

# Создаем цветовую политру
# cmap = sns.diverging_palette(230, 20, as_cmap=True)

# Визуализируем данные кореляции 
# sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0,
#             square=True, linewidths=.5, cbar_kws={"shrink": .5})
# plt.show()


#----------------------------------------- Пингвины
penguins = sns.load_dataset("penguins")
df = penguins
print(penguins.head())
#----------------------------------------- 
# - Использовать 2-3 точечных графика
# sns.scatterplot(data=df, x="bill_length_mm", y="island")
# plt.show()

# sns.scatterplot(data=df, x="species", y="flipper_length_mm")
# plt.show()

#----------------------------------------- 
# - Применить доп. измерение в точечных графиках, используя аргументы hue, size, stile
# sns.scatterplot(data=df, x="body_mass_g", y="island",  hue="sex")
# plt.show()

# sns.scatterplot(data=df, x="body_mass_g", y="island",  size="sex")
# plt.show()

# sns.set_style("darkgrid")
# sns.scatterplot(data=df, x="body_mass_g", y="island", hue="sex", color="k", alpha=0.8)
# plt.show()

#----------------------------------------- 
# - Использовать PairGrid с типом графика на ваш выбор
# cols = ['species', 'island', 'bill_length_mm', 'bill_depth_mm', 'flipper_length_mm',\
#         'body_mass_g', 'sex']
# g = sns.PairGrid(df[cols])
# g.map(sns.scatterplot)
# plt.show()
#----------------------------------------- 
# - Изобразить Heatmap
# corr = df.corr()
# mask = np.triu(np.ones_like(corr, dtype=bool))
# # Создаем полотно для отображения большого графика
# f, ax = plt.subplots(figsize=(11, 9))
# # Создаем цветовую политру
# cmap = sns.diverging_palette(230, 20, as_cmap=True)
# # Визуализируем данные кореляции 
# sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0,
#             square=True, linewidths=.5, cbar_kws={"shrink": .5})
# plt.show()

#----------------------------------------- 
# - Использовать 2-3 гистограммы
# sns.histplot(data=df, x="species")
# plt.show()

# Изобразить гистограмму по species с оттенком age_group
df.loc[df['body_mass_g'] > 5000, 'age_group'] = 'тяжелые'
df.loc[df['body_mass_g'] < 5000, 'age_group'] = 'легкие'
sns.displot(df, x="species", hue="age_group")
plt.show()
