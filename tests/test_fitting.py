#!/usr/bin/env python3

import pytest
import numpy as np
np.seterr(all='raise')

from cylinder_fitting import fit


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


def make_points_on_a_cylinder(theta, phi, C, r, N):
    '''Make N points on a cylinder defined by the center C, direction defined theta and phi and radius r.
    Also return the direction of the cylinder'''
    
    M = np.dot(rotation_matrix_from_axis_and_angle(np.array([0, 0, 1]), phi),
               rotation_matrix_from_axis_and_angle(np.array([1, 0, 0]), theta))

    x = np.dot(M, np.array([1, 0, 0]))
    y = np.dot(M, np.array([0, 1, 0]))
    z = np.dot(M, np.array([0, 0, 1]))

    delta = np.radians(10)
    t = 0.1

    return [C + r * (np.cos(i * delta) * x + np.sin(i * delta) * y + i * t * z) for i in range(N)], z

def test_fit():
    print("test fit.")

    C = np.array([0, 0, 0])
    r = 10
    data, w = make_points_on_a_cylinder(1, -0.3, C, r, 100)
    
    w_fit, C_fit, r_fit = fit(data)

    
    assert(np.absolute(1 - np.absolute(np.dot(w, w_fit))) < 1e-4)

    assert(np.absolute(np.dot(w, C - C_fit)) / np.linalg.norm(w) / np.linalg.norm(C - C_fit) > 0.999)

    assert(np.absolute(r - r_fit) < r_fit * 1e-4)

