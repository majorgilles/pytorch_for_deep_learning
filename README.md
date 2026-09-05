# PyTorch for Deep Learning

A personal, runnable companion repository for DeepLearning.AI's [PyTorch for Deep Learning Professional Certificate](https://www.deeplearning.ai/specializations/pytorch-for-deep-learning-professional-certificate), taught by Laurence Moroney.

Use the [DeepLearning.AI learning platform](https://learn.deeplearning.ai/specializations/pytorch-for-deep-learning-professional-certificate/lesson) for all course content. This repository contains only original notes, experiments, and implementations.

## Table of contents

1. [Course 1 — PyTorch: Fundamentals](#course-1--pytorch-fundamentals)
2. [Course 2 — PyTorch: Techniques and Ecosystem Tools](#course-2--pytorch-techniques-and-ecosystem-tools)
3. [Course 3 — PyTorch: Advanced Architectures and Deployment](#course-3--pytorch-advanced-architectures-and-deployment)
4. [Run the notebooks](#run-the-notebooks)

---

## Course 1 — PyTorch: Fundamentals

### Week 1 — Getting Started with PyTorch

- [**Notes**](weeks/c1_w1/README.md) — Tensors, devices, operations, and PyTorch's core programming model.
- [**Notebook**](weeks/c1_w1/c1_w1_getting-started-with-pytorch.ipynb) · [Issue #1](https://github.com/majorgilles/pytorch_for_deep_learning/issues/1)

### Week 2 — The PyTorch Workflow

- [**Notes**](weeks/c1_w2/README.md) — Models, losses, optimizers, gradients, evaluation, and saving.
- [**Notebook**](weeks/c1_w2/c1_w2_the-pytorch-workflow.ipynb) · [Issue #2](https://github.com/majorgilles/pytorch_for_deep_learning/issues/2)

### Week 3 — Data Management in PyTorch

- [**Notes**](weeks/c1_w3/README.md) — Datasets and repeatable batches with `Dataset` and `DataLoader`.
- [**Notebook**](weeks/c1_w3/c1_w3_data-management-in-pytorch.ipynb) · [Issue #3](https://github.com/majorgilles/pytorch_for_deep_learning/issues/3)

### Week 4 — Core Neural Network Components

- [**Notes**](weeks/c1_w4/README.md) — Layers, activations, losses, and convolutional components.
- [**Notebook**](weeks/c1_w4/c1_w4_core-neural-network-components.ipynb) · [Issue #4](https://github.com/majorgilles/pytorch_for_deep_learning/issues/4)

---

## Course 2 — PyTorch: Techniques and Ecosystem Tools

### Week 1 — Hyperparameter Optimization

- [**Notes**](weeks/c2_w1/README.md) — Optimizers, schedulers, experiment tuning, and model performance.
- [**Notebook**](weeks/c2_w1/c2_w1_hyperparameter-optimization.ipynb) · [Issue #5](https://github.com/majorgilles/pytorch_for_deep_learning/issues/5)

### Week 2 — Working with Images using TorchVision

- [**Notes**](weeks/c2_w2/README.md) — Loading, transforming, augmenting, and classifying images.
- [**Notebook**](weeks/c2_w2/c2_w2_working-with-images-using-torchvision.ipynb) · [Issue #6](https://github.com/majorgilles/pytorch_for_deep_learning/issues/6)

### Week 3 — Working with Text using Hugging Face

- [**Notes**](weeks/c2_w3/README.md) — Text preprocessing and fine-tuning PyTorch-based Hugging Face models.
- [**Notebook**](weeks/c2_w3/c2_w3_working-with-text-using-hugging-face.ipynb) · [Issue #7](https://github.com/majorgilles/pytorch_for_deep_learning/issues/7)

### Week 4 — Efficient Training Pipelines

- [**Notes**](weeks/c2_w4/README.md) — Profiling input and training pipelines and removing bottlenecks.
- [**Notebook**](weeks/c2_w4/c2_w4_efficient-training-pipelines.ipynb) · [Issue #8](https://github.com/majorgilles/pytorch_for_deep_learning/issues/8)

---

## Course 3 — PyTorch: Advanced Architectures and Deployment

### Week 1 — Designing Custom Architectures

- [**Notes**](weeks/c3_w1/README.md) — Siamese networks, ResNet, DenseNet, and other non-sequential architectures.
- [**Notebook**](weeks/c3_w1/c3_w1_designing-custom-architectures.ipynb) · [Issue #9](https://github.com/majorgilles/pytorch_for_deep_learning/issues/9)

### Week 2 — Specialized Approaches to Vision in PyTorch

- [**Notes**](weeks/c3_w2/README.md) — Saliency, activation maps, diffusion, and vision-model interpretation.
- [**Notebook**](weeks/c3_w2/c3_w2_specialized-approaches-to-vision-in-pytorch.ipynb) · [Issue #10](https://github.com/majorgilles/pytorch_for_deep_learning/issues/10)

### Week 3 — Specialized Approaches to Natural Language Processing in PyTorch

- [**Notes**](weeks/c3_w3/README.md) — Attention and Transformer components for language tasks.
- [**Notebook**](weeks/c3_w3/c3_w3_specialized-approaches-to-natural-language-processing-in-pytorch.ipynb) · [Issue #11](https://github.com/majorgilles/pytorch_for_deep_learning/issues/11)

### Week 4 — Preparing Models for Deployment in PyTorch

- [**Notes**](weeks/c3_w4/README.md) — Exporting, tracking, pruning, and quantizing models.
- [**Notebook**](weeks/c3_w4/c3_w4_preparing-models-for-deployment-in-pytorch.ipynb) · [Issue #12](https://github.com/majorgilles/pytorch_for_deep_learning/issues/12)

---

## Run the notebooks

This repository uses [uv](https://docs.astral.sh/uv/):

```bash
uv sync --dev
uv run pytest
```

Open a notebook in VS Code or Jupyter and select the repository's `.venv` interpreter. PyTorch and TorchVision use the CUDA 12.8 package index but still run on CPU when CUDA is unavailable.

## Repository layout

- `weeks/c<course>_w<week>/` — notes and a notebook for each course week.
- `src/pytorch_for_deep_learning/` — reusable code extracted from experiments.
- `tests/` — small reproducibility and behavior checks.

## Source-material policy

DeepLearning.AI course materials remain on the official platform. Do not commit downloaded lessons, solution notebooks, datasets, credentials, model weights, or generated training outputs unless their license explicitly permits redistribution.
