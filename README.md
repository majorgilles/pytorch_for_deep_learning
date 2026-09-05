    # PyTorch for Deep Learning

    A personal, runnable companion repository for DeepLearning.AI's [PyTorch for Deep Learning Professional Certificate](https://www.deeplearning.ai/specializations/pytorch-for-deep-learning-professional-certificate), taught by Laurence Moroney.

    Use the [DeepLearning.AI learning platform](https://learn.deeplearning.ai/specializations/pytorch-for-deep-learning-professional-certificate/lesson) for all course content. This repository contains only original notes, experiments, and implementations.

    ## Curriculum

    | Module | Topic | Notes | Notebook | Issue |
    |---|---|---|---|---|
    | 1.1 | Getting Started with PyTorch | [Notes](modules/c1_m1/README.md) | [Notebook](modules/c1_m1/c1_m1_getting-started-with-pytorch.ipynb) | [#1](https://github.com/majorgilles/pytorch_for_deep_learning/issues/1) |
| 1.2 | The PyTorch Workflow | [Notes](modules/c1_m2/README.md) | [Notebook](modules/c1_m2/c1_m2_the-pytorch-workflow.ipynb) | [#2](https://github.com/majorgilles/pytorch_for_deep_learning/issues/2) |
| 1.3 | Data Management in PyTorch | [Notes](modules/c1_m3/README.md) | [Notebook](modules/c1_m3/c1_m3_data-management-in-pytorch.ipynb) | [#3](https://github.com/majorgilles/pytorch_for_deep_learning/issues/3) |
| 1.4 | Core Neural Network Components | [Notes](modules/c1_m4/README.md) | [Notebook](modules/c1_m4/c1_m4_core-neural-network-components.ipynb) | [#4](https://github.com/majorgilles/pytorch_for_deep_learning/issues/4) |
| 2.1 | Hyperparameter Optimization | [Notes](modules/c2_m1/README.md) | [Notebook](modules/c2_m1/c2_m1_hyperparameter-optimization.ipynb) | [#5](https://github.com/majorgilles/pytorch_for_deep_learning/issues/5) |
| 2.2 | Working with Images using TorchVision | [Notes](modules/c2_m2/README.md) | [Notebook](modules/c2_m2/c2_m2_working-with-images-using-torchvision.ipynb) | [#6](https://github.com/majorgilles/pytorch_for_deep_learning/issues/6) |
| 2.3 | Working with Text using Hugging Face | [Notes](modules/c2_m3/README.md) | [Notebook](modules/c2_m3/c2_m3_working-with-text-using-hugging-face.ipynb) | [#7](https://github.com/majorgilles/pytorch_for_deep_learning/issues/7) |
| 2.4 | Efficient Training Pipelines | [Notes](modules/c2_m4/README.md) | [Notebook](modules/c2_m4/c2_m4_efficient-training-pipelines.ipynb) | [#8](https://github.com/majorgilles/pytorch_for_deep_learning/issues/8) |
| 3.1 | Designing Custom Architectures | [Notes](modules/c3_m1/README.md) | [Notebook](modules/c3_m1/c3_m1_designing-custom-architectures.ipynb) | [#9](https://github.com/majorgilles/pytorch_for_deep_learning/issues/9) |
| 3.2 | Specialized Approaches to Vision in PyTorch | [Notes](modules/c3_m2/README.md) | [Notebook](modules/c3_m2/c3_m2_specialized-approaches-to-vision-in-pytorch.ipynb) | [#10](https://github.com/majorgilles/pytorch_for_deep_learning/issues/10) |
| 3.3 | Specialized Approaches to Natural Language Processing in PyTorch | [Notes](modules/c3_m3/README.md) | [Notebook](modules/c3_m3/c3_m3_specialized-approaches-to-natural-language-processing-in-pytorch.ipynb) | [#11](https://github.com/majorgilles/pytorch_for_deep_learning/issues/11) |
| 3.4 | Preparing Models for Deployment in PyTorch | [Notes](modules/c3_m4/README.md) | [Notebook](modules/c3_m4/c3_m4_preparing-models-for-deployment-in-pytorch.ipynb) | [#12](https://github.com/majorgilles/pytorch_for_deep_learning/issues/12) |

    ## Setup

    This project uses [uv](https://docs.astral.sh/uv/):

    ```bash
    uv sync --dev
    uv run pytest
    ```

    Open a notebook in VS Code or Jupyter and select the repository's `.venv` interpreter.

    PyTorch and TorchVision use the CUDA 12.8 package index. PyTorch will still run on CPU when CUDA is unavailable.

    ## Repository layout

    - `modules/` — one notes file and starter notebook per course module.
    - `src/pytorch_for_deep_learning/` — reusable code extracted from experiments.
    - `tests/` — small reproducibility and behavior checks.

    ## Source-material policy

    DeepLearning.AI course materials remain on the official platform. Do not commit downloaded lessons, solution notebooks, datasets, credentials, model weights, or generated training outputs unless their license explicitly permits redistribution.
