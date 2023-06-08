import matplotlib.pyplot as plt
import numpy as np

vetor = np.array([1,2,-3,4])
vetor = vetor + 2

print(vetor)

plt.plot(vetor)
plt.savefig('plot.png')
plt.show()