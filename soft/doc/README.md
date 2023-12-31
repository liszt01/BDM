## Setting Up the Development Environment

### 1. Create and Activate a Virtual Environment


```bash
# Create a virtual environment
# Python 3.10 is recommended due to [pytorch support](https://stackoverflow.com/questions/75417119/how-to-find-what-is-the-latest-version-of-python-that-pytorch)
# To install python3.10 in Ubuntu, run following command:
# sudo add-apt-repository ppa:deadsnakes/ppa
# sudo apt install python3.10
# sudo apt install python3.10-venv
python3.10 -m venv .bdm-env

# Activate the virtual environment
source .bdm-env/bin/activate
```

#### Download YOLO Model

Download the yolov8n.pt file from [the official Ultralytics YOLOv8 documentation](https://docs.ultralytics.com/models/yolov8/#supported-modes) and place it in the `model/` directory of this repository.

### 2. Install Dependencies

```bash
python3 -m pip install -r requirements.txt
```

### 3. Launch the Application

```bash
cd src
flask run -h 0.0.0.0 -p 8000
```

To access the laptop camera using OpenCV, ensure that the camera access is granted to the development environment, such as VSCode, through the system settings' privacy & security.

### Granting Camera Access on macOS

1. Open **System Settings**.
2. Navigate to **Privacy & Security**.
4. Choose **Camera**.
5. Toggle the switch next to the development environment (e.g., VSCode) to grant camera access.

## Raspberry Pi 側の設定

### USBカメラの設定

### mjpg-streamer のインストール

```
sudo apt install git cmake libjpeg9-dev
git clone https://github.com/jacksonliam/mjpg-streamer.git
cd mjpg-streamer/mjpg-streamer-experimental
make
sudo make install
```