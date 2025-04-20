from flask import Flask, request, render_template
from threading import Thread
import Queue
import log
import runner
import grading
import model
import threading
import sys

error_1 = 'Error: Provide necessary argument to run the code.\n'

app = Flask(__name__)
TASKS_QUEUE  = Queue.Queue(10)


@app.route('/', methods=['GET', 'POST'])
def index():
    x = "wd"
    if request.method == 'POST' and 'fileInput' in request.files:
        x = "Yes i'm enterd!"
        image = request.files['fileInput']
        TASKS_QUEUE.add(image)
        process_
    return render_template('index.html', enterd=x)
=======
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

def core():
    pass
        
if __name__ == '__main__':
    app.run(debug=True, port=5000)
    #Thread(target=app.run, kwargs={'debug': True, 'use_reloader': False})
    #Thread(target=core)
    if len(sys.argv) == 1:
        sys.exit(error_1)
    app.run(port=sys.argv[1], debug=sys.argv[2])
