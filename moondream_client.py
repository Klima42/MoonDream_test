import moondream as md
from PIL import Image

# Path to the Moondream model file
model_path = r"C:\traitement\ai_image\moondream_env\moondream-2b-int8.mf"
model = md.vl(model=model_path)

# Path to the image to process
image_path = r"path_to_image.jpg"

# Load and process the image
image = Image.open(image_path)
encoded_image = model.encode_image(image)

# Generate a caption
caption = model.caption(encoded_image)["caption"]
print(f"Caption: {caption}")

# Ask a question
question = "What is the person doing?"
answer = model.query(encoded_image, question)["answer"]
print(f"Answer: {answer}")
