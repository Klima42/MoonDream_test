import time
from flask import Flask, request, jsonify
import moondream as md
from PIL import Image, ImageOps
import io
import os

app = Flask(__name__)

# Initialize the Moondream model
model_path = r"C:\traitement\ai_image\moondream_env\moondream-2b-int82.mf"
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model file not found at: {model_path}")

model = md.vl(model=model_path)

@app.route('/process-image', methods=['POST'])
def process_image():
    try:
        start_time = time.time()  # Start timer

        # Check if an image file is provided
        if 'image' not in request.files:
            return jsonify({"error": "No image file provided"}), 400
        file_received_time = time.time()  # Measure file upload time

        # Read and process the image
        image_file = request.files['image']
        image = Image.open(io.BytesIO(image_file.read()))  # Load image in binary mode
        file_loaded_time = time.time()  # Measure file loading time

        # Resize the image to a reasonable size (e.g., 512x512)
        image = ImageOps.contain(image, (512, 512))
        file_resized_time = time.time()  # Measure resizing time

        # Encode the image
        encoded_image = model.encode_image(image)
        image_encoded_time = time.time()  # Measure encoding time

        # Generate a caption and answer a question
        caption = model.caption(encoded_image)["caption"]
        answer = model.query(encoded_image, "What is the person doing?")["answer"]
        end_time = time.time()  # End timer

        # Log times
        print(f"Time to receive file: {file_received_time - start_time:.2f} seconds")
        print(f"Time to load file: {file_loaded_time - file_received_time:.2f} seconds")
        print(f"Time to resize file: {file_resized_time - file_loaded_time:.2f} seconds")
        print(f"Time to encode image: {image_encoded_time - file_resized_time:.2f} seconds")
        print(f"Time for model inference: {end_time - image_encoded_time:.2f} seconds")
        print(f"Total time: {end_time - start_time:.2f} seconds")

        # Return results as JSON
        return jsonify({
            "caption": caption,
            "answer": answer
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/', methods=['GET'])
def home():
    return '''
        <h1>Upload an Image</h1>
        <form action="/process-image" method="post" enctype="multipart/form-data">
            <input type="file" name="image" required>
            <button type="submit">Analyze Image</button>
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
