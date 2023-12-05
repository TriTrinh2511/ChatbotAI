from flask import Flask
from rasa import Rasa
from flask_cors import CORS

app = Flask(__name)
rasa = Rasa()

# Allow CORS for all origins
CORS(app)

# ... (other Rasa server setup code)

if __name__ == '__main__':
   app.run()
