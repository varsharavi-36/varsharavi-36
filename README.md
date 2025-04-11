## 📖 Project Description

Road conditions are crucial in public safety, vehicle maintenance, and transportation efficiency. One of the most common and dangerous defects found on roads is potholes. This project presents an AI-driven solution to detect road potholes from images using **YOLOv8**, a state-of-the-art object detection model developed by **Ultralytics**, and provides a modern, browser-based interface built with **Flask** and **Bootstrap**.

The goal of this project is to create a lightweight and intuitive web-based application where users can upload an image of a road, and instantly receive a processed output highlighting any potholes detected in that image.

The project begins with collecting road images, sourced from open platforms like Google Images. A total of 100 diverse images showcasing road surfaces with varying lighting and angles were collected. These images were then uploaded to **Roboflow**, where each image was carefully annotated manually using bounding boxes around visible potholes. The dataset was split into training (70%), validation (20%), and testing (10%) sets and exported in **YOLOv8** format for training. Training was conducted on **Google Colab**, leveraging its free GPU environment to train the YOLOv8 model over 100 epochs. The training process monitored standard metrics like **precision**, **recall**, and **mean average precision (mAP)**, resulting in a moderately well-performing model given the small dataset.

Post-training, the best-performing model weights were downloaded and integrated into a **Flask** application. The backend is responsible for handling user uploads, performing model inference, saving results, and serving them back to the user via a separate results page. The model is initialized using the **Ultralytics** Python package and performs real-time detection through `model.predict()`. Each uploaded image is stored in a uniquely named file using **UUID**, while the processed image is saved in a result directory.

The web interface is designed with responsiveness and elegance in mind. It uses a **glassmorphism** design, animated gradients, and modern typography to enhance the user experience. The upload form ensures users cannot proceed without selecting a valid image, using both frontend **JavaScript modals** and **Flask server-side validation**. After successful detection, users are presented with a processed image clearly marking any detected potholes, along with an option to return and analyze another image.

This project is not just a demonstration of AI capabilities but also an example of how deep learning models can be seamlessly integrated into user-friendly web applications. It opens the door to scalable real-world deployment scenarios, where such a model could be integrated with road surveillance systems, mobile apps for field workers, or even embedded in dashcams to report road conditions in real-time. Future enhancements may include **batch processing**, **GPS tagging**, **heatmaps**, **mobile optimization**, and **deployment on cloud platforms** for public access.

![image](https://github.com/user-attachments/assets/3fbc03dd-e75b-40e9-b1d8-f7002ed23dd8)            
                                                                            
  **💡 Technologies Used**
  
🔍 YOLOv8 (Ultralytics)

🧠 Python 3.10

🌐 Flask (Web framework)

🧩 HTML5 + CSS3 + Bootstrap 5

🧾 Roboflow (Image Annotation & Dataset Export)

☁️ Google Colab (Model Training)

🖼 OpenCV, PIL

💻 Visual Studio Code

**🔄 Project Workflow**

**📦 1. Dataset Collection & Annotation (Roboflow)**

✅ 100 images collected from Google Images, featuring various road conditions.

✅ Uploaded and annotated manually in Roboflow

✅ Annotation label used: POTHOLE

✅ Dataset split into:

70% Training

20% Validation

10% Testing

✅ Exported in YOLOv8 format and mounted to Google Drive for training

**☁️ 2. Model Training (Google Colab)**

✅ Platform: Google Colab (with GPU)

✅ Base model: yolov8n.pt

✅ Training config:

from ultralytics import YOLO
model = YOLO("yolov8n.pt")
model.train(data="data.yaml", epochs=100, imgsz=640)

✅ Final model: best.pt

✅ Performance Metrics:

Precision: 0.477

Recall: 0.356

mAP@0.5: 0.383

mAP@0.5:0.95: 0.205

Inference speed: 30.1 ms/image

**💻 3. Web Application Development (Flask + Bootstrap)**

✅ Built using Flask and Bootstrap for clean backend + frontend integration

✅ User uploads image → YOLOv8 processes → Result image with bounding boxes is returned

✅ Uploaded images stored in static/uploads/

✅ Processed images stored in static/results/

✅ YOLOv8 loaded with:model = YOLO("best.pt")

✅ Used uuid4 to generate unique filenames to prevent overwrite

✅ Modal popups and server-side validations to handle empty uploads

**🌐 Web Interface Overview**

Sleek, responsive form styled with Bootstrap

Glassmorphic UI design with animated background

File validation with popup modal if user attempts to submit without selecting a file

**🔹 Result Page (/predict)**

![Screenshot 2025-04-11 115001](https://github.com/user-attachments/assets/530f3337-c6d2-4c8f-bb5d-9c810f396a06)


**🔹 Backend Logic**

YOLOv8 .predict() processes it
Annotated output saved and path passed to HTML
Result page renders the final detection image

**📁 Folder Structure**

csharp

pothole_app/
├── app.py                  # Flask backend
├── best.pt                 # YOLOv8 trained model
├── roaddamage.ipynb        # Training code (Colab)
├── requirements.txt        # Python packages
├── templates/
│   ├── index.html          # Upload form
│   └── result.html         # Result view
└── static/
    ├── uploads/            # User uploads
    └── results/            # YOLOv8 output
    
**🚀 Running the App Locally**

Step 1: Clone the repository
git clone https://github.com/your-username/pothole-detector.git
cd pothole-detector

Step 2: Install requirements
pip install -r requirements.txt

Step 3: Launch the Flask app
python app.py
Then open http://127.0.0.1:5000 in your browser.

**🔍 Key Features**

📤 Upload road images via web UI

🧠 YOLOv8-based real-time pothole detection

🖼️ Annotated results displayed in-browser

💬 User-friendly modal alerts

📱 Responsive design with modern aesthetics

**🧪 Sample Code**

from ultralytics import YOLO

model = YOLO("best.pt")
results = model("static/uploads/input.jpg")
results.save("static/results/output.jpg")

**📜 License**
This project is licensed under the MIT License.
For commercial use of YOLOv8, visit Ultralytics Licensing.

**🙋 Author**

**Varsha Ravishankar**

**📧 Email: varsha.ravishankar36@gmail.com**

**🌐 GitHub: @varsharavi-36**

“Using AI to make roads safer.”                                                                          

