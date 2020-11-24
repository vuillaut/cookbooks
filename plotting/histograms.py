import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
from numpy.random import multivariate_normal
import seaborn as sns
import matplotlib.pylab as plt
from matplotlib.colors import ListedColormap


def seaborn_palettes():
  data = np.vstack([
    multivariate_normal([10, 10], [[3, 2], [2, 3]], size=100000),
    multivariate_normal([30, 20], [[2, 3], [1, 3]], size=1000)
])


  # construct cmap
  my_cmap = ListedColormap(sns.color_palette('mako', n_colors=100))
  my_cmap = ListedColormap(sns.color_palette('rocket', n_colors=100))
  # my_cmap = ListedColormap(sns.cubehelix_palette(start=.5, rot=-.5, n_colors=100))

  colormaps = {
      'mako': ListedColormap(sns.color_palette('mako_r', n_colors=100)),
      'rocket': ListedColormap(sns.color_palette('rocket', n_colors=100)),
      'rocket_r': ListedColormap(sns.color_palette('rocket_r', n_colors=100)),
      'seaborn-cubehelix': ListedColormap(sns.cubehelix_palette(n_colors=100)),
      'cube1': ListedColormap(sns.cubehelix_palette(start=0, rot=-.5, light=1, n_colors=100)),
      'cube2': ListedColormap(sns.cubehelix_palette(start=0, rot=-.75, light=1, n_colors=100)),
      'cube3': ListedColormap(sns.cubehelix_palette(start=0.3, rot=-0.4, dark=0.1, light=1., reverse=False, n_colors=100)),
      'cube4': ListedColormap(sns.cubehelix_palette(start=2., rot=-0.4, dark=0.1, light=1., reverse=False, n_colors=100)),
      'seagreen': ListedColormap(sns.light_palette("seagreen", n_colors=100)),
      'light_blues': ListedColormap(sns.color_palette('Blues', n_colors=100)),
  }

  for key, cm in colormaps.items():

      plt.hist2d(data[:, 0], 
                 data[:, 1],
                 bins=100,  
                 cmap=cm,
                )
      plt.colorbar()
      plt.title(key)
      plt.show()
