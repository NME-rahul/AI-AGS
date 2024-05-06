from flask import Flask, request, render_template
import threading

app = Flask(__name__)


app.config['Tempearture'] = ""
app.config['dataFile'] = ""
app.config['image'] = ""

def process_file():
    pass


@app.route('/files/')
def index():
    if 'Tempearture' in request.files:
        temperature = request.files['fileInput']
    if "dataFile" in request.files:
        dataFile = request.files['dataFile']
    return render_template('/static/files/settings.html')


@app.route('/')
def index():
    if 'fileInput' in request.files:
        image = request.files['fileInput']
        threading.Thread(target=process_file, args=(image,)).start()
        
    return render_template('index.html')

        
if __name__ == '__main__':
    app.run(port=2543, debug=True)
