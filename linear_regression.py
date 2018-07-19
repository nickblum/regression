#%%
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#df = pd.io.excel.read_excel("sr27abxl/ABBREV.xlsx")
df = pd.read_csv("sr27abxl/ABBREV.csv")

df_poly_chol = df[['FA_Poly_(g)','Cholestrl_(mg)']]

X_plot = np.linspace(0, 7, 100)
Y_plot = 10*X_plot+5

g = sns.FacetGrid(df_poly_chol, size = 6)
g = g.map(plt.scatter, "FA_Poly_(g)", "Cholestrl_(mg)", edgecolor="w")
plt.plot(X_plot, Y_plot, color='r')
plt.show()

