from typing import Sequence
import numpy as np
from .transforms import BboxBase

def affine_transform(points: np.ndarray, trans: np.ndarray) -> np.ndarray: ...
def count_bboxes_overlapping_bbox(a: BboxBase, bboxes: Sequence[BboxBase]) -> int: ...
def update_path_extents(*args, **kwargs): ...
