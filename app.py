from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return "<p>Hello, World!</p>"




@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        return "<p>Not yet supported<p>"
        
    return "<p>This is where login happens</p>"


@app.route("/chat")
def chat():
    # This is where app logic happens.
    # Needs to check login, then send request to OpenAI
    return "<p>This is the chat page<p>"