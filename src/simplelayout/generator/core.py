"""
数据生成的主要逻辑
"""


import numpy as np


def generate_matrix(
    board_grid: int, unit_grid: int, unit_n: int, positions: list
) -> np.ndarray:
    """生成指定布局矩阵

    Args:
        board_grid (int): 布局板分辨率，代表矩形区域的边长像素数
        unit_grid (int): 矩形组件分辨率
        unit_n (int): 组件数
        positions (list): 每个元素代表每个组件的位置
    Returns:
        np.ndarray: 布局矩阵
    """

    l_mat = int(board_grid / unit_grid)
    matr = np.zeros(l_mat * l_mat)
    positions = (np.array(positions)-1).tolist()
    matr[positions] = 1
    matr = matr.reshape(l_mat, l_mat)
    matr = matr.repeat([unit_grid], axis=1)
    matr = matr.repeat([unit_grid], axis=0)
    return matr
