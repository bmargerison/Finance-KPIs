import pandas as pd 
import matplotlib.pyplot as plt

MRR_data = pd.read_excel('C:\\Users\\Ben\\Documents\\git\\Finance-KPIs\\MRR data.xlsx')



MRR_data.plot({'y': y, 'x': x})

plt.show()