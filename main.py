# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :
# vim: set foldmethod=marker commentstring=\ \ #\ %s :
#
# Author:    Taishi Matsumura
# Created:   2017-04-13
#
# Copyright (C) 2017 Taishi Matsumura
#
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm
import matplotlib.mlab as mlab

plt.close('all')


class CellMap(object):
    def __init__(
        self, width, height,
        cell_ratio=0.2, act_sigma=(1.0, 1.0), inact_sigma=(5.0, 5.0)):

        self.width = width
        self.height = height
        self.N = width * height
        self.X, self.Y = np.meshgrid(np.arange(width), np.arange(height))
        self.act_sigma = act_sigma
        self.inact_sigma = inact_sigma

        # True cell means a cell.
        # False cell isn't a cell.
        self.cells = np.random.rand(self.width, self.height) < cell_ratio
        # Initialize activation map.
        self.activation_map = np.zeros((self.width, self.height))

    def _update_activation_map(self):
        active_cell_N = self.cells.sum()
        y, x = np.where(self.cells == True)
        for i in xrange(active_cell_N):
            activation = mlab.bivariate_normal(
                self.X, self.Y,
                mux=x[i], muy=y[i],
                sigmax=self.act_sigma[0], sigmay=self.act_sigma[1])
            inactivation = mlab.bivariate_normal(
                self.X, self.Y,
                mux=x[i], muy=y[i],
                sigmax=self.inact_sigma[0], sigmay=self.inact_sigma[1])
            self.activation_map += activation - inactivation

    def _update_cells(self):
        self.cells = self.activation_map > 0

    def update(self):
        self._update_activation_map()
        self._update_cells()

    def plot_map(self):
        fig = MapFigure()
        fig.plot(self.X, self.Y, self.activation_map, self.cells)
        fig.show()


class FigureBase(object):
    def __init__(self):
        self.fig = plt.figure()
        self.ax1 = self.fig.add_subplot(121, projection='3d')
        self.ax2 = self.fig.add_subplot(122)

    def show(self):
        self.fig.show()

    def save(self, name):
        self.fig.savefig(name)


class Figure1(FigureBase):
    def __init__(self):
        super(Figure1, self).__init__()

    def plot(self):
        x = y = np.arange(100)
        X, Y = np.meshgrid(x, y)
        Z1 = mlab.bivariate_normal(X, Y, mux=50.0, muy=74.0, sigmax=2.0, sigmay=2.0)
        Z2 = mlab.bivariate_normal(X, Y, mux=55.0, muy=30.0, sigmax=5.0, sigmay=5.0)
        Z = Z1 + Z2
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm)
        fig.show()


class Main(object):
    def main(self):
        np.random.seed(0)
        cell_map = CellMap(100, 100, cell_ratio=0.1, act_sigma=(2.0, 4.0), inact_sigma=(3.0, 5.0))
        cell_map.plot_map()
        cell_map.update()
        cell_map.plot_map()
        cell_map.update()
        cell_map.plot_map()
        cell_map.update()
        cell_map.plot_map()
        cell_map.update()
        cell_map.plot_map()
        cell_map.update()
        cell_map.plot_map()
        cell_map.update()
        cell_map.plot_map()
        cell_map.update()
        cell_map.plot_map()
        cell_map.update()
        cell_map.plot_map()
        cell_map.update()
        cell_map.plot_map()
        cell_map.update()
        cell_map.plot_map()


class MapFigure(FigureBase):
    def __init__(self):
        super(MapFigure, self).__init__()

    def plot(self, X, Y, activation_map, cells):
        self.ax1.plot_surface(X, Y, activation_map, rstride=5, cstride=5, cmap=cm.coolwarm)
        self.ax2.imshow(cells, origin='lower')

if __name__ == '__main__':
    main = Main()
    main.main()
