#!/usr/bin/env python
import string
import random
import re
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/generate', methods=['GET', 'POST'])
def password_generate():
    if request.method == 'GET':
        return render_template('generate.html') 
    elif request.method == 'POST':
        num = request.form['length']
        if num == '':
            error = '1以上の数値を入力してください'
            return render_template('generate.html', error=error) 
        elif num == '0':
            error = '1以上の数値を入力してください'
            return render_template('generate.html', error=error) 
        elif re.match('[a-zA-Z]', num):
            error = '1以上の数値を入力してください'
            return render_template('generate.html', error=error) 

        source = string.digits
        source += string.ascii_letters
        password = ''.join([random.choice(source) for i in range(int(num))])
        return render_template('generate.html', password=password) 
