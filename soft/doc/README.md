## Setting Up the Development Environment

### 1. Create and Activate a Virtual Environment


```bash
git clone git@github.com:liszt01/BDM.git
cd BDM/soft
# Create a virtual environment
# Python 3.10 is recommended due to [pytorch support](https://stackoverflow.com/questions/75417119/how-to-find-what-is-the-latest-version-of-python-that-pytorch)
# To install python3.10.13 in Ubuntu, run following command:
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
cd web
flask run -h 0.0.0.0 -p 8000
```

To access the laptop camera using OpenCV, ensure that the camera access is granted to the development environment, such as VSCode, through the system settings' privacy & security.

#### Granting Camera Access on macOS

1. Open **System Settings**.
2. Navigate to **Privacy & Security**.
4. Choose **Camera**.
5. Toggle the switch next to the development environment (e.g., VSCode) to grant camera access.

## Raspberry Pi 側の設定

### mjpg-streamer のインストール & 実行

```
cd ~
sudo apt install git cmake libjpeg9-dev
git clone https://github.com/jacksonliam/mjpg-streamer.git
cd mjpg-streamer/mjpg-streamer-experimental
make
sudo make install
```

```
cd ~/BDM/soft/raspi
./start_stream.sh
```

参考

- [mjpeg-streamerのインストール&設定](https://raspi-katsuyou.com/index.php/2020/06/30/11/10/44/644/)

### root に pyenv をインストール

```
sudo su
curl https://pyenv.run | bash
echo '
export PYENV_ROOT="$HOME/.pyenv"
[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
' >> ~/.bashrc
```