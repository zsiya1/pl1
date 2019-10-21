
import pandas as pd
import matplotlib.pyplot as plt



df = pd.read_csv('/home/siddhi/Downloads/DA Programs/Assignment1/iris.csv')

print("Description:")
df.describe()

print("Minimum value:")
df.min()

print("Maximum value:")
df.max()

print("Average value:")
df.mean()

print("Std dev value:")
df.std()

print("Variance value:")
df.var()

print("Percentiles:")
df.quantile([0, .25, .5, .75, 1])

print("Histograms:")
df.hist()

print("BoxPlots:")
df.boxplot()

