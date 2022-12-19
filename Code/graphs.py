import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#load csv file
strat = pd.read_csv('C:/Users/adapa/OneDrive/Desktop/Stratified Visual Embedding/FiguresData/resultsstart.csv')
total = pd.read_csv('C:/Users/adapa/OneDrive/Desktop/Stratified Visual Embedding/FiguresData/resultstotal.csv')

#drop the first column
strat = strat.drop(strat.columns[0], axis=1)
total = total.drop(total.columns[0], axis=1)

#add column that states the model
strat['Model'] = 'Stratified'
total['Model'] = 'Total'

#combine the two dataframes
df = pd.concat([strat, total])

#plot bar bar plot that compares average times
def plot_bar(df, title, x_label, y_label, file_name):
    fig, ax = plt.subplots()
    ax.bar(df['Model'], df['mean'], label='mean')
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    fig.tight_layout()
    plt.savefig(file_name)
    plt.show()

#plot bar plot that compares min average and max times
plot_bar(df, None, 'Model', 'Time (s)', 'C:/Users/adapa/OneDrive/Desktop/Stratified Visual Embedding/FiguresData/Time.png')

#build a table in latex style that compares the mean, max, average times
def build_table(df, file_name):
    df = df.groupby('Model').agg(['mean', 'max', 'min'])
    df = df.round(2)
    df = df.style.to_latex()
    with open(file_name, 'w') as f:
        f.write(df)


#build table
build_table(df, 'C:/Users/adapa/OneDrive/Desktop/Stratified Visual Embedding/FiguresData/table.txt')

#show table
print(df)

