import streamlit as st
import google.generative_ai as genai

# --- SAYFA AYARLARI ---
st.set_page_config(
    page_title="What If? – Simülatör",
    page_icon="🔮",
    layout="centered"
)

# --- API ANAHTARI KONTROLÜ ---
# Secrets ayarlarından anahtarı çeker
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("⚠️ API Anahtarı bulunamadı! Lütfen Streamlit ayarlarından 'Secrets' kısmına ekleyin.")

# --- BAŞLIK VE GİRİŞ ---
st.title("🔮 What If? (Olasılık Simülatörü)")
st.subheader("Karar vermeden önce, sonucunu yaşa.")
st.write("Aklındaki eylemi yaz, yapay zeka senin için olasılıkları hesaplasın.")

# --- KULLANICI GİRİŞİ ---
user_input = st.text_area("Ne yapmayı düşünüyorsun?", placeholder="Örn: Patronuma zam istediğimi söylersem ne olur?")

# --- BUTON VE SONUÇ ---
if st.button("Geleceği Gör 🚀"):
    if not user_input:
        st.warning("Lütfen önce bir senaryo yaz.")
    else:
        with st.spinner("Olasılıklar hesaplanıyor..."):
            try:
                model = genai.GenerativeModel('gemini-pro')
                prompt = f"Sen bir simülatörsün. Kullanıcı şunu yapmak istiyor: '{user_input}'. Olası sonuçları, riskleri ve tavsiyeleri maddeler halinde, samimi bir dille anlat."
                
                response = model.generate_content(prompt)
                st.markdown(response.text)
                st.success("Simülasyon tamamlandı!")
            except Exception as e:
                st.error(f"Bir hata oluştu: {e}")
