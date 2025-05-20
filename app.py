
import streamlit as st
from PIL import Image
import pytesseract
import pandas as pd
import io
import base64
import requests

# Funzione per parsing simulato (da sostituire con GPT in produzione)
def parse_text(text):
    # Logica semplificata per parsing
    return {
        "Author": "Brice Marden",
        "Title": "Bilder und Zeichnungen",
        "Publisher": "Konrad Fischer",
        "Year": "1971",
        "Place of Publication": "Düsseldorf",
        "Size": "21 x 15 cm",
        "Market Value": "€125–450 (ViaLibri)"
    }

# Interfaccia
st.set_page_config(page_title="Cataloguing Prototype", layout="centered")
st.title("📚 Cataloguing App Prototype")
st.markdown("Upload a photo of a book, catalogue or ephemera to extract and structure bibliographic data.")

uploaded_file = st.file_uploader("Upload image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # OCR extraction
    with st.spinner("Extracting text..."):
        text = pytesseract.image_to_string(image, lang='eng+deu+ita')

    st.text_area("OCR Result", text, height=200)

    # Parsing with AI (simulato)
    st.subheader("📄 Parsed Data")
    parsed = parse_text(text)
    df = pd.DataFrame([parsed])
    st.table(df)

    # Download as CSV
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # B64 encode
    href = f'<a href="data:file/csv;base64,{b64}" download="catalogue_entry.csv">📥 Download CSV</a>'
    st.markdown(href, unsafe_allow_html=True)

    # External links (esempio)
    st.subheader("🌐 Market Search")
    title_query = parsed['Title'].replace(' ', '+')
    author_query = parsed['Author'].replace(' ', '+')
    st.markdown(f"[Search on ViaLibri](https://www.vialibri.net/search_results.html?author={author_query}&title={title_query})")
    st.markdown(f"[Search on AbeBooks](https://www.abebooks.com/servlet/SearchResults?an={author_query}&tn={title_query})")
    st.markdown(f"[Search on eBay](https://www.ebay.com/sch/i.html?_nkw={title_query}+{author_query})")
