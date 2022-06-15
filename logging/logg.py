from flask import Flask
import logging
import os
 
app = Flask(__name__)
 
@app.before_first_request
def before_first_request():
    log_level = logging.INFO
 
    for handler in app.logger.handlers:
        app.logger.removeHandler(handler)
 
    root = os.path.dirname(os.path.abspath(__file__))
    logdir = os.path.join(root, 'logs')
    if not os.path.exists(logdir):
        os.mkdir(logdir)
    log_file = os.path.join(logdir, 'app.log')
    handler = logging.FileHandler(log_file)
    handler.setLevel(log_level)
    app.logger.addHandler(handler)
    app.logger.setLevel(log_level)
 

@app.route("/")
def main():
    logging.debug("main log debug")
    app.logger.info("main log info")
    app.logger.warning("main log warning")
    app.logger.error("main log error")
    app.logger.critical("main log critical")
    return 'hi'

@app.route("/login")
def login():
    app.logger.info("amitej")
    return "Hi"



if __name__ == '__main__':
    app.run(debug=True)