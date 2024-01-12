import cv2
from ultralytics import YOLO
import torch
import requests
from config import PI_IP, INCAM

stream_url = f'http://{PI_IP}:8080/?action=stream'
model = YOLO('../model/yolov8n.pt')
ID = 1
web_server_url = 'http://localhost:5000/api/joystick'

def send_tracking_data(x, y):
    value = {'x': x, 'y': y}

    try:
        response = requests.post(web_server_url, json=value, headers={'Content-Type': 'application/json'})
        response.raise_for_status()  # エラーチェック
        data = response.json()
        print('Response from server:', data)
    except requests.exceptions.RequestException as e:
        print('Error:', e)

class VideoCamera(object):
    def __init__(self):
        if INCAM: self.video = cv2.VideoCapture(0)
        else: self.video = cv2.VideoCapture(stream_url)

        # Opencvのカメラをセットします。(0)はノートパソコンならば組み込まれているカメラ

    def __del__(self):
        self.video.release()

    def get_frame(self):
        global ADVANCED
        success, image = self.video.read()

        if ADVANCED:
            # # 物体検知
            # # results = model(image, conf=0.6, verbose=False)
            # # 物体認知
            results = model.track(image, conf=0.6, verbose=False, persist=True)
            # print(results[0].boxes)
            id_list = results[0].boxes.id
            if id_list is not None and ID in id_list:
                id_index = int(torch.where(id_list == ID)[0])
                send_tracking_data(float(results[0].boxes.xywhn[id_index][0]), float(results[0].boxes.xywhn[id_index][1]))

            ret, jpeg = cv2.imencode('.jpg', results[0].plot())
            return jpeg.tobytes()
        else:
            ret, jpeg = cv2.imencode('.jpg', image)
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