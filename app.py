import os
import model
from flask import Flask, render_template, request, redirect, url_for, send_from_directory


UPLOAD_FOLDER = 'pictures'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['UPLOAD_PATH'] = 'uploads'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        for uploaded_file in request.files.getlist('file'):
            if uploaded_file.filename != '':
                uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], uploaded_file.filename))

                model.changed_pic(uploaded_file.filename)

        return redirect(url_for('index'))
    files = os.listdir(app.config['UPLOAD_PATH'])
    return render_template('index.html', files=files)


@app.route('/uploads/<filename>')
def upload(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


if __name__ == '__main__':
    app.run()
