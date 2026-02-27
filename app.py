from flask import Flask, render_template

app = Flask(__name__)

class Portfolio:
    def __init__(self):
    user = {
    "ism": "Abibullayev Begdulla Rashidovich",
    "unv": "Dasturiy injiniring yo'nalishi 3-kurs talabasi",
    "guruh": "304-guruh",
    "bio": "Men Samarqand shahrida tug'ilganman. Yoshligimdan texnologiya va dasturlashga qiziqaman. Hozirda Samarqand Davlat Universiteti talabasiman.",
    "maqsadlar": [
        "Full-stack developer bo'lish",
        "Sun'iy intellektni o'rganish",
        "Xalqaro IT kompaniyalarda ishlash"
    ],
    "tel": "+998 90 123 45 67",
    "insta": "begdulla005",
    "tg": "begdulla005",
    "qiziqishlar": ["Python", "Java", "C++", "Backend"],
    "loyihalar": ["Onlayn xarid tizimi", "Shaxsiy Portfolio"]
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