import cv2
from ultralytics import YOLO
from config import PI_IP, PI_PORT_STREAM, NO_PI

stream_url = f'http://{PI_IP}:{PI_PORT_STREAM}/?action=stream'
model = YOLO('../model/yolov8n.pt')

class VideoCamera(object):
    def __init__(self):
        if NO_PI: self.video = cv2.VideoCapture(0)
        else: self.video = cv2.VideoCapture(stream_url)

        # Opencvのカメラをセットします。(0)はノートパソコンならば組み込まれているカメラ

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, image = self.video.read()
        # 物体検出した結果
        results = model(image, conf=0.6, verbose=False)
        ret, jpeg = cv2.imencode('.jpg', results[0].plot())
        return jpeg.tobytes()

        # read()は、二つの値を返すので、success, imageの2つ変数で受けています。
        # OpencVはデフォルトでは raw imagesなので JPEGに変換
        # ファイルに保存する場合はimwriteを使用、メモリ上に格納したい時はimencodeを使用
        # cv2.imencode() は numpy.ndarray() を返すので .tobytes() で bytes 型に変換

def frame_generator(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')