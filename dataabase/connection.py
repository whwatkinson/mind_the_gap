from neomodel import config, db

from settings.environment_variables import NEO4J_DATABASE_URL

config.DATABASE_URL = NEO4J_DATABASE_URL


class DatabaseConnection:
    def __init__(self, database_url: str):
        self.connection = db.set_connection(database_url)
