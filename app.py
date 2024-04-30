from flask import Flask, render_template, request
import re

app = Flask(__name__)

def is_scientific_number(input_str):
    # Regular expression pattern for scientific notation
    pattern = r'^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?$'
    
    # Check if input matches the pattern
    if re.match(pattern, input_str):
        return "Yes, it is a scientific number."
    else:
        return "No, it is not a scientific number."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check():
    input_number = request.form['number']
    result = is_scientific_number(input_number)
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
