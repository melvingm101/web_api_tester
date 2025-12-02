# Web API Tester

This project is a sample Web API tester project. It contains the test website and the files to test Web API security. We would need Python installed to run these files, which we can do here: [Python Download](https://www.python.org/downloads/)

## Setup

- `scanner_files` folder contains bash scripts which can be executed. We need to make sure that these packages are installed first.

- `whatweb`: Responsible for analyzing web request and providing some basic info about the technologies used. 

To start, first we need to create and activate a Python virtual environment. It can be done with the following commands:

- `python -m venv venv`
- `source venv/bin/activate` 

Next, we can then run `pip install -r requirements.txt` to install all the necessary Python packages. Once this is done, we can then head inside the `scanner_files` folder and run `./main.sh`.