from flask import Flask, render_template

app = Flask(__name__)

class Portfolio:
    def __init__(self):
        user = {
    "ism": "Begdulla",
    "unv": "Dasturiy injiniring yo'nalishi talabasi",
    "guruh": "3-kurs",
    "bio": "Men Qoraqalpog'iston Respublikasi Beruniy tumanida tug'ulganman. Yoshligimdan sun'iy intellekt, informatika va dasturlashga qiziqaman. Hozirda Samarqand Davlat Universiteti Sun'iy intellekt va raqamli texnologiyalar fakultetida o'qiyman. Mening maqsadim - sun'iy intellekt, o'z bilimim va tajribamga tayangan holda mobil ilovalar, qiziqarli o'yinlar yaratish.",
    "maqsadlar": [
        "Dasturchi bo'lish va zamonaviy texnologiyalar yaratish",
        "Har xil qiziqarli loyihalarda faol ishtirok etish",
        "Sun'iy intellekt va dasturlashni chuqur o'rganish",
        "Katta IT kompaniyalarida yo'nalishim bo'yicha ish yuritish"
    ],
    "tel": "+998 90 504 08 11"
    "insta": "abibullayev_begdulla"
    "tg": "abibullayev_begdulla"
    "qiziqishlar": ["Python", "Java". "C++", "va boshqa dasturlash tilllari"]
    "loyihalar": ["Portfolio", "Do'kon.uz"]
}

@app.route('/')
def index():
    user = Portfolio()
    return render_template('index.html', user=user)

if __name__ == '__main__':
    import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)