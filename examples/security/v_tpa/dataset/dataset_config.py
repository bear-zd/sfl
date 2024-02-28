#!/usr/bin/env python
# coding=utf-8
import sys

sys.path.append(".")

from .badnets_cifar_dataset import BadNetsCIFARDataset
from .badnets_mnist_dataset import BadNetsMNISTDataset
from .badnets_nuswide_dataset import BadNetsNUSWIDEDataset
from .cifar_dataset import CIFARDataset
from .mirror_cifar_dataset import MirrorCIFARDataset
from .mirror_mnist_dataset import MirrorMNISTDataset
from .mirror_nuswide_dataset import MirrorNUSWIDEDataset
from .mnist_dataset import MNISTDataset
from .nuswide_dataset import NUSWIDEDataset

DATASETS = {
    "cifar10": {
        "data_path": "<local dataset path>",  # change to the local dataset directory
        "normal": CIFARDataset,
        "mirror": MirrorCIFARDataset,
        "badnets": BadNetsCIFARDataset,
        "args": {"target_class": None},
    },
    "mnist": {
        "data_path": "<local dataset path>",  # change to the local dataset directory
        "normal": MNISTDataset,
        "mirror": MirrorMNISTDataset,
        "badnets": BadNetsMNISTDataset,
        "args": {"target_class": None},
    },
    "nus-wide": {
        "data_path": "<local dataset path>",  # change to the local dataset directory
        "normal": NUSWIDEDataset,
        "mirror": MirrorNUSWIDEDataset,
        "badnets": BadNetsNUSWIDEDataset,
        "args": {"target_class": 1},
    },
}
