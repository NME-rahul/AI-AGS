from flask import Flask, request, render_template
import threading
import sys

error_1 = 'Error: Provide necessary argument to run the code.\n'

app = Flask(__name__)

'''
def process_file(image,):
    pass

@app.route('/files/')
def index():
    if 'Tempearture' in request.files:
        temperature = request.files['fileInput']
    if "dataFile" in request.files:
        dataFile = request.files['dataFile']
    return render_template('/static/files/settings.html')

'''


@app.route('/')
def index():
    if 'fileInput' in request.files:
        image = request.files['fileInput']
        threading.Thread(target=process_file, args=(image,)).start()
    return render_template('index.html')

        
if __name__ == '__main__':
    if len(sys.argv) == 1:
        sys.exit(error_1)
    app.run(port=sys.argv[1], debug=sys.argv[2])
