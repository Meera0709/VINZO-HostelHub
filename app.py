from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import pandas as pd

m=0
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('login.html')

@app.route('/create_new_user', methods=['POST'])
def create_new_user():
    registration_number = request.form['registration_number']
    name = request.form['name']
    block = request.form['block']
    room_number = request.form['room_number']
    phone_number = request.form['phone_number']
    password = request.form['password']
    user_data = pd.read_csv('C:\\Users\\meera\\Documents\\BTech CSE spl. AIML\\VS code\\Solvathon\\user_data.csv')
    new_user = pd.DataFrame({'Registration Number': [registration_number],'Name': [name], 'Block': [block], 'Room Number': [room_number], 'Phone Number': [phone_number], 'Password': [password]})
    
    new_user.to_csv('C:\\Users\\meera\\Documents\\BTech CSE spl. AIML\\VS code\\Solvathon\\user_data.csv', index=False, mode='a',header=False)

    return redirect('/login')

@app.route('/login')
def login(): 
       return render_template('login.html', message='Please log in')
def login(m): 
       return render_template('login.html', message=m)

@app.route('/auth', methods=['POST']) 
def auth():
    registration_number = request.form['registration_number']
    password = request.form['password']
    df= pd.read_csv('C:\\Users\\meera\\Documents\\BTech CSE spl. AIML\\VS code\\Solvathon\\user_data.csv')
    dict_records = df.to_dict(orient='records')
    for i in dict_records:
      if (registration_number== i['Registration Number']) & (i['Password']== password): 
        return redirect(url_for('choice'))
    
    else:
        return login("Incorrect registration number or password")
    
@app.route('/home')
def home():
       return render_template(
       'home.html',
       title='Home Page',
       year=datetime.now().year,
       )

@app.route('/choice')
def choice():
       return render_template(
       'choice.html',
       title='Choice Page',
       year=datetime.now().year,
       )

@app.route('/profile')
def profile():
    return render_template('profile.html',message=m)

@app.route('/buy')
def buy():
    return render_template('buy.html')

@app.route('/intra')
def intra():
    return render_template('home.html')

@app.route('/inter')
def inter():
    return render_template('home.html')

@app.route('/borrow')
def borrow():
    return render_template('borrow.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/lostandfound')
def lostandfound():
    return render_template('lostandfound.html')

@app.route('/submit_borrow', methods=['POST'])
def submit_borrow():
    product_name = request.form['product_name']
    urgency = request.form['urgency']
    within = request.form['within']
    
    read_borrow = pd.read_csv('borrow1.csv')
    new_borrow = pd.DataFrame({'Product Name':[product_name],'Urgency':[urgency], 'Within':[within]})
    new_borrow.to_csv('borrow1.csv', index=False, mode='a',header=False)
    return render_template('borrow.html')

@app.route('/submit_buy', methods=['POST'])
def submit_buy():
    product_name = request.form['product-name']
    product_description = request.form['product-description']
    cost = request.form['cost']
    urgency = request.form['urgency']
    read_buy = pd.read_csv('buy.csv')
    new_buy = pd.DataFrame({'Product Name':[product_name],'Cost':[cost], 'urgency':[urgency]})
    new_buy.to_csv('borrow.csv', index=False, mode='a',header=False)
    return render_template('buy.html')
    
@app.route('/signup')
def signup():
    return render_template('create_user.html')

@app.route('/login1')
def login1():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)