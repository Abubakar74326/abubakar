# from typing import Optional
# from fastapi import FastAPI

from flask import Flask
import factorialcode

app = Flask(__name__)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.route("/factorial/<int:num>/")
def read_item(num: int):
    fact = factorialcode.factorial(num)
    return {"factorial": fact}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)
