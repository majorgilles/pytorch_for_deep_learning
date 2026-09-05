import torch

from pytorch_for_deep_learning import available_device


def test_available_device_is_usable() -> None:
    device = available_device()
    tensor = torch.tensor([1.0], device=device)

    assert tensor.item() == 1.0
    assert device.type in {"cpu", "cuda"}
