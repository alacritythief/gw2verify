from flask import Flask, render_template
from verify import *

app = Flask(__name__)

@app.route("/")
@app.route("/<api_key>")
def index(api_key=None):

    if api_key is not None:
        verify = define_person(api_key)
    else:
        verify = None

    return render_template('index.html', context=verify)

if __name__ == "__main__":
    app.debug = True
    app.run()
