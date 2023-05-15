from app import app
import os

if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(host="192.168.99.46")
