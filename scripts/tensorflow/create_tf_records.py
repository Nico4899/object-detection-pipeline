from tf_record_generation.record_generation.tf_record_generator import TfRecordGenerator
from tf_record_generation.models.object_detection_region import ObjectDetectionRegion
import json


def convert_annotations_to_regions(annotations):
    regions_list = []
    for annotation in annotations:
        bbox = annotation["bbox"]
        label_class = annotation["category_id"]
        region = ObjectDetectionRegion(*bbox, label_class)
        regions_list.append(region)
    return regions_list


def main():
    # Load annotations from JSON file
    with open('../../data/images_and_labels/annotations/sample_annotations.json', 'r') as f:
        annotations_data = json.load(f)

    # Paths
    label_map_path = '../../data/data_pu_cropped/label_map.pbtxt'
    tf_record_file_name = 'output.tfrecord'
    image_file_names = [entry['file_name'] for entry in annotations_data['images']]

    # Convert annotations to ObjectDetectionRegion instances
    regions_list = convert_annotations_to_regions(annotations_data['annotations'])

    # Initialize and call the TfRecordGenerator
    tf_record_generator = TfRecordGenerator(label_map_file_name=label_map_path)
    tf_record_generator(tf_record_file_name=tf_record_file_name,
                        image_file_names=image_file_names,
                        regions_list=[regions_list])


if __name__ == "__main__":
    main()
