import pandas as pd 
import matplotlib.pyplot as plt


dashboard = pd.read_excel('C:\\Users\\Ben\\Documents\\git\\Finance-KPIs\\MRR data.xlsx', index_col=0)

fig, [[ax1, ax2, ax3], [ax4, ax5, ax6]] = plt.subplots(2,3, figsize=(20,50))

month_labels = ['Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Jan', 'Feb', 'Mar']

MRR_data = dashboard.iloc[[4,5,6,7],:].set_axis(month_labels, axis='columns')
MRR_data_plot = MRR_data.swapaxes('index','columns')
ax1.set_yticks([50000, 100000, 150000, 200000, 250000])
ax1.set_yticklabels(['50k', '100k', '150k', '200k', '250k'])
MRR_data_plot.plot.bar(ax=ax1)



print(MRR_data_plot)


plt.show()
