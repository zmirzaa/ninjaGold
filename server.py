from pyexpat.errors import messages
from flask import Flask, render_template, redirect, request, session 
import random 
app = Flask(__name__)
app.secret_key = "hushush"

@app.route('/')
def index():
    if 'totalGold' not in session:
        session['totalGold'] = 0 
        session['activity'] = ""
    return render_template('index.html', messages=session['activity'])

@app.route('/process', methods=['POST'])
def process():
    place = request.form['building'] 
    
    if place == 'farm': 
        gold = random.randint(10,20)

    elif place == 'cave':
        gold = random.randint(5,10) 

    elif place == 'house':
        gold = random.randint(2,5)

    else: 
        gold = random.randint(-50,50)
    session['totalGold'] += gold 

    if gold > 0: 
        newAlert = f"<p class=text-success style='font-family: Fredoka;'>Congrats! You just won {gold} pounds of gold from {place}!</p>"
        session['activity'] += newAlert
    elif gold < 0: 
        newAlert = f"<p class=text-danger style='font-family: Fredoka;'>Oh no, that's what happens when you go the casino...You just lost {gold} pounds of gold.</p>"
        session['activity'] += newAlert
    return redirect('/')


@app.route('/reset')
def reset():
    session.clear() 
    return redirect ('/')


if __name__ == "__main__":
    app.run(debug=True)