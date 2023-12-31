import cv2
from ultralytics import YOLO

raspberrypi_ip = '192.168.0.17'
stream_url = f'http://{raspberrypi_ip}:8080/?action=stream'
model = YOLO('../model/yolov8n.pt')

class VideoCamera(object):
    def __init__(self):
        # self.video = cv2.VideoCapture(0)
        self.video = cv2.VideoCapture(stream_url)

        # Opencvのカメラをセットします。(0)はノートパソコンならば組み込まれているカメラ

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, image = self.video.read()
        # 物体検出した結果
        results = model(image)
        ret, jpeg = cv2.imencode('.jpg', results[0].plot())
        return jpeg.tobytes()

        # read()は、二つの値を返すので、success, imageの2つ変数で受けています。
        # OpencVはデフォルトでは raw imagesなので JPEGに変換
        # ファイルに保存する場合はimwriteを使用、メモリ上に格納したい時はimencodeを使用
        # cv2.imencode() は numpy.ndarray() を返すので .tobytes() で bytes 型に変換
