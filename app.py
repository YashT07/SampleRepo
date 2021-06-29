import flask
import mysql.connector
from flask import render_template, request, Flask,Response,url_for
import json
from formFields import Clinic

#function by rohit to add two numbers
def addNum(num1, num2):
    summation = num1+ num2
    reutrn summation

app = Flask(__name__)
app.config["SECRET_KEY"] = 'ypt07'
names = []

@app.route('/')
def homepage():
    form = Clinic()
    return render_template('home.html', form = form)

@app.route('/about')
def aboutpage():
    form = Clinic()
    return render_template('about.html', form = form)

@app.route('/medistore')
def medistorepage():
    form = Clinic()
    return render_template('medistore.html', form = form)

@app.route('/catalog', methods=['GET', 'POST'])
def autocompletepage():
    form = Clinic(request.form)
    names = SQLConnection()
    return render_template("catalog.html", form=form, names=names)

@app.route('/returnlist', methods=['GET'])
def autocomplete():
    print(names)    
    return Response(json.dumps(names), mimetype='application/json')

@app.route('/test')
def testpage():
    form = Clinic()
    names = SQLConnection()
    return render_template('test.html', form = form, names = names)
    
@app.route('/success', methods = ['POST'])
def successpage():
    form = Clinic()
    return render_template('success.html', form = form)

def SQLConnection():
    # names = []

    try:
        con = mysql.connector.connect(
            user ='root',
            password = 'vu123',
            host = 'localhost',
            database = 'clinic'
        )
        
        if con.is_connected():
            print('Python is connected to the MySQL')

            my_cursor = con.cursor()


            my_cursor.execute('Select Patient_Name from patients_catalog')
            
            # Generation of resulset
            for record in my_cursor:
                # print(record)

                # To convert tuple to string
                record = ''.join(record)
                names.append(record)

            print(names)

    except mysql.connector.Error as err:
        print("Error Occurred::",err)

    finally:
        if con.is_connected():
            con.close()
            print("Connection is closed")

        return names

if __name__ == '__main__':
    print(flask.__version__)
    app.run()