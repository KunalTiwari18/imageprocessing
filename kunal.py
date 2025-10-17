import streamlit as st
from PIL import Image, ExifTags

st.set_page_config(page_title="Image Metadata Viewer", layout="centered")
st.title("🔍 Image Metadata Viewer")
st.write("Upload any photo to see its main EXIF metadata (camera, date, GPS, etc.)")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Image", use_container_width=True)

    exif_data = img._getexif()

    if exif_data:
        st.subheader("📊 Metadata")
        exif_dict = {}
        for tag, value in exif_data.items():
            decoded = ExifTags.TAGS.get(tag, tag)
            # Only include main EXIF fields you want
            if decoded in [
                "ImageWidth", "ImageLength", "GPSInfo", "ExifOffset",
                "Make", "Model", "Orientation", "DateTime",
                "ShutterSpeedValue", "ApertureValue", "ExifImageWidth",
                "ExifImageHeight", "DateTimeOriginal", "DateTimeDigitized"
            ]:
                exif_dict[decoded] = value

        for key, val in exif_dict.items():
            st.write(f"{key}:** {val}")
    else:
        st.info("No EXIF metadata found in this image.")
else:
    st.info("Please upload an image to view metadata.")