from flask import Flask, render_template, request
from colorthief import ColorThief

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return render_template('index.html', error='No file part')

    file = request.files['file']

    if file.filename == '':
        return render_template('index.html', error='No selected file')

    # Save the uploaded file
    file.save(file.filename)

    # Get the most common colors from the uploaded image
    color_thief = ColorThief(file.filename)
    palette = color_thief.get_palette(color_count=5)

    return render_template('result.html', colors=palette)


if __name__ == '__main__':
    app.run(debug=True)
