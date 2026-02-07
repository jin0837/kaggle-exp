from pathlib import Path
import shutil

from seed import set_seed
from log import get_logger
from factories.data_factory import build_datamodule
from factories.model_factory import build_model
from factories.loss_factory import build_loss
from factories.optim_factory import build_optimizer
from factories.scheduler_factory import build_scheduler
from trainer import Trainer

def run(cfg, config_path: str):
    out_dir = Path(cfg["project"]["output_dir"]) / cfg["project"]["exp_name"]
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(config_path, out_dir / "config.yaml")

    logger = get_logger(out_dir / "logs.txt")
    set_seed(cfg["system"]["seed"])

    dm = build_datamodule(cfg)
    model = build_model(cfg)
    criterion = build_loss(cfg)
    optimizer = build_optimizer(cfg, model)
    scheduler = build_scheduler(cfg, optimizer)

    trainer = Trainer(cfg, logger, out_dir)
    trainer.fit(dm, model, criterion, optimizer, scheduler)
