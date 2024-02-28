#!/usr/bin/env python
# coding=utf-8
import sys

sys.path.append("..")

import numpy as np
import torch.nn.functional as F
from torch import nn, optim


class PassiveModel(nn.Module):
    def __init__(self, input_shape, output_shape):
        super().__init__()
        self.linear1 = nn.Linear(np.prod(input_shape), 32)
        self.linear2 = nn.Linear(32, output_shape)

    def forward(self, x):
        x = F.relu(self.linear1(x))
        x = self.linear2(x)
        return x


def get_passive_model(input_shape, output_shape):
    return PassiveModel(input_shape, output_shape)


def get_optimizer(lr, params):
    return optim.SGD(params, lr=lr)
