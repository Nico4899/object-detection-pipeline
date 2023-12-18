import json
import os
from tf_record_generation.record_generation.tf_record_generator import TfRecordGenerator
from tf_record_generation.models.object_detection_region import ObjectDetectionRegion


def convert_annotations_to_regions(annotations):
    regions_list = []
    for annotation in annotations:
        # Ensure your bbox format matches the expected format in ObjectDetectionRegion
        bbox = annotation["bbox"]
        label_class = annotation["category_id"]
        region = ObjectDetectionRegion(*bbox, label_class)
        regions_list.append(region)
    return regions_list


def load_annotations(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Annotation file not found at {file_path}")

    with open(file_path, 'r') as f:
        return json.load(f)


def main():
    # Paths
    annotations_file = '../../data/images_and_labels/annotations/sample_annotations.json'
    label_map_path = '../../data/data_pu_cropped/label_map.pbtxt'
    tf_record_file_name = 'output.tfrecord'

    try:
        annotations_data = load_annotations(annotations_file)
    except Exception as e:
        print(f"Error loading annotations: {e}")
        return

    image_file_names = [entry['file_name'] for entry in annotations_data['images']]
    regions_list = convert_annotations_to_regions(annotations_data['annotations'])

    # Initialize and call the TfRecordGenerator
    tf_record_generator = TfRecordGenerator(label_map_file_name=label_map_path)
    try:
        tf_record_generator(tf_record_file_name=tf_record_file_name,
                            image_file_names=image_file_names,
                            regions_list=[regions_list])
    except Exception as e:
        print(f"Error generating TFRecord: {e}")


if __name__ == "__main__":
    main()
