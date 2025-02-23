# coding=utf-8
from __future__ import absolute_import, division, print_function

import numpy as np

from .. import PixelCollection
from .utils import TransformationBase


class Image(TransformationBase):

    def transform(self, pixels):
        data = pixels.data
        (count, _, _) = data.shape

        if 3 > count > 4:
            raise Exception("Source data must be 3 or 4 bands")

        if data.dtype == np.float32:
            # data was normalized; expand it
            data *= np.iinfo(np.uint8).max

        if count == 4:
            rgba = np.ma.transpose(data.astype(np.uint8), [1, 2, 0])
            return PixelCollection(rgba, pixels.bounds), "RGBA"

        rgb = np.ma.transpose(data.astype(np.uint8), [1, 2, 0])
        if data.mask.any():
            a = np.logical_and.reduce(~data.mask).astype(np.uint8) * 255
        else:
            a = np.full((rgb.shape[:-1]), 255, np.uint8)

        return PixelCollection(np.dstack((rgb, a)), pixels.bounds), "RGBA"
