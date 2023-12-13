import os
from object_detection import model_lib_v2

dir_path = os.path.dirname(__file__)
data_path = os.path.join(dir_path, "../../data")
model_path = os.path.join(dir_path, "../../model")

config_path = os.path.join(data_path, "pipeline.config")
model_dir = os.path.join(model_path, "mask_rcnn_inception_resnet_v2_checkpoint")

if __name__ == '__main__':
    model_lib_v2.train_loop(
        pipeline_config_path=config_path,
        model_dir=model_dir,
        train_steps=10,
        use_tpu=False,
        checkpoint_every_n=1,
        record_summaries=True,
        save_final_config=True,
        total_loss_thresh=0.0)