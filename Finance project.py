import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn

#import KPI dashboard
dashboard = pd.read_excel('C:\\Users\\Ben\\Documents\\git\\Finance-KPIs\\MRR data.xlsx', index_col=0)

#create figures and define common axes
fig, axs = plt.subplots(2,2, figsize=(30,30))
month_labels = ['Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Jan', 'Feb', 'Mar']

#extract MRR data from dashbaord for MRR graph (axs[0,0])
MRR_data = dashboard.iloc[[4,5,6,7],:].set_axis(month_labels, axis='columns')
MRR_data_plot = MRR_data.swapaxes('index','columns')

#plot axs[0,0]
axs[0,0].set_yticks([50000, 100000, 150000, 200000, 250000])
axs[0,0].set_yticklabels(['50k', '100k', '150k', '200k', '250k'])
axs[0,0].set_title('Monthly Revenue CY vs. PYs')
MRR_data_plot.plot.bar(ax=axs[0,0], width=0.9, linewidth=20)


print(MRR_data_plot)
plt.show()
