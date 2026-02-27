from flask import Flask, render_template
import os

app = Flask(__name__)

class Portfolio:
    def __init__(self):
        # 6-qator va undan keyingilar endi ichkariga surilgan (Indent qilingan)
        self.user = {
            "ism": "Abibullayev Begdulla Rashidovich",
            "unv": "Dasturiy injiniring yo'nalishi 3-kurs talabasi",
            "guruh": "304-guruh",
            "bio": "Men Qoraqalpog'iston Respublikasi Beruniy tumanida tug'ilganman. Yoshligimdan sun'iy intellekt, informatika va dasturlashga qiziqaman. Hozirda Samarqand Davlat Universiteti talabasiman.",
            "maqsadlar": [
                "Sun'iy intellekt va dasturlashni chuqur o'rganish",
                "Xalqaro katta IT kompaniyalarda ish yuritish"
            ],
            "tel": "+998905040811",
            "insta": "abibullayev_begdulla",
            "tg": "abibullayev_begdulla",
            "qiziqishlar": ["Python", "Java", "C++", "Backend", "Fronted"],
            "loyihalar": ["Onlayn xarid tizimi", "Shaxsiy Portfolio"]
        }

@app.route('/')
def index():
    portfolio = Portfolio()
    # portfolio.user orqali lug'atni HTML-ga uzatamiz
    return render_template('index.html', user=portfolio.user)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)