project:
  exp_name: "exp001_baseline"
  output_dir: "experiments"

system:
  seed: 42
  device: "cuda"
  num_workers: 4
  amp: true

data:
  name: "image_folder"     # datamoduleの種類
  params:
    train_dir: "input/train"
    valid_dir: "input/valid"
    img_size: 224
    batch_size: 32
    shuffle: true

augment:
  name: "basic"            # augの種類
  params:
    hflip: 0.5
    color_jitter: 0.2

model:
  name: "resnet50"         # model種類
  params:
    pretrained: true
    num_classes: 10

loss:
  name: "cross_entropy"    # loss種類
  params:
    label_smoothing: 0.0
    class_weights: null    # [1.0, 2.0, ...] or null

optim:
  name: "adamw"
  params:
    lr: 0.0003
    weight_decay: 0.01

scheduler:
  name: "cosine"
  params:
    warmup_epochs: 1
    min_lr: 1.0e-6

train:
  epochs: 10
  grad_clip: 1.0
  log_every: 50
  eval_every: 1
  save_best: "metric"      # "loss" or "metric"
  metric: "accuracy"
