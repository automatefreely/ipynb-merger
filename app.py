import os
import io
import nbformat
from flask import Flask, request, render_template, send_file, jsonify

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
MERGED_FILE = "merged.ipynb"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Ensure upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def merge_notebooks(base_dir, file_paths):
    """Merge multiple Jupyter notebooks into one."""
    merged, metadata = None, []

    if not file_paths:
        return None

    for path in file_paths:
        full_path = os.path.join(base_dir, path)
        with io.open(full_path, 'r', encoding='utf-8') as fp:
            nb = nbformat.read(fp, as_version=4)

        metadata.append(nb.metadata)

        if merged is None:
            merged = nb
        else:
            merged.cells.extend(nb.cells)

    # Merge metadata from all notebooks
    merged_metadata = {}
    for meta in reversed(metadata):
        merged_metadata.update(meta)
    merged.metadata = merged_metadata

    return merged

@app.route("/", methods=["GET", "POST"])
def upload_files():
    """Render the upload form and handle file uploads."""
    if request.method == "POST":
        files = request.files.getlist("files")

        if not files:
            return "No files uploaded", 400

        saved_files = []
        for file in files:
            if file.filename.endswith(".ipynb"):
                file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
                file.save(file_path)
                saved_files.append(file.filename)

        return jsonify({"message": "Files uploaded", "files": saved_files})

    return render_template("index.html")

@app.route("/delete", methods=["POST"])
def delete_file():
    """Delete a selected `.ipynb` file."""
    filename = request.json.get("filename")
    if not filename:
        return jsonify({"error": "Filename not provided"}), 400

    file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    
    if os.path.exists(file_path):
        os.remove(file_path)
        return jsonify({"message": f"{filename} deleted successfully"})
    return jsonify({"error": "File not found"}), 404

@app.route("/merge", methods=["POST"])
def merge_files():
    """Merge selected `.ipynb` files."""
    file_order = request.json.get("files")

    if not file_order:
        return jsonify({"error": "No files provided for merging"}), 400

    try:
        merged_nb = merge_notebooks(app.config["UPLOAD_FOLDER"], file_order)
        if merged_nb is None:
            return jsonify({"error": "No valid notebooks to merge"}), 400

        merged_path = os.path.join(app.config["UPLOAD_FOLDER"], MERGED_FILE)
        with open(merged_path, "w", encoding="utf-8") as f:
            nbformat.write(merged_nb, f)

        return jsonify({"message": "Merge successful", "download_url": "/download"})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/download")
def download_file():
    """Download the merged notebook."""
    merged_path = os.path.join(app.config["UPLOAD_FOLDER"], MERGED_FILE)
    if os.path.exists(merged_path):
        return send_file(merged_path, as_attachment=True)
    return "Merged file not found", 404

if __name__ == "__main__":
    app.run(debug=True)
