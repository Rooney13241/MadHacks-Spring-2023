from flask import Flask, render_template, url_for, send_file, request
import os
import script

app = Flask(__name__)
html_dir = './htmlfiles/'


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get the user input from the request
        user_input = request.form['user_input']
        # Run the user input on the command line
        
        script.scan(user_input)
    html_files = [f for f in os.listdir(html_dir) if f.endswith('.html')]
    # Save the output to a file
    # Return the output file to the user
    return render_template('index.html', html_files=html_files)


@app.route('/view/<filename>')
def view(filename):
    filepath = os.path.join(html_dir, filename)

    return send_file(filepath)



