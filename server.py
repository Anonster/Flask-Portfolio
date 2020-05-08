from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)


def write_to_file(data):
    with open('database.csv', newline='', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        writer = csv.writer(database, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([email, subject, message])


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_name(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_file(data)
        return redirect('/thankyou.html')
    else:
        return "Something Went Wronge"
