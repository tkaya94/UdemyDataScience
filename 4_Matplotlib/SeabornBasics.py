import matplotlib.pyplot as plt
import seaborn as sns

import numpy as np
np.random.seed(0)
import pandas as pd

data = pd.read_csv("data/titanic/final_dataset.csv")
print(data.head())

# sns.histplot(data["Age"])
# plt.show()

# g = sns.jointplot(x="Survived", y="Age", data=data, kind="kde")
# g.ax_joint.set_xticks([0, 1])
# plt.show()

penguins = sns.load_dataset("penguins")
sns.pairplot(penguins, hue="species", height=2.5, kind="scatter")
plt.show()
