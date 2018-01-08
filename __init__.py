import torch

class AbstractBatch(object):
    pass

class VectorBatch(AbstractBatch):
    pass

class MaskedBatch(AbstractBatch):

    def __init__(self, data, mask, dims):
        if data.dim() != mask.dim() or mask.dim() != len(dims) + 1:
            raise ValueError("malformed batch object")
        self.data = data
        self.mask = mask
        self.dims = dims