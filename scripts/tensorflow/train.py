import os
import argparse
from object_detection import model_lib_v2


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--train_steps', type=int, default=10000)
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_arguments()
    train_steps = args.train_steps

    dir_path = os.path.dirname(__file__)
    data_path = os.path.join(dir_path, "../../data")
    model_path = os.path.join(dir_path, "../../model")

    config_path = os.path.join(data_path, "pipeline.config")
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Config file not found at {config_path}")

    model_dir = os.path.join(model_path, "mask_rcnn_inception_resnet_v2_checkpoint")
    os.makedirs(model_dir, exist_ok=True)

    model_lib_v2.train_loop(
        pipeline_config_path=config_path,
        model_dir=model_dir,
        train_steps=train_steps,
        use_tpu=False,
        checkpoint_every_n=1,
        record_summaries=True,
        save_final_config=True,
        total_loss_thresh=0.0)
