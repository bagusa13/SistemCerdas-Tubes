import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

columns = ['Age', 'Op_Year', 'axil_nodes', 'Surv_status']
src = "haberman.csv, haberman.data, haberman.txt"
df = pd.read_csv(src, names=columns)
