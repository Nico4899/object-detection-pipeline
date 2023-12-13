import json
import numpy as np

from PIL import Image
from blenderproc.python.writer import CocoWriterUtility

data_path = "/../../data/images_and_labels"
coco_path = data_path + "/annotations_base_all.json"
with open(coco_path, "r") as file:
    coco_anno = json.load(file)

annotations = coco_anno["annotations"]
for annotation in annotations:
    image_id = annotation["image_id"]
    rle = annotation["segmentation"]
    binary_mask = CocoWriterUtility.rle_to_binary_mask(rle)
    binary_mask = np.array(binary_mask, dtype=np.uint8)*255

    # Convert to binary mask arry to grayscale image
    mask_image_gray = Image.fromarray(binary_mask)

    # Convert the grayscale image to RGB
    mask_image_rgb = mask_image_gray.convert("RGB")
    mask_image_rgb.save(data_path + f"/mask/{image_id}.png")


