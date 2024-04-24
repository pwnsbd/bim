from flask import render_template, request, flash, Blueprint
from instance.config import ALLOWED_EXTENSIONS
from PIL import Image
import base64
import io

uploads_bp = Blueprint("uploads", __name__, url_prefix="/uploads")


@uploads_bp.route("/", methods=["GET", "POST"])
def uploads():
    if request.method == "POST":
        # check if the post request has the file part
        if "image_file" not in request.files:
            flash("No file part")
            return "Error image not found"
        file = request.files["image_file"]
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == "":
            flash("No selected file")
            return "Error, image sent empty?"
        if file and allowed_file(file.filename):
            im = Image.open(file)
            data = io.BytesIO()
            ext = file.filename.rsplit(".", 1)[1].lower()
            if ext == "jpg":
                ext = "JPEG"
            im.save(data, f"{ext}".upper())
            encoded_img_data = base64.b64encode(data.getvalue())
            return render_template(
                "bim.html", img_data=encoded_img_data.decode("utf-8"), img_type=ext
            )
        else:
            return "Error: Invalid file type"

    return "This route only supports POST requests."


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
