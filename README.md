# Notebook Merger

A simple web application built with Flask that allows users to upload multiple Jupyter Notebooks (.ipynb files), rearrange them, and merge them into a single notebook. The merged notebook can then be downloaded directly from the interface.

## Features
- **Upload Jupyter Notebooks**: Allows users to upload multiple `.ipynb` files.
- **Rearrange Files**: Users can reorder the uploaded files by dragging and dropping them.
- **Delete Files**: Users can delete any file before merging.
- **Merge Notebooks**: Merges the notebooks in the selected order and prepares the merged notebook for download.
- **Download Merged Notebook**: Once the merge is complete, the merged file is available for download.

## Tech Stack
- **Backend**: Flask (Python)
- **Frontend**: HTML, JavaScript (with jQuery for DOM manipulation)
- **File Handling**: FormData (for uploading), File System (for reading and writing `.ipynb` files)

## Installation

### Prerequisites
- Python 3.x

### Steps to Set Up

1. Clone the repository to your local machine.

    ```bash
    https://github.com/automatefreely/ipynb-merger
    cd ipynb-merger
    ```

2. Create a virtual environment (recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the Flask application:

    ```bash
    python app.py
    ```

5. Open a browser and navigate to `http://localhost:5000`.

## Usage

1. **Upload Notebooks**: Click the "Upload" button and select multiple `.ipynb` files to upload.
2. **Rearrange Files**: Once the files are uploaded, they will appear in a list. You can drag and drop them to reorder.
3. **Delete Files**: If you need to remove any notebook, click the "Delete" button next to the file.
4. **Merge Notebooks**: Once you’re satisfied with the order of the files, click the "Merge Notebooks" button to merge them.
5. **Download Merged Notebook**: After merging, the link to download the merged notebook will appear. Click it to download the file.

## File Structure

```
/project-root
    /templates
        index.html                # HTML template for the frontend
    /uploads
        # Uploaded notebook files will be stored here
    app.py                         # Flask application logic
    requirements.txt               # List of dependencies
    README.md                      # This README file
```

## Endpoints

- **`POST /`**: Handles file uploads. Accepts multiple `.ipynb` files and stores them in the server.
- **`POST /merge`**: Merges the uploaded Jupyter notebooks and returns the merged file.
- **`POST /delete`**: Deletes a specified notebook file from the server.
- **`GET /download`**: Provides the merged notebook for download.

## Requirements

- Flask
- nbmerge (or similar library for merging notebooks)

To install the required libraries, run:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file should include the necessary libraries for Flask and `nbmerge` (or an alternative method for merging Jupyter Notebooks).

---

## Contributing

1. Fork the repository.
2. Clone your fork locally.
3. Create a new branch for your feature (`git checkout -b feature-name`).
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push your changes to your fork (`git push origin feature-name`).
6. Create a pull request to the main repository.

---

## License

This project is open-source and available under the MIT License.
