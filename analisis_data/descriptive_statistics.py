import numpy as np
from scipy import stats
import pandas as pd
import matplotlib.pyplot as plt

array_of_nums = np.array([2, 5, 3, 4, 1, 3, 4, 2, 3, 3, 6, 4, 3])

# Measuring Central Tendency
print(array_of_nums.mean())
print(np.median(array_of_nums))
print(stats.mode(array_of_nums)[0])

# Measuring Dispersion
range1 = array_of_nums.max() - array_of_nums.min()
print(range1)
iqr = np.percentile(array_of_nums, 75) - np.percentile(array_of_nums, 25)
print(iqr)
num_series = pd.Series(array_of_nums)
print(num_series.var())
print(num_series.std())

# Measuring Asymmetric
# plt.hist(array_of_nums, bins=4)
# plt.show()
print(num_series.skew())

# Data Correlation
sample_data = {
    'name': ['John', 'Alia', 'Ananya', 'Steve', 'Ben'],
    'age': [24, 22, 23, 25, 28],  
    'communication_skill_score': [85, 70, 75, 90, 90],
    'quantitative_skill_score': [80, 90, 80, 75, 70]
}
 
df = pd.DataFrame(sample_data)
 
print(df.corr(numeric_only=True))
print(df.cov(numeric_only=True))