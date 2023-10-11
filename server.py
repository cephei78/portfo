import csv

from flask import Flask, render_template, request, redirect

app = Flask(__name__)

def write_to_database(data:dict):
    fieldnames = ['email', 'subject', 'message']

    try:
        with open('database.csv', mode='a', newline='') as database:
            writer = csv.DictWriter(database, fieldnames)
            print (f'debug: {database.tell()}')
            if database.tell() == 0:
                writer.writeheader()
            writer.writerow(data)
    except OSError:
        print('Error persisting data!')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<string:page_name>')
def works(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_database(data)
        return redirect('/thankyou.html')
    else:
        return 'Something went wrong. Try again!'
