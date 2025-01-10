import os
from app import app

env = os.getenv("ENV", "dev")

if env == "dev" and __name__ == "__main__":
    app.run("localhost", 8080, True)
