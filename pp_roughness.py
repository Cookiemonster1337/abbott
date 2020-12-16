import pandas as pd
import matplotlib.pyplot as plt

df_data = pd.read_csv('C:/Users/Julian/PycharmProjects/abbott/roughness/maxcoat.csv', sep=';')


print(df_data)
df_data = df_data[df_data['Vorbehandlung'] == 'plasmapoliert']
mean_roughness = df_data['Ra_nf [µm]'].mean()

roughness = df_data['Ra_nf [µm]']
samples = df_data['Probe']
#
plt.barh(samples, roughness)
plt.vlines(mean_roughness, 0, 6, linestyle='--', colors='red')
plt.title('Rauheit')
plt.xlabel('Rauheit [µm]')
plt.show()
