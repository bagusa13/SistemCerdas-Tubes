import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('haberman.csv')
df.columns = ['age', 'op_Year', 'axil_nodes', 'surv_status']

print("tampilkan baris pertama:")
display(df.head())

print("\nstatus kelangsungan hidup:")
print("1 = bertahan hidup 5 tahun atau lebih\n2 = meninggal dalam 5 tahun")
print(df['surv_status'].value_counts())


plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='surv_status', palette='set2')
plt.title('distribusi kelas (survival status)')
plt.xlabel('Status (1 = >= 5 tahun, 2 = < 5 tahun)')
plt.ylabel('jumlah Pasien')
plt.show()