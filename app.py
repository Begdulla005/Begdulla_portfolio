from flask import Flask, render_template

app = Flask(__name__)

class Portfolio:
    def __init__(self):
        self.ism = "Abibullayev Begdulla Rashidovich"
        self.unv = "Dasturiy injiniring yo'nalishi 3-kurs talabasi"
        self.guruh = "304-guruh"
        self.tel = "+998905040811"
        self.insta = "abibullayev_begdulla"
        self.tg = "abibullayev_begdulla"
        self.qiziqishlar = ["Python", "Java", "C++", "HTML/CSS", "Backend", "Fronted"]
        self.loyihalar = ["Onlayn xarid tizimi", "Shaxsiy Portfolio"]

@app.route('/')
def index():
    user = Portfolio()
    return render_template('index.html', user=user)

if __name__ == '__main__':
    app.run(debug=True)