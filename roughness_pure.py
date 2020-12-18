import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df_data = pd.read_csv('C:/Users/Kapp/PycharmProjects/abbott/roughness/pure.csv', sep=';')


print(df_data)
# df_data = df_data[df_data['Vorbehandlung'] == 'keine']
# mean_roughness = df_data['Ra_nf [µm]'].mean()

roughness_nf_q = df_data['Konfokal (q)']
roughness_nf_l = df_data['Konfokal (l)']
roughness_mech_q = df_data['Tastschnitt (q)']
roughness_mech_l = df_data['Tastschnitt (l)']
samples = df_data['Probe']
#
plt.barh(samples, roughness_nf_l)
plt.barh(samples, roughness_nf_q)
plt.barh(samples, roughness_mech_q)
plt.barh(samples, roughness_mech_l)


#plt.vlines(mean_roughness, 0, len(np.asarray(samples))-1, linestyle='--', colors='red')
plt.title('Rauheit (ohne Vorbehandlung)', pad=10, fontsize=16)
xticks = [x / 100 for x in range(0, 30, 2)]
plt.xticks(xticks)
plt.xlabel('Ra [µm]', labelpad=10)
plt.show()