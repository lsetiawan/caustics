from math import pi
from typing import Tuple

import torch
from torch import Tensor


def flip_axis_ratio(q, phi):
    """
    Makes q positive, then swaps x and y axes if it's larger than 1.
    """
    q = q.abs()
    return torch.where(q > 1, 1 / q, q), torch.where(q > 1, phi + pi / 2, phi)


def translate_rotate(x, y, phi=None, x_0=0.0, y_0=0.0):
    """
    Translates and applies an ''active'' counterclockwise rotation to the input
    point.
    """
    x = x - x_0
    y = y - y_0

    if phi is not None:
        c_phi = phi.cos()
        s_phi = phi.sin()
        return x * c_phi - y * s_phi, x * s_phi + y * c_phi
    else:
        return x, y


def to_elliptical(x, y, q):
    """
    Converts to elliptical Cartesian coordinates.
    """
    return x * q.sqrt(), y / q.sqrt()


def get_meshgrid(resolution, nx, ny, device=None) -> Tuple[Tensor, Tensor]:
    xs = torch.linspace(-1, 1, nx, device=device) * resolution * (nx - 1) / 2
    ys = torch.linspace(-1, 1, ny, device=device) * resolution * (ny - 1) / 2
    return torch.meshgrid((xs, ys), indexing="xy")
