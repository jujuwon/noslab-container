import matplotlib.pyplot as plt
import numpy as np

font = {
    'family': 'serif',
    'color': 'blue',
    'weight': 'bold',
    'size': 14
}

# t = np.arange(0., 5., 0.2)
# plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
# plt.plot([1, 2, 3, 4],[1, 4, 9, 16], 'ro')
# plt.axis([0, 6, 0, 20])

plt.plot([1,2,3,4], [1,4,9,16], label='line1')
plt.plot([1,2,3,4], [3,5,9,7], label='line2')
plt.xlabel('X-Label', labelpad=15, fontdict=font, loc='right')
plt.ylabel('Y-Label', labelpad=20, fontdict=font, loc='top')
plt.legend(loc='best', ncol=2)
plt.show()