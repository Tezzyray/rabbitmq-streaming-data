Producer-Consumer Data Streaming using RabbitMQ
This project shows how to create and use synthetic temperature and humidity data in real-time using RabbitMQ in a basic data streaming framework.

Conditions
Python 3.6+
Locally operating RabbitMQ server (or reachable over a network)
Setting up
Make a clone of the repository:
Git clone <url of repository>
cd data-rabbitmq-streaming
Use pip to install dependencies:

Use Producer: pip install -r requirements.txt
Synthetic temperature and humidity data are created by the producer script and published to a RabbitMQ exchange.


Producer.py in Python
Purchaser
After establishing a connection with RabbitMQ, the consumer script reads the data from the queue and handles each message.

Consumer.py in Python Configuration
Ascertain that RabbitMQ is installed and operational on port 5672, the default, locally.
In Producer.py and Consumer.py, change localhost if RabbitMQ is hosted somewhere else.
Project Organization
Synthetic data can be created and published to RabbitMQ using Producer.py.
Consumer.py: Establishes a connection with RabbitMQ, reads and interprets messages.
Requirements.txt: Enumerates project-related dependencies.
Making a Contribution: We appreciate your help! Kindly create a branch in the repository and send pull requests that include enhancements or bug fixes.

Permission
For further information, refer to the LICENSE file. This project is licensed under the MIT License.

Recognitions
Pika is a Python package designed to communicate with RabbitMQ.
Faker is a Python package that creates fictitious information.
Make Contact
To report problems or inquire about this project, file a GitHub issue.


