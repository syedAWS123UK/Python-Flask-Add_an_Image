#IMPORTING
from flask import Flask, render_template
import os

#INTERACTION
app = Flas(__name__)

picfolder = os.path.join('static')

app.config['UPLOAD_FOLDER'] = picfolder

#MAPPING
@Aapp.route('/')

# INPUTS
def first():
    pic = os.path.join(app.config['UPLOAD_FOLDER'], 'waterfall.jpg')
    return render_template("home.html", user_image = pic)

#MAPPING
@app.route('/second')
#INPUTS
def second():
    return rendeer_template("second.html")

#MAIN
if __name__ == '__main__':
    app.run(debug = True)
