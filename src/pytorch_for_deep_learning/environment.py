"""Small environment helpers used across notebooks."""

import torch


def available_device() -> torch.device:
    """Return a CUDA device when available, otherwise CPU."""
    return torch.device("cuda" if torch.cuda.is_available() else "cpu")
