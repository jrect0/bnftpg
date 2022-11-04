
from flask import Flask, render_template, url_for, redirect

app = Flask(__name__, template_folder="templates")

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/page2")
def page2():
    return render_template('page2.html')

@app.route("/page3")
def page3():
    return render_template('page3.html')

@app.route("/rarenfts")
def burgerhouse():
    return render_template('rarenfts.html')

@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/babyburgbuy")
def babyburgbuy():
    return render_template('babyburgbuy.html')

@app.route("/burgercutbuy")
def burgercutbuy():
    return render_template('burgercutbuy.html')

@app.route("/burgercutebuy")
def burgercutebuy():
    return render_template('burgercutebuy.html')

@app.route("/burgereatbuy")
def burgereatbuy():
    return render_template('burgereatbuy.html')

@app.route("/burgerfadedbuy")
def burgerfadedbuy():
    return render_template('burgerfadedbuy.html')

@app.route("/burgergolfbuy")
def iburgergolfbuyndex():
    return render_template('burgergolfbuy.html')

@app.route("/burgerkidbuy")
def burgerkidbuy():
    return render_template('burgerkidbuy.html')

@app.route("/burgerlaybuy")
def burgerlaybuy():
    return render_template('burgerlaybuy.html')

@app.route("/burgerliftbuy")
def burgerliftbuy():
    return render_template('burgerliftbuy.html')

@app.route("/burgerrollsbuy")
def burgerrollsbuy():
    return render_template('burgerrollsbuy.html')

@app.route("/burgertumblebuy")
def burgertumblebuy():
    return render_template('burgertumblebuy.html')

@app.route("/smallspillbuy")
def smallspillbuy():
    return render_template('smallspillbuy.html')

@app.route("/checkout")
def checkout():
    return render_template('checkout.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run()