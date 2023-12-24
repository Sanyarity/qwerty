#Импорт
from flask import Flask, render_template,request, redirect



app = Flask(__name__)

#Запуск страницы с контентом
@app.route('/')
def index():
    return render_template('index.html')


#Динамичные скиллы
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_python = request.form.get('button_discord')
    return render_template('index.html', button_python=button_python)
@app.route("/send", methods=['POST'])
def send():
    email = request.form.get("email")
    message = request.form.get("text")
    complete = "Ваше обращение отправлено, ждите ответа"
    with open("message.txt", "a", encoding="UTF=8") as f:
        f.write(f"email: {email}, сообщение: {message} \n") 
       
    return render_template('index.html', complete=complete)

if __name__ == "__main__":
    app.run(debug=True)