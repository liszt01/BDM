## あそびかた

目次

- [0. 環境構築](#0-環境構築)
    - [パソコン側の設定](#パソコン側の設定)
    - [ラズパイ側の設定](#ラズパイ側の設定)
- [1. 実行](#1-実行)

### 0. 環境構築

#### パソコン側の設定

リポジトリをクローンする。

```bash
git clone git@github.com:liszt01/BDM.git
```

Python3.10 の仮想環境をつくる。

> 3.10 が必要な理由
> [pytorch support](https://stackoverflow.com/questions/75417119/how-to-find-what-is-the-latest-version-of-python-that-pytorch)


```bash
# apt で Python3.10 をインストールする場合
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.10
sudo apt install python3.10-venv
```

```bash
cd BDM/soft
python3.10 -m venv .bdm-env
source .bdm-env/bin/activate
python3 -m pip install -r requirements.txt
```

YOLO のモデルをダウンロードする。

```bash
cd model
wget https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8n.pt
```

#### ラズパイ側の設定

リポジトリをクローンする。

```bash
sudo apt update
sudo apt install git
git clone git@github.com:liszt01/BDM.git
```

mjpg-streamer をビルドする。

```bash
sudo apt update
sudo apt install cmake libjpeg9-dev
git clone https://github.com/jacksonliam/mjpg-streamer.git
cd mjpg-streamer/mjpg-streamer-experimental
make
sudo make install
```

pigpio をインストールする。

```bash
sudo apt update
sudo apt install pigpio
```

参考

- [mjpeg-streamerのインストール&設定](https://raspi-katsuyou.com/index.php/2020/06/30/11/10/44/644/)

### 1. 実行

ラズベリーパイのIPアドレスを取得する。

```bash
ssh {user}@raspberrypi.local
ifconfig
```

パソコン上で `BDM/soft/web/config.py` の `PI_IP` と、ラズパイ上で `BDM/soft/raspi/main.py` の `PI_IP` を先程取得したラズパイのIPに変更する。

パソコン上で Web サーバーを立ち上げる。

```bash
cd BDM/soft/web
flask run -h 0.0.0.0
```

ラズパイ上で `main.py` を実行する。

```bash
cd BDM/soft/raspi
python3 main.py
```

最後にブラウザで `http://{パソコンのIPアドレス}:5000` にアクセスすると、遊べます。

### おまけ: root に pyenv をインストール

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