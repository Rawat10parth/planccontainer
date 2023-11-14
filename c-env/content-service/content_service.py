from flask import Flask, send_from_directory
import os

app = Flask(__name__)

video_directory = 'videos'

if not os.path.exists(video_directory):
    os.makedirs(video_directory)

@app.route('/video/<filename>')
def stream_video(filename):
    video_path = os.path.join(video_directory, filename)
    return send_from_directory(video_directory, filename)

if __name__ == '__main__':
    app.run(debug=True, port=5000)