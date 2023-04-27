import numpy as np
import matplotlib.pyplot as plt

y = np.array([50, 25, 25, 15])
myexp = [0, 0, 0.2, 0]
mylables = ['Moscow', 'SPB', 'EKB', 'Perm']
mycolors = ['lime', 'green', 'brown', 'yellow']
plt.pie(y, labels=mylables, explode=myexp, shadow=True, colors=mycolors)
plt.legend(title='Cities names: ')
plt.show()


def visualize_type(types_set):
    pass


def visualize_companies(companies_set):
    pass


def visualize_industries(industries_set):
    pass


def visualize_currencies(currencies_set):
    pass
