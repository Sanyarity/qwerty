from flask import Flask
import random
app = Flask(__name__)

pictures = ["img src = images/img0,"
            "img src = images/img1,"
            "img src = images/img2,"]   


@app.route("/")
def index():
  return '<h1>Здесь вы можете узнать о картинках</h1> <a href=/pictures">Посмотреть случайные картинки!</a>'

@app.route("/pictures")
def random_fact():
 return f'<p>{random.choice(pictures)}</p>'


app.run(debug = True)