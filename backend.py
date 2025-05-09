from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from pymongo import MongoClient
from bson import ObjectId
import json
import os
import datetime

class MongoJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()
        return super().default(obj)

app = Flask(__name__)
app.json_encoder = MongoJSONEncoder

# MongoDB configuration
client = MongoClient("mongodb://localhost:27017/")
db = client["bearing_fault_detection"]
collection = db["uploads"]

# Directory to save uploaded files
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No file selected"}), 400

    try:
        # Create timestamp-based filename to avoid duplicates
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        original_filename = secure_filename(file.filename)
        filename = f"{timestamp}_{original_filename}"
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        
        # Ensure upload directory exists
        os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)
        
        # Save file
        file.save(filepath)

        # Store metadata in MongoDB
        document = {
            "original_filename": original_filename,
            "saved_filename": filename,
            "filepath": filepath,
            "timestamp": datetime.datetime.now(),
            "output": request.form.get("output", "N/A"),
            "input_type": request.form.get("input_type", "N/A"),
        }
        
        result = collection.insert_one(document)
        document['_id'] = str(result.inserted_id)
        
        return jsonify({
            "message": "File uploaded successfully",
            "data": document
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/uploads", methods=["GET"])
def get_uploads():
    try:
        # Convert MongoDB cursor to list and handle ObjectId serialization
        uploads = list(collection.find({}))
        for upload in uploads:
            upload["_id"] = str(upload["_id"])
        return jsonify({"uploads": uploads}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
