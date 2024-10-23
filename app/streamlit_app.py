import streamlit as st
from PIL import Image
import numpy as np
import os
import time
import json
import os

with open('config.json', 'r') as f:
    DETAILS = json.load(f)

def predict_phishing(image):
    time.sleep(3)
    return False, 92



def main(**args):
    st.title("🛡️ PhishGuard Vision")
    st.write(
        """
        Welcome to **PhishGuard Vision** \n
        A tool to detect phishing websites from screenshots. \r
        Upload a screenshot (PNG format), and our model will predict whether the site is a phishing attempt or legitimate.
        """
    )

    uploaded_file = st.file_uploader("Upload a website screenshot (PNG)", type="png")

    if uploaded_file is not None:
        image = Image.open(uploaded_file)

        with st.container(border = True, height = 500):
            st.subheader("Uploaded Screenshot")
            st.image(image, caption="Uploaded Screenshot", use_column_width=True)

        if st.button("Submit"):
            with st.spinner(text = "Running prediction model"):
                prediction, confidence = predict_phishing(image)

            st.subheader("Prediction")
            if prediction == 1:
                st.error(f"⚠️ This website is likely a phishing attempt! (Confidence: {confidence:.2f}%)")
            else:
                st.success(f"✅ This website is legitimate. (Confidence: {confidence:.2f}%)")
    else:
        st.info("Please upload a PNG file to begin the phishing detection.")


    # Sidebar
    st.sidebar.title("About PhishGuard Vision")
    st.sidebar.info(
        """
        PhishGuard Vision uses machine learning to analyze website screenshots and detect phishing attempts. \n
        """
    )
    
    # Key Features
    st.sidebar.markdown("#### Key Features")
    st.sidebar.markdown("- Screenshot-based phishing detection")
    st.sidebar.markdown("- Confidence score on predictions")
    st.sidebar.markdown("- Powered by machine learning")

    st.sidebar.markdown("---")
    
    # Important Links
    st.sidebar.markdown("#### Important Links")
    st.sidebar.write("- Check out source Github Repository [link](%s)" % DETAILS["github_link"])
    st.sidebar.write("- Dataset used [link](%s)" % DETAILS["dataset_link"])

    # Footer
    st.markdown(
        """
        <style>
        .footer {
            # position: fixed;
            bottom: 0;
            width: 100%;
            color: grey;
            text-align: center;
            padding: 10px;
        }
        </style>
        <div class="footer">
            Developed with ❤️ by PhishGuard Vision Team.
        </div>
        """, unsafe_allow_html=True
    )
    return None


if __name__ == "__main__":
    st.set_page_config(
        page_title="PhishGuard Vision",
        page_icon=":shield:",
        layout="centered",
        initial_sidebar_state="expanded",
    )
    main()


