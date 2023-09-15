from flask import *
import violenceDetector
import time

app = Flask(__name__)

@app.route("/")
def upload():
    return render_template("file_upload.html")


@app.route("/success",methods=["POST"])
def success():
    global fr
    global file
    global ty
    fr=int(request.form['frame'])
    ty = (request.form['type'])

    print(ty)

    f = request.files['file']
    file = f.filename
    f.save(file)
    return render_template("success.html", frames=fr, name=file, modelType=ty)

@app.route("/convert")
def cropper():
    violenceDetector.detector(fr, file, ty)
    
    #time.sleep(5)

    return render_template("download.html")


if __name__== "__main__":
    app.run(debug=True)
