# RobustPhysics RASA project

## Necessary packages needed:
Please make sure python verison 3.8, 3.9, or 3.10 as Rasa is only compatible with these python versions. You can download python here: [https://www.python.org/downloads/release/python-31013/](https://www.python.org/downloads/release/python-31013/).

Once python is installed, please clone this github repo, or ensure the code for this github repo is installed. To do so, you can use the command `git clone https://github.com/wrachel/RobustPhysics-RASA-project.git`. 

In order to install Rasa, please use the command `pip install rasa`. Ensure that you are in the folder of the repo you just cloned when running this command. 

## Training the Rasa model: 

Ensure that you are in the Rasa folder. 

Run `rasa train` to train the model. When this command finishes running, you should see the output "Your Rasa model is trained and saved at..."
![image](https://github.com/wrachel/RobustPhysics-RASA-project/assets/40574565/b5f594a3-1096-45e9-b74d-0abfb324dc6e)

To test out the model in your terminal, run the command `rasa shell`. It will recall your most recent model and allow you to interact with the model in the terminal
![image](https://github.com/wrachel/RobustPhysics-RASA-project/assets/40574565/b06e061c-9538-4c66-a7f1-ac78a24516b4)

 
## Instructions to run Rasa project:

To interact with the rasa model, we need to start the rasa server. To start the server, utilize the following command on the command line: 

`rasa run -m models --enable-api`

## Instructions to run FLASK webapp containing RASA

Once the rasa server is running, we need to start the flask server by running `app.py`. To do this, navigate to the flaskr folder and run the server by entering the following commands:

`cd flaskr`

`py app.py`

Then navigate to the port where `app.py` is running in your browser. The default is `http://127.0.0.1:5000`. You are good to go!

## Summary of instructions:
1. Install python version 3.8, 3.9, or 3.10
2. Clone the repository and navigate to the folder
3. Install Rasa using `pip install rasa`
4. Train the Rasa model using `rasa train`, and optionally interact with the model in the terminal using `rasa shell`
5. Use `rasa run -m models --enable-api` to start the rasa server
6. To run the FLASK webapp, navigate to the folder `cd flaskr` and run the script to start the FLASK webapp using `py app.py`
7. Now, Rasa will appear in your local browser at http://127.0.0.1:5000
