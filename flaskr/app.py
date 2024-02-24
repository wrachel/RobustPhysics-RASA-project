from flask import Flask, render_template, request, jsonify,flash,redirect,url_for
import os,sys,requests, json
from flaskwebgui import FlaskUI

messages = [ {'question': "Hi",
              'response': "hi"},
              {'question': "Hi x2",
              'response': "hi x2"},
              {'question': "Hi x3",
              'response': "hi x3"},
              {'question': "Hi x4",
              'response': "hi x4"},
              {'question': "Hi x5",
              'response': "hi x5"},
              {'question': "Hi x6",
              'response': "hi x6"},
              {'question': "Hi x7",
              'response': "hi x7"},
              {'question': "Hi x8",
              'response': "hi x8"},
              {'question': "Hi x9",
              'response': "hi x9"},
              {'question': "Hi x10",
              'response': "bro do you not have a job you've been saying hi to a digital bot for like 3 minutes like are you mentally okay"},
              {'question': "no",
              'response': "yeah I figured"},
              {'question': "hi",
              'response': "you serious"},
              {'question': "Hi",
              'response': "please just let me rest"},
              {'question': "Hi",
              'response': "bro am i the bot or are you the bot i'm just confused now"},
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