
import streamlit as st
import pandas as pd
import base64

# Simulazione di parsing da testo statico (niente OCR)
def parse_text():
    return {
        "Author": "Brice Marden",
        "Title": "Bilder und Zeichnungen",
        "Publisher": "Konrad Fischer",
        "Year": "1971",
        "Place of Publication": "Düsseldorf",
        "Size": "21 x 15 cm",
        "Market Value": "€125–450 (ViaLibri)"
    }

# UI
st.set_page_config(page_title="Cataloguing App Prototype", layout="centered")
st.title("📚 Cataloguing App Prototype (Demo)")
st.markdown("This version skips OCR. Just click the button below to simulate parsed data.")

if st.button("Simulate Parsing"):
    st.subheader("📄 Parsed Data")
    parsed = parse_text()
    df = pd.DataFrame([parsed])
    st.table(df)

    # Download CSV
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="catalogue_entry.csv">📥 Download CSV</a>'
    st.markdown(href, unsafe_allow_html=True)

    # Market value search links
    st.subheader("🌐 Market Search")
    title_query = parsed['Title'].replace(' ', '+')
    author_query = parsed['Author'].replace(' ', '+')
    st.markdown(f"[Search on ViaLibri](https://www.vialibri.net/search_results.html?author={author_query}&title={title_query})")
    st.markdown(f"[Search on AbeBooks](https://www.abebooks.com/servlet/SearchResults?an={author_query}&tn={title_query})")
    st.markdown(f"[Search on eBay](https://www.ebay.com/sch/i.html?_nkw={title_query}+{author_query})")
