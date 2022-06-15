from flask import Flask
import logging

logging.basicConfig(filename='record.log', level=logging.INFO)
app = Flask(__name__)

@app.route('/')
def main():
  app.logger.debug("debug log info")
  app.logger.info("Info log information")
  return "testing logging levels."

@app.route('/main')
def aps():
  return 'HI ami'

if __name__ == '__main__':
  app.run(debug=True)