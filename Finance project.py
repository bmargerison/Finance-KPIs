import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

#import KPI dashboard
dashboard = pd.read_excel('.\\MRR data.xlsx', index_col=0)

#create figures and define common axes
fig, axs = plt.subplots(2,2, figsize=(20,15))
month_labels = ['Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Jan', 'Feb', 'Mar']

#extract tables from dashbaord for plots
MRR_data = dashboard.iloc[[4,5,6,7],:].set_axis(month_labels, axis='columns')
MRR_data_plot = MRR_data.swapaxes('index','columns')

user_numbers = dashboard.iloc[[28,29,30],:].set_axis(month_labels, axis='columns')
user_numbers_table = user_numbers.swapaxes('index','columns')

#plot axs[0,0]
axs[0,0].set_yticks([50000, 100000, 150000, 200000, 250000])
axs[0,0].set_yticklabels(['50k', '100k', '150k', '200k', '250k'])
axs[0,0].set_title('Monthly Revenue CY vs. PYs')
colors = ['skyblue','wheat','lightgreen','salmon']
MRR_data_plot.plot.bar(ax=axs[0,0], color=colors, width=0.9, linewidth=20, label="hi")

#plot ax[0,1]
axs[0,1].set_yticks([50000, 100000, 150000, 200000, 250000])
axs[0,1].set_yticklabels(['50k', '100k', '150k', '200k', '250k'])
axs[0,1].set_title('MRR & User Numbers')
MRR_data_plot.plot(ax=axs[0,1], linewidth=3, color=colors)
axs[0,1].get_legend().remove()


#plot second axis on ax[0,1]
ax2 = axs[0,1].twinx()
ax2.set_ylim([0,250])
colors2 = ['wheat','lightgreen','salmon']
user_numbers_table.plot.bar(ax=ax2, color=colors2).legend(loc='upper center')



print(MRR_data_plot)
print(user_numbers_table)
plt.show()
