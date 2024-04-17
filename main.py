import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from config import UPLOAD_FOLDER, ALLOWED_EXTENSIONS



app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def main():
    return render_template("bim_index.html")


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/bim", methods=["GET", "POST"])
def bim():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'image_file' not in request.files:
            flash('No file part')
            return "Error image not found"
        file = request.files['image_file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return "Error, image sent empty?"
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            upload_folder = app.config["UPLOAD_FOLDER"]
            print(upload_folder)
            file.save(os.path.join(upload_folder, filename))
            return "you file is available <a href='static/{filename}'> here </a>"
app.run(port=5001)