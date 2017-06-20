import numpy as np

def rotation_matrix_from_axis_and_angle(u, theta):
  '''Calculate a rotation matrix from an axis and an angle.'''

  x = u[0]
  y = u[1]
  z = u[2]
  s = np.sin(theta)
  c = np.cos(theta)

  return np.array([[c + x**2 * (1 - c), x * y * (1 - c) - z * s, x * z * (1 - c) + y * s],
                   [y * x * (1 - c) + z * s, c + y**2 * (1 - c), y * z * (1 - c) - x * s ],
                   [z * x * (1 - c) - y * s, z * y * (1 - c) + x * s, c + z**2 * (1 - c) ]])
