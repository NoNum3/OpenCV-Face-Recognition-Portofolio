# Real-time Face Recognition System

This project was created as a part of the final exam for the university course by:

- **陳英全 (Kenny Stevens)**
  ![Kenny Stevens](url_to_kenny_stevens_picture)

- **翁海平 (Kai Wijaya)**
  ![Kai Wijaya](url_to_kai_wijaya_picture)

## Table of Contents

- [Features](#features)
- [System Components](#system-components)
  - [1. Data Collection](#1-data-collection)
  - [2. Model Training](#2-model-training)
  - [3. Face Recognition](#3-face-recognition)
- [Usage](#usage)
- [Configuration](#configuration)
- [License](#license)
- [Acknowledgments](#acknowledgments)
- [Contribution](#contribution)

## Features

- Face data collection
- Model training
- Real-time face recognition
- Confidence level display
- Unknown face handling

## System Components

### 1. Data Collection

- Capture 30 grayscale images for each face.
- Image size: 257x257.
- File naming: `dataset.[id].[image_count_each_id]`.

### 2. Model Training

- Convert images to grayscale.
- Process images (resize, normalize, etc.).
- Use OpenCV for training.
- Save the trained model as `trainer.yml`.

### 3. Face Recognition

- Load the pre-trained model (`trainer.yml`).
- Create an ID-to-name mapping for recognition.
- Initialize the camera for real-time recognition.
- Capture and detect faces in video frames.
- Display recognized names and confidence levels.
- Mark unknown faces as "Unknown."
- Display real-time video feed with recognized names and confidence levels.

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/face-recognition.git
    cd face-recognition
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the application:

    ```bash
    python main.py
    ```

## Configuration

- Adjust confidence threshold in the code (`confidence_threshold = 80`).
- Modify image processing parameters if needed.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- Mention any libraries or resources used.
- Credit the source of the pre-trained model.

## Contribution

Contributions are welcome! Please follow the [contribution guidelines](CONTRIBUTING.md).
