# OCR Project on Streamlit

Welcome to my OCR (Optical Character Recognition) Project on Streamlit! This project is designed to provide users with a seamless and intuitive experience for converting images containing text into editable and searchable formats.

## Table of Contents

- [About](#about)
- [Usage Guide](#usage-guide)
- [Installation](#installation)
- [Dependencies](#dependencies)
- [How to Use](#how-to-use)
- [Contributing](#contributing)


## About

This OCR Project on Streamlit is powered by advanced OCR technology, providing accurate text extraction from various image formats. The user-friendly interface and real-time processing make it convenient for anyone to use.

## Usage Guide

1. Choose the 'OCR' tab on the left sidebar.
2. Click the 'Upload your Image or PDF' button to upload an image containing text.
3. Supported image formats: PNG and PDF.
4. For PDFs, each page will be processed separately.
5. Once the image is uploaded, the OCR processing will begin.
6. The extracted text will be displayed below the image.

## Installation

To use this project locally, follow the steps below:

1. Clone the repository:

   ```
   git clone https://github.com/your-username/OCR-Project-on-Streamlit.git
   ```

2. Install the required dependencies:

   ```
   pip install streamlit st_on_hover_tabs pytesseract opencv-python-headless pillow pdf2image numpy
   ```

3. Make sure to have the Poppler library installed and add its path to the code as specified in the project.

## Dependencies

- streamlit
- st_on_hover_tabs
- pytesseract
- opencv-python-headless
- pillow
- pdf2image
- numpy

## How to Use

1. Run the Streamlit app locally:

   ```
   streamlit run app.py
   ```

2. Open your web browser and navigate to the provided local address (usually `http://localhost:8501`).

3. Follow the instructions in the Streamlit app to upload your image or PDF and extract the text.


## Contributing

Contributions are welcome! If you have any suggestions, feature requests, or bug reports, please open an issue or submit a pull request.
