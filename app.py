from flask import Flask
from pymongo import MongoClient
import json


client = MongoClient()
app = Flask(__name__)
database = client.local


@app.route("/words", methods=['GET'])
def words():
    words = list(database.get_collection("words").find({}))
    for word in words:
        del word['_id']
    return json.dumps(words)


if __name__ == "__main__":
    app.run()
