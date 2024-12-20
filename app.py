import os
from flask import Flask, request, jsonify
from PIL import Image
from io import BytesIO
from minio import Minio
from minio.error import S3Error

# Load MinIO configuration from environment variables or use default values
MINIO_HOST = os.getenv("MINIO_URL", "yveanepc:9000")
MINIO_ACCESS_KEY = os.getenv("MINIO_ACCESS_KEY", "admin")
MINIO_SECRET_KEY = os.getenv("MINIO_SECRET_KEY", "admin123")

# Initialize MinIO client
minio_client = Minio(
    MINIO_HOST,
    access_key=MINIO_ACCESS_KEY,
    secret_key=MINIO_SECRET_KEY,
    secure=False,
)

# Ensure the bucket exists
BUCKET_NAME = "lab-2"
if not minio_client.bucket_exists(BUCKET_NAME):
    minio_client.make_bucket(BUCKET_NAME)

app = Flask(__name__)

@app.route('/process-image', methods=['POST'])
def process_image():
    try:
        # Get scale from query parameter, default to 0.25 if not provided
        scale = float(request.args.get('scale', 0.25))

        # Check if the file is in the request
        if 'file' not in request.files:
            return jsonify({"error": "No file part"}), 400

        file = request.files['file']
        if file.filename == '':
            return jsonify({"error": "No selected file"}), 400

        # Open the image and apply scaling
        img = Image.open(file.stream)
        new_width = int(img.width * scale)
        new_height = int(img.height * scale)
        img = img.resize((new_width, new_height))  # Resize image

        # Save the image to a BytesIO object
        img_byte_array = BytesIO()
        img.save(img_byte_array, format="JPEG")
        img_byte_array.seek(0)

        # Modify the object name to include the scale (e.g., "image_0.5.jpg")
        original_filename, file_extension = os.path.splitext(file.filename)
        object_name = f"{original_filename}_{scale}{file_extension}"  # New name with scale

        # Upload the image to MinIO
        try:
            minio_client.put_object(
                BUCKET_NAME,
                object_name,
                BytesIO(img_byte_array.getvalue()),
                len(img_byte_array.getvalue())
            )
            return jsonify({"message": "Image processed and uploaded successfully!"}), 200
        except S3Error as e:
            return jsonify({"error": f"Failed to upload image: {str(e)}"}), 500

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)

