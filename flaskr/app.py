from flask import Flask, render_template, request, jsonify,flash,redirect,url_for
import os,sys,requests, json
from flaskwebgui import FlaskUI

messages = [
            ]

app = Flask(__name__)
app.config.from_pyfile('config.py')
app.config['SECRET KEY'] = '2acae7b3b9b0c8bdb86669e2d05816403537301edb125a52'
ui = FlaskUI(app, width=500, height=500)


@app.route('/',methods=('GET','POST'))
def home():
  if request.method == 'POST':
        question = request.form.get('rasa')
        
        if not question:
            flash('Something is required!')
        else:
            text=str(question)
            payload = json.dumps({"sender": "Rasa","message": text})
            headers = {'Content-type': 'application/json', 'Accept':     'text/plain'}
            response = requests.request("POST",   url="http://localhost:5005/webhooks/rest/webhook", headers=headers, data=payload)
            response=response.json()
            resp=''
            for i in range(len(response)):
              try:
                resp += response[i]['text']
              except:
                continue
            messages.append({'question': question,'response': resp})
            return redirect(url_for('home'))
  return render_template('index.html', messages=messages)

if __name__ == "__main__":
  app.run(debug=True)
  # ui.run()