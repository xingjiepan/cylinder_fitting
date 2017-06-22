import numpy as np


def normalize(v):
    '''Normalize a vector based on its 2 norm.'''
    if 0 == np.linalg.norm(v):
        return v
    return v / np.linalg.norm(v)

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

def point_line_distance(p, l_p, l_v):
    '''Calculate the distance between a point and a line defined
    by a point and a direction vector.
    '''
    l_v = normalize(l_v)
    u = p - l_p
    return np.linalg.norm(u - np.dot(u, l_v) * l_v)
