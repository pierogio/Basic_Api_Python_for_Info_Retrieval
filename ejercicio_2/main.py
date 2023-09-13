from flask import Flask
from controller import Routes
from connector import ConnectorDatabase
from repository import Repository

if __name__ == '__main__':
    app = Flask(__name__)

    db_connector = ConnectorDatabase(
        host="localhost",
        user="root",
        password="root",
        database="escuela"
    )

    repository = Repository(db_connector)
    routes = Routes(app, repository)

    app.run(host='0.0.0.0', port=8080)






