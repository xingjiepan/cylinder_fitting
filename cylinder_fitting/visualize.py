import numpy as np
import matplotlib
matplotlib.use('TkAgg') 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

from .geometry import rotation_matrix_from_axis_and_angle 
from . import fitting


def show_G_distribution(data):
    '''Show the distribution of the G function.'''
    Xs, t = fitting.preprocess_data(data)  

    Theta, Phi = np.meshgrid(np.linspace(0, np.pi, 50), np.linspace(0, 2 * np.pi, 50))
    G = []

    for i in range(len(Theta)):
        G.append([])
        for j in range(len(Theta[i])):
            w = fitting.direction(Theta[i][j], Phi[i][j])
            G[-1].append(fitting.G(w, Xs))

    plt.imshow(G, extent=[0, np.pi, 0, 2 * np.pi], origin='lower')
    plt.show()

def show_fit(w_fit, C_fit, r_fit, Xs):
    '''Plot the fitting given the fitted axis direction, the fitted
    center, the fitted radius and the data points.
    '''

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    
    # Plot the data points
    
    ax.scatter([X[0] for X in Xs], [X[1] for X in Xs], [X[2] for X in Xs])
   
    # Get the transformation matrix

    theta = np.arccos(np.dot(w_fit, np.array([0, 0, 1])))
    phi = np.arctan2(w_fit[1], w_fit[0])

    M = np.dot(rotation_matrix_from_axis_and_angle(np.array([0, 0, 1]), phi),
               rotation_matrix_from_axis_and_angle(np.array([0, 1, 0]), theta))

    # Plot the cylinder surface
   
    delta = np.linspace(-np.pi, np.pi, 20)
    z = np.linspace(-10, 10, 20)

    Delta, Z = np.meshgrid(delta, z)
    X = r_fit * np.cos(Delta)
    Y = r_fit * np.sin(Delta)

    for i in range(len(X)):
        for j in range(len(X[i])):
            p = np.dot(M, np.array([X[i][j], Y[i][j], Z[i][j]])) + C_fit

            X[i][j] = p[0]
            Y[i][j] = p[1]
            Z[i][j] = p[2]

    ax.plot_surface(X, Y, Z, alpha=0.2)

    # Plot the center and direction

    ax.quiver(C_fit[0], C_fit[1], C_fit[2], 
            r_fit * w_fit[0], r_fit * w_fit[1], r_fit * w_fit[2], color='red')


    plt.show()
