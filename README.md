# 🌸 Flower Classification using CNN

An AI-powered web app for real-time flower image classification using a Convolutional Neural Network (CNN).
Built with **Flask**, **HTML5/CSS3**, and trained on 4,000+ flower images.

---

## 🌼 Supported Flower Classes

* 🟣 **Daisy**
* 🟡 **Dandelion**
* 🌹 **Rose**
* 🌻 **Sunflower**
* 🌷 **Tulip**

---

## 🎯 Project Objectives

* 🧠 Build a CNN model to classify flower images
* 🎨 Create a modern front-end for image uploads
* ⚡️ Serve predictions in real-time using Flask
* 🔧 Make it modular and easy to update or extend

---

## 🌐 Key Features

* 📄 **Image Upload**: Drag-and-drop or file-select interface with preview
* 🧠 **CNN Model**: Conv2D, Dropout, ReLU, trained on 4,000+ images
* 📡 **Real-Time Predictions**: Instant results on image upload
* 🎨 **Responsive UI/UX**: Clean, mobile-friendly design using HTML/CSS
* 📊 **Training Graphs**: Accuracy/loss visualizations
* 📀 **Model Storage**: Saved `.h5` model with optional `.pkl` history

---

## 📁 Project Structure

```plaintext
flower_classification_project/
├── app.py               # Flask web server
├── train.py             # Model training script
├── Model.h5             # Trained CNN model
├── static/
│   ├── images/          # Demo images/screenshots
│   └── uploads/         # Uploaded image files
├── templates/
│   ├── index.html       # Main upload UI
│   └── result.html      # Prediction result display
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## ⚙️ Installation & Setup

### 🔹 Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/flower_classification_project.git
cd flower_classification_project
```

### 🔹 Step 2: Create Virtual Environment

```bash
python -m venv venv
```

#### On Windows:

```bash
venv\Scripts\activate
```

#### On macOS/Linux:

```bash
source venv/bin/activate
```

### 🔹 Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### 🔹 Step 4: Run the App

```bash
python app.py
```

Then open your browser at:
[http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🧠 CNN Model Overview

* **Input Shape**: `128 x 128 x 3`
* **Layers**: Conv2D, MaxPooling, Dropout, Flatten, Dense
* **Activations**: ReLU, Softmax
* **Loss Function**: Categorical Crossentropy
* **Optimizer**: Adam
* **Epochs**: 25
* **Metrics**: Accuracy, Loss

---

## 🖼️ Demo Screenshots

![Prediction Result 1](https://raw.githubusercontent.com/taj-shabreen/Flower_Classification/main/static/images/prediction_result1.png)

![Prediction Result 2](https://raw.githubusercontent.com/taj-shabreen/Flower_Classification/main/static/images/prediction_result2.png)


---

## 📚 Dataset Source

* **Source**: [Kaggle – Flowers Recognition Dataset](https://www.kaggle.com/datasets/alxmamaev/flowers-recognition)
* **Categories**: Daisy, Dandelion, Rose, Sunflower, Tulip
* **Total Images**: \~4,242

---

## 📦 Dependencies

Install all required libraries using:

```bash
pip install -r requirements.txt
```

### 🗂️ Key Packages

```ini
Flask==3.0.3
TensorFlow==2.17.0
Keras==3.6.0
NumPy==1.26.4
Pillow==10.4.0
opencv-python==4.10.0.84
scikit-learn==1.5.2
```

---

## 🧹 Future Enhancements

* ✅ Add **Transfer Learning** (e.g., MobileNetV2, VGG16)
* 📸 **Webcam Support** for real-time camera uploads
* 🌸 Expand to **10+ flower classes**
* 🗃️ Add **SQLite/PostgreSQL** for storing logs and predictions
* 🐳 **Dockerize** for production deployment
* 📱 Integrate with **Android/iOS** app

---

## 💼 Use Cases

* 🧪 Academic projects – image recognition & AI
* 🌷 Botany tools – identify flower species
* 📷 Mobile/IoT integration – future apps
* 💻 Portfolio/Demo – practical ML showcase

---

## 👤 Maintainer

**Shabreen Taj**
🔗 GitHub: [@taj-shabreen](https://github.com/taj-shabreen)

---

## ⭐️ Show Your Support

If you like this project, give it a ⭐ on GitHub and share it!
