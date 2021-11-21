from flask import Flask, request, render_template
import ast

app = Flask(__name__)


@app.route('/')
def input_form():
    return render_template('input-form.html')


@app.route('/', methods=['POST'])
def input_form_post():
    # text = request.form['version']
    versionlist = ast.literal_eval(request.form['version'])
    versionlist.sort(reverse=True)
    processed_text = str(versionlist)
    return processed_text


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
