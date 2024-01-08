### TODO

- threading.Lock()のテスト

- (UIを凝る)

  ストリームのオンオフ機能
  操作部分の位置など
  ボタンが押せない間のアニメーション

- (物体追跡の機能を追加)

### ラズパイからパソコンに映像を送る

- ラズパイ

`mjpg-streamer`でストリーム配信する。
ブラウザで http://[ラズパイのIP]:8080/?action=stream を開くと見れる。

- パソコン

OpenCVでストリーム配信をキャプチャする。
`cv2.VideoCapture([ストリームURL])`

参考サイト

- [Raspberry Pi 3 の標準カメラで撮影した動画をブラウザに配信する方法まとめ](https://qiita.com/okaxaki/items/72226a0b0f5fab0ec9e9)
- [ラズパイカメラの映像をMacからチェックする](https://plant-raspberrypi3.hatenablog.com/entry/2017/10/22/123404)
- [「ラズパイ」動画配信を試してみた](https://note.com/030616/n/nc090bd88cb0a)
- [ラズパイカメラから NDI 送信してみた。](https://qiita.com/kitazaki/items/eeb710a78c657024f844)
- [RaspberryPi と ffmpeg で映像＋音声ストリーミング](https://heavymoon.org/2021/10/12/raspberrypi-ffmpeg-streaming/)
- [Raspberry Pi 4でffmpegを使ってUDPでのストリーミング](https://tomosoft.jp/design/?p=46398)
- [Pi3（Pi4）の h264_omx でts動画をmp4にハードウェアエンコード爆速（HandBrakeCLIより速い）](https://min117.hatenablog.com/entry/2022/09/18/074547)
- [Raspberry Pi 4で64ビットハードウェアエンコードを試してみましたが](https://denor.jp/raspberry-pi-4%E3%81%A764%E3%83%93%E3%83%83%E3%83%88%E3%83%8F%E3%83%BC%E3%83%89%E3%82%A6%E3%82%A7%E3%82%A2%E3%82%A8%E3%83%B3%E3%82%B3%E3%83%BC%E3%83%89%E3%82%92%E8%A9%A6%E3%81%97%E3%81%A6%E3%81%BF)
- [ラズパイ ＋ ffmpeg で Web カメラ映像をH.264コーデックで保存する方法](https://qiita.com/y-okamon/items/c468ef1b0172f3c0a76f)
- [Raspberry Pi: 動画の撮影](https://hazm.at/mox/gadget/raspberrypi/camera/movie/index.html)
- [ラズパイに繋いだWEBカメラの映像を HLS 形式で配信してブラウザで再生する](https://qiita.com/y-okamon/items/bc5cdf87d68e4ec3dcc0)
- [HTTPによるビデオ・ストリーミング配信](https://interface.cqpub.co.jp/wp-content/uploads/if2101_101.pdf)

- [FlaskとOpenCVでカメラ画像をストリーミングして複数ブラウザでアクセスする](https://qiita.com/RIckyBan/items/a7dea207d266ef835c48)
- [【Raspberry Pi】ストリーミング配信した映像をOpenCVで受け取る](https://nn-hokuson.hatenablog.com/entry/2020/11/16/162539)
- [ラズパイ4BとUSBカメラで、Python Bottle、OpenCVを使ったブラウザ上のMJPGストリーミング実験（備忘録）](https://www.mgo-tec.com/blog-entry-raspi4-opencv-cam01.html)
- [Raspberry Piへのコンピュータビジョンの実装](https://www.koi.mashykom.com/Raspi_opencv.html)
- [FlaskとOpenCVを使ってWEBカメラで撮影した画像をストリーミングする](https://qiita.com/sti320a/items/3cdafb737d2c16fbaa51)

### YOLOv8 物体検出

参考文献
- [WebカメラでYOLOv8を動かす](https://zenn.dev/straydog/articles/4965a62e6fbb97)
- [YOLOv8をpython openCVでちゃちゃっと物体検出してみる](https://qiita.com/napspans/items/9ddc80e4625314c5607d)
- [カメラに映った画像をリアルタイムに物体検知する](https://www.tetsumag.com/2023/03/11/317/)


### raspberry pi に Python3.10.13 インストール

ビルド失敗してた

```
$ pyenv install 3.10.13

Downloading Python-3.10.13.tar.xz...
-> https://www.python.org/ftp/python/3.10.13/Python-3.10.13.tar.xz
Installing Python-3.10.13...
Traceback (most recent call last):
  File "<string>", line 1, in <module>
  File "/home/fuma/.pyenv/versions/3.10.13/lib/python3.10/bz2.py", line 17, in <module>
    from _bz2 import BZ2Compressor, BZ2Decompressor
ModuleNotFoundError: No module named '_bz2'
WARNING: The Python bz2 extension was not compiled. Missing the bzip2 lib?
Traceback (most recent call last):
  File "<string>", line 1, in <module>
  File "/home/fuma/.pyenv/versions/3.10.13/lib/python3.10/curses/__init__.py", line 13, in <module>
    from _curses import *
ModuleNotFoundError: No module named '_curses'
WARNING: The Python curses extension was not compiled. Missing the ncurses lib?
Traceback (most recent call last):
  File "<string>", line 1, in <module>
  File "/home/fuma/.pyenv/versions/3.10.13/lib/python3.10/ctypes/__init__.py", line 8, in <module>
    from _ctypes import Union, Structure, Array
ModuleNotFoundError: No module named '_ctypes'
WARNING: The Python ctypes extension was not compiled. Missing the libffi lib?
Traceback (most recent call last):
  File "<string>", line 1, in <module>
ModuleNotFoundError: No module named 'readline'
WARNING: The Python readline extension was not compiled. Missing the GNU readline lib?
Traceback (most recent call last):
  File "<string>", line 1, in <module>
  File "/home/fuma/.pyenv/versions/3.10.13/lib/python3.10/ssl.py", line 99, in <module>
    import _ssl             # if we can't import it, let the error propagate
ModuleNotFoundError: No module named '_ssl'
ERROR: The Python ssl extension was not compiled. Missing the OpenSSL lib?

Please consult to the Wiki page to fix the problem.
https://github.com/pyenv/pyenv/wiki/Common-build-problems


BUILD FAILED (Raspbian 11 using python-build 20180424)

Inspect or clean up the working tree at /tmp/python-build.20240102164754.3995
Results logged to /tmp/python-build.20240102164754.3995.log

Last 10 log lines:
        LD_LIBRARY_PATH=/tmp/python-build.20240102164754.3995/Python-3.10.13 ./python -E -m ensurepip \
                $ensurepip --root=/ ; \
fi
Looking in links: /tmp/tmpqk0nlfnv
Processing /tmp/tmpqk0nlfnv/setuptools-65.5.0-py3-none-any.whl
Processing /tmp/tmpqk0nlfnv/pip-23.0.1-py3-none-any.whl
Installing collected packages: setuptools, pip
  WARNING: The scripts pip3 and pip3.10 are installed in '/home/fuma/.pyenv/versions/3.10.13/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed pip-23.0.1 setuptools-65.5.0
```

### ChatGPT に一応聞いてみた
 
ラズベリーパイで撮影した映像をパソコンに送信し、OpenCVの処理を施したり、ウェブアプリに表示させるためには、いくつかのステップがあります。以下に、一般的な手順を示します。

1. **ラズベリーパイ側の設定:**
   - カメラを有効にする: `raspi-config` を使用して、ラズベリーパイのカメラモジュールを有効にします。

   - ストリーミングサーバのインストール: ラズベリーパイ上でストリーミングサーバをセットアップします。たとえば、`motion` や `mjpg-streamer` などが利用できます。

     例えば `mjpg-streamer` を使用する場合:

     ```bash
     sudo apt-get update
     sudo apt-get install -y libjpeg8-dev imagemagick libv4l-dev
     git clone https://github.com/jacksonliam/mjpg-streamer.git
     cd mjpg-streamer/mjpg-streamer-experimental
     make
     ```

     ストリーミングを開始:

     ```bash
     ./mjpg_streamer -i "./input_uvc.so" -o "./output_http.so -w ./www"
     ```

     これにより、`http://<your_pi_ip>:8080` でラズベリーパイのストリーミングが見れるようになります。

2. **パソコン側の設定:**
   - OpenCVのインストール: パソコンにOpenCVをインストールします。

     ```bash
     pip install opencv-python
     ```

   - ストリーミングの受信: OpenCVを使用して、ラズベリーパイからのストリーミングを受信します。

     ```python
     import cv2
     import urllib.request
     import numpy as np

     stream_url = 'http://<your_pi_ip>:8080/stream/video.mjpeg'
     stream = urllib.request.urlopen(stream_url)

     while True:
         bytes = bytes()
         for i in range(30):
             bytes += stream.read(1024)
             a = bytes.find(b'\xff\xd8')
             b = bytes.find(b'\xff\xd9')
             if a != -1 and b != -1:
                 jpg = bytes[a:b+2]
                 bytes = bytes[b+2:]
                 img = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
                 cv2.imshow('Video', img)
                 if cv2.waitKey(1) & 0xFF == ord('q'):
                     break
     ```

3. **ウェブアプリの作成:**
   - FlaskなどのWebフレームワークを使用して、ウェブアプリを作成します。

     ```python
     from flask import Flask, render_template, Response

     app = Flask(__name__)

     @app.route('/')
     def index():
         return render_template('index.html')

     def gen():
         stream_url = 'http://<your_pi_ip>:8080/stream/video.mjpeg'
         stream = urllib.request.urlopen(stream_url)
         while True:
             bytes = stream.read(1024)
             yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + bytes + b'\r\n\r\n')

     @app.route('/video_feed')
     def video_feed():
         return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')

     if __name__ == '__main__':
         app.run(debug=True)
     ```

4. **HTMLテンプレートの作成:**
   - ウェブアプリ用のHTMLファイルを作成し、映像を表示するためのタグを追加します。

     ```html
     <!DOCTYPE html>
     <html>
     <head>
         <title>Video Streaming</title>
     </head>
     <body>
         <h1>Video Streaming</h1>
         <img src="{{ url_for('video_feed') }}">
     </body>
     </html>
     ```

これにより、ラズベリーパイで撮影した映像がストリーミングされ、パソコン上でOpenCVの処理を施し、ウェブアプリで表示されるはずです。各ステップで発生する問題に対処するには、デバッグやログ出力を活用してください。

映像をラズベリーパイからパソコンに送り、OpenCVを使用して画像処理を行うには、いくつかのステップが必要です。以下に基本的な手順を示します。

1. **ラズベリーパイの設定:**
   - カメラを有効にします。`raspi-config` を使用してカメラを有効にし、ラズベリーパイを再起動します。

2. **ストリーミングサーバのセットアップ:**
   - ラズベリーパイで動作するストリーミングサーバをセットアップします。例えば、MJPG-Streamerを使用することができます。GitHubリポジトリからソースコードをクローンしてビルドします。

     ```bash
     sudo apt-get update
     sudo apt-get install -y libjpeg8-dev imagemagick libv4l-dev
     git clone https://github.com/jacksonliam/mjpg-streamer.git
     cd mjpg-streamer/mjpg-streamer-experimental
     make
     ```

     ストリーミングを開始:

     ```bash
     ./mjpg_streamer -i "./input_uvc.so" -o "./output_http.so -w ./www"
     ```

     これにより、`http://<your_pi_ip>:8080` でラズベリーパイのストリーミングが見れるようになります。

3. **パソコン側の設定:**
   - OpenCVをインストールします。

     ```bash
     pip install opencv-python
     ```

   - OpenCVを使用して、ストリーミングからフレームを取得し、画像処理を行います。

     ```python
     import cv2
     import urllib.request
     import numpy as np

     stream_url = 'http://<your_pi_ip>:8080/stream/video.mjpeg'
     stream = urllib.request.urlopen(stream_url)

     while True:
         bytes = bytes()
         for i in range(30):
             bytes += stream.read(1024)
             a = bytes.find(b'\xff\xd8')
             b = bytes.find(b'\xff\xd9')
             if a != -1 and b != -1:
                 jpg = bytes[a:b+2]
                 bytes = bytes[b+2:]
                 img = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)

                 # ここに画像処理のコードを追加

                 cv2.imshow('Frame', img)
                 if cv2.waitKey(1) & 0xFF == ord('q'):
                     break
     ```

4. **画像処理の追加:**
   - OpenCVを使用して物体検知やラベリングを行います。物体検知には、例えばHaar cascadesやDNN (Deep Neural Networks) を使用することができます。以下は簡単な例です。

     ```python
     # 例: Haar cascadesを使用して顔検知
     face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
     faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

     for (x, y, w, h) in faces:
         cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

     # ここに他の処理を追加

     cv2.imshow('Frame', img)
     ```

これで、ラズベリーパイで撮影した映像がストリーミングされ、パソコン上でOpenCVを使用して画像処理が行われます。処理結果は`img`にありますので、これを用いてさまざまな処理を追加できます。
