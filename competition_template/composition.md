train.py (固定)
  └─ cfg = load_config(path)
  └─ run(cfg)

runner.py
  └─ set_seed(cfg)
  └─ out_dir = prepare_output(cfg)
  └─ logger = build_logger(out_dir)
  └─ dm = build_datamodule(cfg)      # DataLoader群
  └─ model = build_model(cfg)
  └─ criterion = build_loss(cfg)
  └─ optimizer = build_optimizer(cfg, model)
  └─ scheduler = build_scheduler(cfg, optimizer)
  └─ trainer = build_trainer(cfg, ...)
  └─ trainer.fit(...)
