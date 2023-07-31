import streamlit as st 
from st_on_hover_tabs import on_hover_tabs
import base64
import pytesseract
import cv2
from PIL import Image
from pdf2image import convert_from_bytes
import numpy as np    

@st.cache_data
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover;
        

    }}
    </style>
    """,
    unsafe_allow_html=True
    )

def bounding_box(image):
    height, width, _ = image.shape
    boxes = pytesseract.image_to_boxes(image)

    for box in boxes.strip().split("\n"):
        box_data = box.split(' ')
        char, x_min, y_min, x_max, y_max, _ = box_data
        x_min, y_min, x_max, y_max = int(x_min), int(y_min), int(x_max), int(y_max)
        cv2.rectangle(image, (x_min, height - y_min), (x_max, height - y_max), (0, 255, 0), 2)

    return image




st.set_page_config(layout="wide")
add_bg_from_local('F:\OCR app\image.png')
st.markdown('<style>' + open('style.css').read() + '</style>', unsafe_allow_html=True)


with st.sidebar:
    tabs = on_hover_tabs(tabName=['Home','OCR'], 
                         iconName=['info','history_edu'], default_choice=0)

if tabs=="Home":
    st.title("OCR Project on Streamlit")
    st.markdown("Welcome to my OCR (Optical Character Recognition) Project on Streamlit!")
    st.markdown("This OCR Project is designed to provide users with a seamless and intuitive experience for converting images containing text into editable and searchable formats.")

    st.subheader("About")
    st.markdown("This OCR Project on Streamlit is powered by advanced OCR technology, providing accurate text extraction from various image formats. The user-friendly interface and real-time processing make it convenient for anyone to use.")

    st.subheader("Usage Guide")
    st.markdown("1. Choose the 'OCR' tab on the left sidebar.")
    st.markdown("2. Click the 'Upload your Image or PDF' button to upload an image containing text.")
    st.markdown("3. Supported image formats: PNG and PDF.")
    st.markdown("4. For PDFs, each page will be processed separately.")
    st.markdown("5. Once the image is uploaded, the OCR processing will begin.")
    st.markdown("6. The extracted text will be displayed below the image.")
 

elif tabs=="OCR":
    text = ""
    image_file=st.file_uploader('Upload your Image or PDF here',type=["png","pdf"])
    if image_file is not None:
        if image_file.type=="application/pdf":
            pages = convert_from_bytes(image_file.read(), 500,poppler_path=r"C:\Program Files\poppler-23.07.0\Library\bin")
            for page in pages:
                image_np = np.array(page)
                boxed_image=bounding_box(image_np)
                st.image(boxed_image, caption="Image with Bounding Boxes", width=500)
                text_data = pytesseract.image_to_string(page)

                st.header("Extracted Text")
                st.write(text_data)

        else :
            image = Image.open(image_file)
            image_np = np.array(image)
            boxed_image=bounding_box(image_np)
            st.image(boxed_image, caption="Image with Bounding Boxes", use_column_width=False)
            text = pytesseract.image_to_string(image)
            st.header("Extracted Text")
            st.write(text)
        



       

