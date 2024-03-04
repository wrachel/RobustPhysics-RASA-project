# RobustPhysics RASA project

## Necessary packages needed:
Please make sure python verison 3.8, 3.9, or 3.10 as RASA is only compatible with these python versions. You can download python here: [https://www.python.org/downloads/release/python-31013/](https://www.python.org/downloads/release/python-31013/).

Once python is installed, please clone this github repo, or ensure the code for this github repo is installed. To do so, you can use the command `git clone 
 
## Instructions to run RASA project:

To interact with the rasa model, we need to start the rasa server. To start the server, utilize the following command on the command line: 

`rasa run -m models --enable-api`

## Instructions to run FLASK webapp containing RASA

Once the rasa server is running, we need to start the flask server by running `app.py`. To do this, navigate to the flaskr folder and run the server by entering the following commands:

`cd flaskr`

`py app.py`

Then navigate to the port where `app.py` is running in your browser. The default is `http://127.0.0.1:5000`. You are good to go!
