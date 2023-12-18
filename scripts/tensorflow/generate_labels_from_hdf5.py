import h5py
import json


def read_hdf5(file_path):
    with h5py.File(file_path, 'r') as hdf:
        # Assuming structure: /dataset/annotations and /dataset/images
        annotations = hdf['/dataset/annotations'][()]
        images = hdf['/dataset/images'][()]

    return annotations, images


def convert_annotations(annotations, images):
    converted_annotations = []
    for annotation in annotations:
        image_id = annotation['image_id']
        image_file = images[image_id].decode('utf-8')  # Assuming image filenames are encoded in bytes
        bbox = annotation['bbox']  # Ensure this matches TensorFlow's expected format
        label = annotation['label']

        converted_annotations.append({
            'filename': image_file,
            'bbox': bbox,
            'label': label
        })
    return converted_annotations


def write_annotations_to_file(annotations, output_path):
    with open(output_path, 'w') as file:
        json.dump(annotations, file, indent=4)


def main():
    hdf5_file_path = '../../output/labels/file.hdf5'
    output_file_path = '../../output/file.json'

    annotations, images = read_hdf5(hdf5_file_path)
    converted_annotations = convert_annotations(annotations, images)
    write_annotations_to_file(converted_annotations, output_file_path)


if __name__ == "__main__":
    main()
