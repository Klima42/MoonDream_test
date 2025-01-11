# Moondream Image Analyzer

Moondream Image Analyzer is a Flask-based web application that uses the **Moondream vision-language model** to analyze images and provide captions and answers to questions about the uploaded image. It's a user-friendly tool for exploring the capabilities of AI-powered image analysis.

---

## **Features**

- **Upload Images:** Users can upload images through a simple web interface.
- **Generate Captions:** Automatically generates a descriptive caption for the uploaded image.
- **Answer Questions:** Provides answers to specific questions about the image (e.g., "What is the person doing?").
- **GPU Acceleration:** Supports GPU for faster inference using CUDA.
- **Responsive Feedback:** Displays results dynamically after processing the image.

---

## **Project Structure**

```
moondream_env/
├── app.py                  # Flask web application
├── moondream_client.py     # Script for testing Moondream model directly
├── requirements.txt        # Python dependencies
├── package.json            # Node.js dependencies (if applicable)
├── templates/
│   └── index.html          # HTML template for the web interface
├── .gitignore              # Git ignore file
└── moondream-2b-int8.mf    # Moondream model file (ignored by Git)
```

---

## **Installation**

### **1. Clone the Repository**
```bash
git clone git@github.com:Klima42/MoonDream_test.git
cd MoonDream_test
```

### **2. Set Up Python Environment**
1. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate       # On Linux/Mac
   venv\Scripts\activate          # On Windows
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### **3. Set Up Node.js (Optional)**
If you have a `package.json`:
```bash
npm install
```

### **4. Download the Moondream Model**
Place the model file (e.g., `moondream-2b-int8.mf`) in the project directory:
```plaintext
moondream_env/
└── moondream-2b-int8.mf
```

---

## **Usage**

### **1. Start the Flask App**
Run the application:
```bash
python app.py
```

The app will be available at [http://127.0.0.1:5000](http://127.0.0.1:5000).

### **2. Upload an Image**
1. Visit the homepage.
2. Upload an image using the provided form.
3. Click "Analyze" to generate a caption and get answers about the image.

### **3. Example Request via `curl`**
You can also analyze an image directly via the terminal:
```bash
curl -X POST -F "image=@path_to_image.jpg" http://127.0.0.1:5000/process-image
```

---

## **Screenshots**

### **Web Interface**
![Screenshot of the web interface](https://via.placeholder.com/800x400?text=Moondream+Image+Analyzer+Interface)

---

## **Key Technologies**

- **Python**:
  - Flask: Backend web framework.
  - Pillow: Image processing library.
- **Moondream**:
  - Vision-language model for image analysis.
- **JavaScript** (Optional):
  - For dynamic client-side interactivity.

---

## **Optimizations**

1. **GPU Acceleration**:
   The app leverages a GPU using CUDA for faster inference.
2. **Image Resizing**:
   Uploaded images are resized to 512x512 pixels to reduce processing time.

---

## **Development**

### **Run Locally**
```bash
python app.py
```

### **Test the Moondream Model**
```bash
python moondream_client.py
```

### **Run with Gunicorn (Production Mode)**
```bash
gunicorn -w 4 -b 127.0.0.1:5000 app:app
```

---

## **Contributing**

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your feature description"
   ```
4. Push to your branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Create a pull request.

---

## **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## **Acknowledgments**

- [Moondream AI](https://moondream.ai): For providing the vision-language model.
- **Flask**: For powering the web backend.
- **OpenAI**: For assisting with project guidance.

---

## **Contact**

For questions or support, contact:

- **Name**: Kamil Serrai
- **Email**: [kamil.serrai@gmail.com](mailto:kamil.serrai@gmail.com)
- **GitHub**: [Klima42](https://github.com/Klima42)

