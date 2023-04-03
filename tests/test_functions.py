import numpy as np
import pytest

from mpm_la import det, mult, adj, inv, solve


@pytest.mark.parametrize('a, deta',
                         [([[2, 0, -1], [0, 5, 6], [0, -1, 1]], [22.0]),
                          ([[1, 3, 2, 4], [2, 4, 5, 2],
                            [2, 1, 3, 3], [4, 2, 1, 6]], [-100.0])])
def test_det(a, deta):
    m = det(a)

    assert np.isclose(m, deta)


@pytest.mark.parametrize('a, b, mult1',
                         [([[1, 2], [3, 4]],
                           [[5], [6]], [[17], [39]]),
                          ([[3, 4, 1], [5, 4, 3], [3, 6, 4], [2, 5, 4]],
                           [[1, 2, 4, 6, 3], [2, 3, 3, 5, 3], [8, 2, 5, 3, 4]],
                           [[19, 20, 29, 41, 25], [37, 28, 47, 59, 39],
                            [47, 32, 50, 60, 43], [44, 27, 43, 49, 37]])])
def test_mult(a, b, mult1):
    m = mult(a, b)

    assert np.allclose(m, mult1)


@pytest.mark.parametrize('a, adj1',
                         [([[1, 0, -1], [-2, 3, 0], [1, -3, 2]],
                           [[6, 3, 3], [4, 3, 2], [3, 3, 3]]),
                          ([[1, 5, -1], [-2, 3, 0], [1, -8, 2]],
                           [[6, -2, 3], [4, 3, 2], [13, 13, 13]])])
def test_adj(a, adj1):
    m = adj(a)

    assert np.allclose(m, adj1)


@pytest.mark.parametrize('a, inv1',
                         [([[1, 0, -1], [-2, 3, 0],
                            [1, -3, 2]], [[2, 1, 1],
                                          [4 / 3, 1, 2 / 3], [1, 1, 1]]),
                          ([[1, 3, -1], [-2, 2, 0], [1, -7, 2]],
                           [[1, 0.25, 0.5], [1, 0.75, 0.5], [3, 2.5, 2]])])
def test_inv(a, inv1):
    m = inv(a)

    assert np.allclose(m, inv1)


@pytest.mark.parametrize('a, b, solve1',
                         [([[1, 1, 1], [-1, 1, 1],
                            [-1, -1, 1]], [[1], [2], [-1]],
                           [[-1 / 2], [3 / 2], [0]]),
                          ([[1, 4, 1], [-1, 3, 1], [-1, -1, 1]],
                           [[1], [2], [-1]], [[-0.875], [0.75], [-1.125]])])
def test_solve(a, b, solve1):
    m = solve(a, b)

    assert np.allclose(m, solve1)
