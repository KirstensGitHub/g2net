from pathlib import Path
from common.utils import get_datetime_version

def get():
    PROJECT_ROOT = Path(__file__).resolve().parents[2]
    DATA_ROOT = PROJECT_ROOT.joinpath("datasets")

    metadata_config = {
        "model_name": "baseline",
        "version": get_datetime_version()
    }

    dataloader_config = {
        # Set path variables for convenience
        "data_path": DATA_ROOT.joinpath("train"),
        "labels_path": DATA_ROOT.joinpath("training_labels.csv"),
        "test_data_path": DATA_ROOT.joinpath("test"),
        "test_labels_path": DATA_ROOT.joinpath("sample_submission.csv"),

        "seed": 10,
        "val_ratio": 0.2,
        "batch_size": 64,
        "num_workers": 0,
    }

    model_config = {
        "resnet_pretrain": False,
    }

    policy_config = {
        "loss_fn": "BCELoss",
        "optimizer": "Adam",
    }

    logging_config = {
        "use_wandb": True,
        "name": "baseline",
        "tags": [metadata_config["version"]],
        "project": "molecular-translation",
        "entity": "dmlg"
    }

    trainer_config = {
        "gpus": 1,
        "auto_select_gpus": True,

        "min_epochs": 0,
        "max_epochs": 200,
        "val_check_interval": 1000,

        "resume_from_checkpoint": None,
        "fast_dev_run": False,
        "deterministic": False
    }

    checkpoint_config = {
        "save_checkpoint": True,
        "save_dir": PROJECT_ROOT.joinpath("checkpoints",
                                          metadata_config["model_name"],
                                          metadata_config["version"]),
        "monitor": "val/loss",
        "mode": "min",
        "save_last": True,
        "save_top_k": 3,
        "every_n_train_steps": 1001
    }

    return metadata_config, dataloader_config, model_config, policy_config, logging_config, trainer_config, checkpoint_config