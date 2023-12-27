# Object Detection of Packaging Units

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)
- [Authors and Acknowledgment](#authors-and-acknowledgment)
- [FAQs](#faqs)

## Installation

### Prerequisites

- Python 3.6 or later
- TensorFlow (Version 2.x)
- Blenderproc

### Installing

Clone the repository and install the required dependencies:

```bash
git clone https://lsogit.fzi.de/doerr/hiwi_fliegel.git
cd yourproject
pip install -r requirements.txt
```

## Usage

After installation, you can run the object detection module as follows:
```bash
python object_detection.py
```

## Features

- Object detection using TensorFlow's state-of-the-art algorithms.
- Dynamic rendering of 3D packaging units using Blenderproc.
- Customizable settings for different types of packaging units.
- Integration of TensorFlow and Blenderproc for enhanced accuracy.

## Contributing
We welcome contributions. If you want to contribute:

```bash
# Fork the Repository
# Create your Feature Branch
git checkout -b feature/YourAmazingFeature

# Commit your Changes
git commit -m 'Add some YourAmazingFeature'

# Push to the Branch
git push origin feature/YourAmazingFeature

# Open a Pull Request
```

## License

MIT LICENCE

## Authors and Acknowledgment
Thank you to all contributors and maintainers of this project.

Nicolas Fliegel - [GitHub Profile](https://github.com/Nico4899)

## FAQs

1. How do I integrate my own packaging unit models into the pipeline?
    - Follow the guidelines in the usage section and refer to the technical details for model integration.
2. Can I use this project with different versions of TensorFlow or Blenderproc?
   - The project is optimized for TensorFlow 2.x and the latest version of Blenderproc. Compatibility with other versions is not guaranteed.
