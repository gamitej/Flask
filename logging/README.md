## Application logging with Flask

Flask logging can change the way you understand debugging and how you interact with logs produced by the application. The Flask logging module gives you a way to record errors over different severity levels. A default logging module is included in the Python standard library, and it provides both simple and advanced logging functions.


## Implementing a Flask logger

Logging allows developers to monitor the flow of a program with actions taken. You can use loggers to track application flows like tracking transactional data in ecommerce applications or recording events when an API call interacts with a service.

### Here is how to use the loggers:

1. Debug provides developers with detailed information for diagnosing program error.
2. Info displays a confirmation message that a program’s flow behavior is executing as expected.
3. Warning shows that something unexpected occurred, or that a problem might occur in the near future (low disk space, for example).
4. Error indicates a serious problem, like the program failed to execute some functionality.
5. Critical shows the occurrence of a serious error in the application, such as a program failure.


## Basic Code:

```
from flask import Flask
import logging

logging.basicConfig(filename='record.log', level=logging.INFO)
app = Flask(__name__)

@app.route('/')
def main():
  # showing different logging levels
  app.logger.debug("debug log info")
  app.logger.info("Info log information")
  app.logger.warning("Warning log info")
  app.logger.error("Error log info")
  app.logger.critical("Critical log info")
  return "testing logging levels."

```