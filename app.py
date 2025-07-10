import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
from PIL import Image
import io


load_dotenv()
genai.configure(api_key="YOUR_API_KEY")


st.set_page_config(page_title="🍎 NutriVision", layout="centered", page_icon="favicon.png")
st.title("🍎 NutriVision - AI Calorie Analyzer")
st.subheader("Upload a food image to get its calorie and health breakdown.")


uploaded_file = st.file_uploader("Upload a food image...", type=["jpg", "jpeg", "png"])


image_part = None


if uploaded_file:
    
    bytes_data = uploaded_file.read()

    
    image = Image.open(io.BytesIO(bytes_data))
    st.image(image, caption="Uploaded Image", use_container_width=True)

    image_part = {
        "mime_type": uploaded_file.type,
        "data": bytes_data
    }

input_prompt = """
Please analyze the dish shown in this image.
- Identify each food item present.
- Provide a detailed calorie breakdown (macronutrients like carbs, fats, proteins if possible).
- Estimate total calories for the entire dish.
- Evaluate the overall healthiness of this meal.
- State whether this meal is advisable to eat or not, and why.
- Suggest the ideal body weight range for which this meal is most suitable.
- Finally, give a health rating out of 10.
"""

# When button is clicked
if st.button("🔍 Analyze Image"):
    if not image_part:
        st.warning("Please upload an image before analyzing.")
    else:
        try:
            with st.spinner("Analyzing with Gemini..."):
                model = genai.GenerativeModel("gemini-1.5-flash")
                response = model.generate_content([input_prompt, image_part])
                st.success("✅ Analysis Complete!")
                st.header("🍽️ Food & Calorie Breakdown")
                st.write(response.text)
        except Exception as e:
            st.error(f" Error: {e}")
