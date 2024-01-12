from flask import Flask, render_template, Response, redirect, url_for, request, jsonify
from config import DEBUG_FLASK
import script.image_processing as imp
from script.input_handler import move_motor_relative, set_absolute_angle, launch_rocket, reload

imp.ADVANCED = False
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', debug=DEBUG_FLASK)

@app.route('/video_feed')
def video_feed():
    return Response(imp.frame_generator(imp.VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/api/joystick', methods=['POST'])
def receive_joystick():
    joystick_value = request.json    
    move_motor_relative(joystick_value['x'], joystick_value['y'])
    # 応答としてJSONデータを返す（一応）
    response_data = {'message': 'Joystick data received successfully!'}
    return jsonify(response_data)

@app.route('/api/form', methods=['POST'])
def receive_form():
    form_value = request.json    
    set_absolute_angle(form_value['x'], form_value['y'])
    
    response_data = {'message': 'Form data received successfully!'}
    return jsonify(response_data)

@app.route('/api/launch', methods=['POST'])
def receive_launch():
    response_data = launch_rocket()
    return jsonify(response_data)

@app.route('/api/reload', methods=['POST'])
def receive_reload():
    response_data = reload()
    return jsonify(response_data)

@app.route('/api/advanced', methods=['POST'])
def receive_advanced():
    imp.ADVANCED = not imp.ADVANCED
    response_data = {'message': 'Request received successfully!'}
    print('api', imp.ADVANCED)
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
