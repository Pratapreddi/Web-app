from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask on port 5000! 🚀"

@app.route("/about")
def about():
    return "This is running on port 5000."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

