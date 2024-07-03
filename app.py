from flask import Flask, request, render_template
from stories import Story, story

app = Flask(__name__)

@app.route("/")
def index():

    return render_template("madlib.html", prompts=story.prompts)

@app.route("/story")
def story_page():

    return story.generate(request.args)