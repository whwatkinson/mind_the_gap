from os import getenv


NEO4J_USERNAME = getenv("NEO4J_USERNAME", "neo4j")
NEO4J_PASSWORD = getenv("NEO4J_PASSWORD", "password")
NEO4J_DATABASE_URL = f"bolt://{NEO4J_USERNAME}:{NEO4J_PASSWORD}@localhost:7687"
