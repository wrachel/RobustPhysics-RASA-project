# RobustPhysics RASA project
 
## Instructions to run RASA project:

First, we need to install the necessary libraries. On the command line, run:

`pip install rasa`

`pip install flask` 

To interact with the rasa model, we need to start the rasa server. To start the server, utilize the following command on the command line: 

`rasa run -m models --enable-api`

## Instructions to run FLASK webapp containing RASA

Once the rasa server is running, we need to start the flask server by running `app.py`. To do this, navigate to the flaskr folder and run the server by entering the following commands:

`cd flaskr`

`py app.py`

Then navigate to the port where `app.py` is running in your browser. The default is `http://127.0.0.1:5000`. You are good to go!