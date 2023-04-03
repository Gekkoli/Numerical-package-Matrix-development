__all__ = ['det', 'mult', 'adj', 'inv', 'solve']

import numpy as np


def det(a):
    """
    Given a martix `a`, return its determinat or `None` if its
    determinant does not exist.

    Parameters
    ----------
    a : np.array or list of lists
        'n x m' array

    Returns
    -------
    det : np.float64 or None
        The determinant of `a`.

    Examples
    --------
    >>> a = [[2, 0, -1], [0, 5, 6], [0, -1, 1]]
    >>> d = det(a)
    >>> d
    22.0

    >>> a = [[2, 0, -1], [0, 5, 6]]
    >>> d = det(a)
    >>> d

    >>> a = [[1, 3, 2, 4], [2, 4, 5, 2], [2, 1, 3, 3], [4, 2, 1, 6]]
    >>> d = det(a)
    >>> d
    -100.0

    Notes
    -----
    See https://en.wikipedia.org/wiki/Gaussian_elimination for further details.
    """

    x = np.array(a)  # convert list of list or ndarray to ndarray
    if x.shape[0] != x.shape[1]:  # if it was a square matrix
        return None
    else:
        det1 = 0
        if x.shape[0] >= 3:  # row number
            for i in range(x.shape[0]):
                x_copy = x.copy()
                B = np.delete(x_copy, i, axis=1)[1:, :]
                # B is (n-1)size of origin
                det1 = \
                    det1 + ((-1) ** (i + 2)) * \
                    x[0, i] * det(B)  # Recursive detB
            return float(det1)
        else:
            return float(x[0, 0] * x[1, 1] - x[0, 1] * x[1, 0])


def mult(a, b):
    """
    Given two martices `a` and `b`,
    return their multipilication
    or `None` if their
    multipilication does not exist.

    Parameters
    ----------
    a : np.array or list of lists
        'n x m' array
    b : np.array or list of lists
        'm x l' array

    Returns
    -------
    mult1 : np.ndarray or None
        The multipilication of `a` and `b`.

    Examples
    --------
    >>> a = [[1, 2], [3, 4]]
    >>> b = [[5], [6]]
    >>> d = mult(a, b)
    >>> d
    array([[17.],
           [39.]])

    >>> a = [[1, 2], [3, 4]]
    >>> b = [[5, 1], [6, 2]]
    >>> d = mult(a, b)
    >>> d
    array([[17.,  5.],
           [39., 11.]])

    Notes
    -----
    See https://en.wikipedia.org/
    wiki/Gaussian_elimination for further details.
    """

    x = np.array(a)  # convert list of list or ndarray to ndarray
    y = np.array(b)  # convert list of list or ndarray to ndarray
    if x.shape[1] != y.shape[0]:  # if it was a square matrix
        return None
    else:
        mult1 = np.zeros((x.shape[0], y.shape[1]))  # size after matrices mult.
        for j in range(y.shape[1]):     # col number
            # extension the col j of matrix b same as matrix a
            b_after = np.resize(y[:, j].T, (x.shape[0], x.shape[1]))
            # col j of result matrix fulled by mult a and b_after
            mult1[:, j] = np.sum(x * b_after, axis=1).T
        return mult1


def adj(a):
    """
    Given a martix `a`, return its adjugate matrix or `None` if its
    adjugate matrix does not exist.

    Parameters
    ----------
    a : np.array or list of lists
        'n x m' array

    Returns
    -------
    adj1 : np.ndarray or None
        The determinant of `a`.

    Examples
    --------
    >>> a = [[1,0,-1],[-2,3,0],[1,-3,2]]
    >>> d = adj(a)
    >>> d
    array([[6., 3., 3.],
           [4., 3., 2.],
           [3., 3., 3.]])

    >>> a = [[1,5,-1],[-2,3,0],[1,-8,2]]
    >>> d = adj(a)
    >>> d
    array([[ 6., -2.,  3.],
           [ 4.,  3.,  2.],
           [13., 13., 13.]])

    Notes
    -----
    See https://en.wikipedia.org/
    wiki/Gaussian_elimination for further details.
    """

    x1 = np.array(a)  # convert list of list or ndarray to ndarray
    if x1.shape[0] != x1.shape[1]:  # if it was a square matrix
        return None
    else:
        adj_b = np.zeros((x1.shape[0], x1.shape[1]))
        for i in range(x1.shape[0]):
            for j in range(x1.shape[1]):
                adj_b_copy = a.copy()
                # delete twice form (n-1)size matrix for calculate det
                adj_b[i, j] = \
                    ((-1) ** (i + j)) * \
                    det(np.delete(np.delete(adj_b_copy, i, axis=0), j, axis=1))
                adj1 = np.transpose(adj_b)
        return adj1


def inv(a):
    """
    Given a martix `a`, return its inverse matrix or `None` if its
    inverse matrix does not exist.

    Parameters
    ----------
    a : np.array or list of lists
        'n x m' array

    Returns
    -------
    a_inv : np.ndarray or None
        The determinant of `a`.

    Examples
    --------
    >>> a = [[1,0,-1],[-2,3,0],[1,-3,2]]
    >>> d = inv(a)
    >>> d
    array([[2.        , 1.        , 1.        ],
           [1.33333333, 1.        , 0.66666667],
           [1.        , 1.        , 1.        ]])

    >>> a = [[1,3,-1],[-2,2,0],[1,-7,2]]
    >>> d = inv(a)
    >>> d
    array([[1.  , 0.25, 0.5 ],
           [1.  , 0.75, 0.5 ],
           [3.  , 2.5 , 2.  ]])

    Notes
    -----
    See https://en.wikipedia.org/
    wiki/Gaussian_elimination for further details.
    """

    x = np.array(a)  # convert list of list or ndarray to ndarray
    if det(x) == 0:  # Avoid division by 0 when calculate inverse matrix
        return None
    else:
        a_inv = adj(x) / det(x)
        return a_inv


def solve(a, b):
    """
    Given two martices `a` and `b`,
    for a linear system composed of them form ax = b,
    return its solution x  or `None` if its cannot be solved.

    Parameters
    ----------
    a : np.array or list of lists
        'n x m' array
    b : np.array or list of lists
        'n x 1' array

    Returns
    -------
    det_b : np.ndarray or None
        The determinant of `a`.

    Examples
    --------
    >>> a = [[1, 1, 1], [-1, 1, 1],[-1, -1, 1]]
    >>> b = [[1], [2], [-1]]
    >>> d = solve(a, b)
    >>> d
    array([[-0.5],
           [ 1.5],
           [ 0. ]])

    >>> a = [[1, 4, 1], [-1, 3, 1],[-1, -1, 1]]
    >>> b = [[1], [2], [-1]]
    >>> d = solve(a, b)
    >>> d
    array([[-0.875],
           [ 0.75 ],
           [-1.125]])

    Notes
    -----
    See https://en.wikipedia.org/
    wiki/Gaussian_elimination for further details.
    """

    x = np.array(a)  # convert list of list or ndarray to ndarray
    y = np.array(b)  # convert list of list or ndarray to ndarray
    det_b = np.zeros((1, len(y)))
    if det(x) == 0:  # Avoid division by 0
        return None
    else:
        for j in range(x.shape[1]):
            x_copy = x.copy()
            x_copy[:, j] = y.reshape((1, len(y)))  # use col j to replace
            det_b[0, j] = det(x_copy)
        det_b = det_b / det(x)
        return det_b.reshape(len(y), 1)
