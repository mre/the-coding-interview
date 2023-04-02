import numpy as np
import matplotlib.pyplot as plt

# Set up the grid
xmin, xmax, ymin, ymax = -2, 1, -1.5, 1.5
npts = 500
x, y = np.meshgrid(np.linspace(xmin, xmax, npts), np.linspace(ymin, ymax, npts))
c = x + 1j*y
z = np.zeros_like(c)

# Iterate the Mandelbrot equation
for i in range(100):
    z = z**2 + c

# Create the plot
plt.imshow(np.abs(z), extent=(xmin, xmax, ymin, ymax), cmap='magma')
plt.axis('off')
plt.show()
