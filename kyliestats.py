import matplotlib.pyplot as plt
import numpy as np
from numpy.polynomial.polynomial import polyfit
np.random.seed(23321421)

spelling = np.array([5,3,2,3,1,4,5,3,4,4,5,5,4,5,3,2,4,2,4,2,5,3,5,2,3,4,5,2,2,5,5,2,4,4,5,3,1,1,5,3,0,5,3])
grammar = np.array([4,6,3,3,1,5,4,4,2,6,6,2,3,3,6,3,3,4,4,2,3,3,3,1,6,4,5,4,1,4,4,6,3,5,5,5,3,1,4,5,2,4,5])
fig, ax = plt.subplots()
colors = np.random.rand(len(grammar))
area = (30 * np.random.rand(len(grammar)))**2  # 0 to 15 point radii
m, b = np.polyfit(spelling, grammar, 1)

# adding the regression line to the scatter plot
plt.plot(spelling, m*spelling + b)
plt.scatter(spelling, grammar,s=area, c=colors, alpha=0.25)
ax.set(xlabel='Number of Identified Spelling Errors',ylabel='Number of Identified Grammar Errors',title='Number of Identified Spelling Errors vs Number of Identified Grammar Errors')
# either have show or savefig commented
plt.show()
# plt.savefig('figure1.png', dpi=300)
