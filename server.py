from flask import Flask, render_template, redirect, request, session 
import random 
app = Flask(__name__)
app.secret_key = "hushush"

@app.route('/')
def index():
    if 'totalGold' not in session:
        session['totalGold'] = 0
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    place = request.form['building'] 
    if place == 'farm': 
        session['totalGold'] += random.randint(10,20)

    elif place == 'cave':
        session['totalGold'] += random.randint(5,10) 

    elif place == 'house':
        session['totalGold'] += random.randint(2,5)

    else: 
        session['totalGold'] += random.randint(-50,50)
    return redirect('/')

    # if gold >= 0:
    #     newAlert = f"<p>Congrats! You just earned {gold} from {place}!"
    #     session['activities'] += newAlert 
    # elif gold <= 0: 
    #     newAlert = f"<p>Damn..that's what happens when you go to the casino. You just lost {gold} gold.</p>"
    #     session['activities'] += newAlert
    # return redirect('/')


@app.route('/reset')
def reset():
    session.clear() 
    return redirect ('/')


if __name__ == "__main__":
    app.run(debug=True)