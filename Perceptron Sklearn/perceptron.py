import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv('placement.csv')
print(df.shape)
df.head()
sns.scatterplot(df['cgpa'],df['resume_score'],hue=df['placed'])
