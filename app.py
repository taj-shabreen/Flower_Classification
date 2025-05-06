from flask import Flask, render_template, request, url_for
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

# Initialize the Flask app
app = Flask(__name__)

# Load the pre-trained model
model = load_model('Model.h5')

# Mapping class indices to flower names
class_labels = ['Daisy', 'Dandelion', 'Rose', 'Sunflower', 'Tulip']

# Define route for homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            # Save the uploaded image to the 'static/data' directory
            image_dir = os.path.join('static', 'data')
            if not os.path.exists(image_dir):
                os.makedirs(image_dir)

            filepath = os.path.join(image_dir, file.filename)
            file.save(filepath)

            # Preprocess the image for model prediction
            img = image.load_img(filepath, target_size=(224, 224))
            img = image.img_to_array(img)
            img = np.expand_dims(img, axis=0)
            img = img / 255.0  # Normalize

            # Make prediction
            result = model.predict(img)
            predicted_class = class_labels[np.argmax(result)]

            # Return result and show the image on the result page
            return render_template('result.html', image_path=file.filename, prediction=predicted_class)

if __name__ == '__main__':
    app.run(debug=True)
