from flask import Flask, render_template, request, redirect, url_for, flash
from ultralytics import YOLO
import os
import uuid

app = Flask(__name__)
app.secret_key = "your_secret_key"

# Folder paths
UPLOAD_FOLDER = 'static/uploads'
RESULT_FOLDER = 'static/results'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['RESULT_FOLDER'] = RESULT_FOLDER

# Create folders if not exist
for folder in [UPLOAD_FOLDER, RESULT_FOLDER]:
    if os.path.isfile(folder):
        os.remove(folder)
    os.makedirs(folder, exist_ok=True)

# Load model
model = YOLO('best.pt')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        if 'image' not in request.files:
            flash('⚠️ Image not uploaded. Please choose an image.')
            return redirect(url_for('index'))

        file = request.files['image']
        if file.filename == '':
            flash('⚠️ No file selected. Please choose an image.')
            return redirect(url_for('index'))

        filename = f"{uuid.uuid4().hex}.jpg"
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(image_path)

        results = model.predict(image_path, save=True, project=RESULT_FOLDER, name=filename.split('.')[0], exist_ok=True)

        result_image_path = os.path.join(
            RESULT_FOLDER,
            filename.split('.')[0],
            os.path.basename(image_path)
        )
        result_image_web_path = '/' + result_image_path.replace('\\', '/')

        return render_template('result.html', result_image=result_image_web_path)

    # If GET request (like visiting /predict directly)
    flash("⚠️ Image not uploaded. Please choose an image.")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
