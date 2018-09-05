#%%
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import linregress
from regression import find_curve

def usda_dairy():
    #Get all dairy items from dataset. Note: Dairy codes are in the 1000's range
    df = pd.read_csv("regression/datasets/USDA_nutrient.csv").query('1000 <= NDB_No < 1999').dropna()

    # open graph, plot data points
    sns.set_style("darkgrid")
    g = sns.FacetGrid(df, size = 6)
    g = g.map(plt.scatter, "FA_Mono_(g)", "Cholestrl_(mg)", edgecolor="w")
    g = (g.set_axis_labels('Polyunsaturated Fat (g)','Cholesterol (mg)'))

    # get actual regression line
    gradient, intercept, r_value, p_value, std_err = linregress(df['FA_Mono_(g)'].tolist(),df['Cholestrl_(mg)'].tolist())
    reg_x=np.linspace(0,8,100)
    reg_y=gradient*reg_x+intercept
    plt.plot(reg_x,reg_y)

    # get custom regression line
    X_plot = np.linspace(0, 8.5, 100)
    Y_plot = 20*X_plot+30
    plt.plot(X_plot, Y_plot, color='r')

    find_curve()

    plt.show()

if __name__ == "__main__":
    usda_dairy()