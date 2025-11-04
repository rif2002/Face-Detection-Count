# 🎯 Face Detection App  

An interactive **Face Detection Application** built using **Python**, **OpenCV**, and **Pygame**.  
This app captures live video from your webcam, detects faces in real-time, and displays the **number of faces detected** on the screen — all within a custom-designed Pygame interface.  

---

## Features  
- ✅ Real-time face detection using OpenCV’s Haar Cascade Classifier  
- ✅ Displays the **count of detected faces** dynamically  
- ✅ Live webcam feed displayed in a Pygame window  
- ✅ Stylish UI with custom background and design elements  
- ✅ Smooth integration of computer vision and interactive graphics  

---

## Tech Stack  
- **Python 3.x**  
- **OpenCV** – for computer vision and face detection  
- **NumPy** – for array and image data handling  
- **Pygame** – for creating the graphical interface  

---

## 🚀 How It Works  

1. The app initializes a webcam feed using `cv2.VideoCapture(0)`.  
2. Each frame is converted to grayscale for face detection.  
3. Faces are detected using OpenCV’s `haarcascade_frontalface_default.xml`.  
4. A red bounding box and corner lines are drawn around each detected face.  
5. The total number of detected faces is shown at the top of the window.  
6. Pygame renders the video feed, text, and background image together.  

---

## 📂 Project Structure  

Face-Detection-App/
│
├── main.py # Main Python file
├── haarcascade_frontalface_default.xml # Haar Cascade model file
├── bg1.png # Background image for UI
└── README.md # Project documentation

## Installations
pip install opencv-python pygame numpy

## Future Enhancements
🔹 Add detection for tilted or side faces using MTCNN or Dlib
🔹 Integrate emotion or age-gender prediction models
🔹 Enhance UI with start/stop buttons and animations
