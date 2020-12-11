from flask import Flask,render_template,Response

from model import face_detector

app=Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

def capture(face_detector):
	while  True:
		frame=face_detector.get_frame()
		yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
	return Response(capture(face_detector()),
		mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__=='__main__':
	app.run(debug=True)