

from flask import Flask, render_template

from .assets import assets
from . import config

def create_app(config=config.base_config):
  app = Flask(__name__)
  app.config.from_object(config)

  assets.init_app(app)

  @app.route("/")
  def hello_world():
    return render_template("index.html")


  return app