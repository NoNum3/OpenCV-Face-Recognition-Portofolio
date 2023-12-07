[English](#english-version) | [中文](#中文)

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

### [中文](#中文)

# 實時人臉辨識系統

本專案是大學期末考試的一部分，由以下成員製作：

- **陳英全 (Kenny Stevens)**
  ![Kenny Stevens](url_to_kenny_stevens_picture)

- **翁海平 (Kai Wijaya)**
  ![Kai Wijaya](url_to_kai_wijaya_picture)

## 目錄

- [功能](#功能)
- [系統組件](#系統組件)
  - [1. 資料收集](#1-資料收集)
  - [2. 模型訓練](#2-模型訓練)
  - [3. 人臉辨識](#3-人臉辨識)
- [使用方法](#使用方法)
- [設定](#設定)
- [專案製作者](#專案製作者)
- [授權](#授權)
- [致謝](#致謝)
- [貢獻](#貢獻)

## 功能

- 人臉資料收集
- 模型訓練
- 實時人臉辨識
- 信心水平顯示
- 未知人臉處理

## 系統組件

### 1. 資料收集

- 對每個人臉捕捉 30 張灰階圖片。
- 圖片大小：257x257。
- 檔案命名：`dataset.[id].[image_count_each_id]`。

### 2. 模型訓練

- 將圖片轉換為灰階。
- 處理圖片（調整大小，正規化，等等）。
- 使用 OpenCV 進行訓練。
- 將已訓練的模型儲存為 `trainer.yml`。

### 3. 人臉辨識

- 載入已訓練的模型（`trainer.yml`）。
- 創建 ID 到姓名的對應表進行辨識。
- 初始化攝像頭以進行實時人臉辨識。
- 即時捕捉和檢測視訊幀中的人臉。
- 使用已訓練的模型進行人臉辨識。
- 如果置信度 > 80%，顯示已辨識的姓名和置信度。
- 對於無法識別的人臉，標記為 "未知"。
- 顯示實時視頻鏈路，顯示已辨識的姓名和置信度水平。
- 如果置信度低於 80%，標記為 "未知"。

## 使用方法

1. 克隆存儲庫：

   ```bash
   git clone https://github.com/your-username/face-recognition.git
   cd face-recognition
   ```

2. 安裝依賴：

   ```bash
   pip install -r requirements.txt
   ```

3. 運行應用程序：

   ```bash
   python main.py
   ```

## 設定

- 在代碼中調整置信度閾值（`confidence_threshold = 80`）。
- 如果需要，修改圖片處理參數。

# 專案製作者

此專案是大學期末考試的一部分，由以下成員製作：

- **陳英全 (Kenny Stevens)**
  ![Kenny Stevens](url_to_kenny_stevens_picture)

- **翁海平 (Kai Wijaya)**
  ![Kai Wijaya](url_to_kai_wijaya_picture)

## 目錄

- [功能](#功能)
- [系統組件](#系統組件)
  - [1. 資料收集](#1-資料收集)
  - [2. 模型訓練](#2-模型訓練)
  - [3. 人臉辨識](#3-人臉辨識)
- [使用方法](#使用方法)
- [設定](#設定)
- [授權](#授權)
- [致謝](#致謝)
- [貢獻](#貢獻)

## 功能

- 人臉資料收集
- 模型訓練
- 實時人臉辨識
- 信心水平顯示
- 未知人臉處理

## 系統組件

### 1. 資料收集

- 對每個人臉捕捉 30 張灰階圖片。
- 圖片大小：257x257。
- 檔案命名：`dataset.[id].[image_count_each_id]`。

### 2. 模型訓練

- 將圖片轉換為灰階。
- 處理圖片（調整大小，正規化，等等）。
- 使用 OpenCV 進行訓練。
- 將已訓練的模型儲存為 `trainer.yml`。

### 3. 人臉辨識

- 載入已訓練的模型（`trainer.yml`）。
- 創建 ID 到姓名的對應表進行辨識。
- 初始化攝像頭以進行實時人臉辨識。
- 即時捕捉和檢測視訊幀中的人臉。
- 使用已訓練的模型進行人臉辨識。
- 如果置信度 > 80%，顯示已辨識的姓名和置信度。
- 對於無法識別的人臉，標記為 "未知"。
- 顯示實時視頻鏈路，顯示已辨識的姓名和置信度水平。
- 如果置信度低於 80%，標記為 "未知"。

## 使用方法

1. 克隆存儲庫：

   ```bash
   git clone https://github.com/your-username/face-recognition.git
   cd face-recognition
   ```

2. 安裝依賴：

   ```bash
   pip install -r requirements.txt
   ```

3. 運行應用程序：

   ```bash
   python main.py
   ```

## 設定

- 在代碼中調整置信度閾值（`confidence_threshold = 80`）。
- 如果需要，修改圖片處理參數。

## 授權

本專案使用 [MIT 授權](LICENSE)。

## 致謝

- 提及使用的任何庫或資源。
- 聲明預訓練模型的來源。

## 貢獻

歡迎貢獻！請遵從 [貢獻指南](CONTRIBUTING.md)。
