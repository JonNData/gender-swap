from flask import render_template, make_response, request, current_app as app
from flask import url_for, flash, redirect
from werkzeug.utils import secure_filename
import os

@app.route('/', methods=['GET', 'POST'])
def home():
    print('Visited Home page')
    return render_template('home.html', title='Home')


@app.route('/about', methods=['GET', 'POST'])
def about():
    print('Visited about page')
    return render_template('about.html', title='About')

@app.route('/explanation', methods=['GET'])
def explanation():
    print('Visited Explanation page')
    return render_template('explanation.html', title='Explanation')

# Input file

def allowed_image(filename):

    if not "." in filename:
        return False

    ext = filename.rsplit(".", 1)[1]

    if ext.upper() in app.config["ALLOWED_EXTENSIONS"]:
        return True
    else:
        return False

@app.route("/imageupload", methods=["GET", "POST"])
def imageupload():

    if request.method == "POST":

        if request.files:

            image = request.files["image"]

            if image.filename == "":
                print("No filename")
                return redirect(request.url)

            if allowed_image(image.filename):
                filename = secure_filename(image.filename)

                image.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

                print("Image saved")

                return redirect(request.url)

            else:
                print("That file extension is not allowed")
                return redirect(request.url)

    return render_template('imageupload.html')