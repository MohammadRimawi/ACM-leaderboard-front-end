from flask import Flask,render_template
from flask_assets import Environment,Bundle
from flask_scss import Scss


app = Flask(__name__)

Scss(app)

bundles = {
    "general.css": Bundle('scss/general.scss', filters='pyscss', output='gen/general.css'),
    "flex.css": Bundle('css/flex.css', output='gen/flex.css'),

}


assets = Environment(app)
assets.register(bundles)

@app.route('/')
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(host="0.0.0.0" ,debug=True)


