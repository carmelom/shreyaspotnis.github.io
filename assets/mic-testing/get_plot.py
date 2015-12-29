import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams.update({'font.size': 10, 'font.family': 'STIXGeneral',
                            'mathtext.fontset': 'stix'})

x = np.linspace(0, np.pi*2.0, 100)
y = np.sin(x)

plt.figure(figsize=(4, 3))
plt.plot(x, y, color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.tight_layout()
plt.savefig('test_plot.svg')
