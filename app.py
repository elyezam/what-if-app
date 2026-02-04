import streamlit as st
import os

# --- 1. KÜTÜPHANE KURULUMU (Otomatik) ---
# requirements.txt dosyasına gerek kalmadan buradan yükler.
try:
    import google.generative_ai as genai
except ImportError:
    os.system("pip install google-generative-ai")
    import google.generative_ai as genai

# --- 2. SAYFA AYARLARI ---
st.set_page_config(
    page_title="What If? – Simülatör",
    page_icon="🔮",
    layout="centered"
)

# --- 3. GOOGLE API ANAHTARINI TANITMA ---
# Streamlit Secrets kısmına girdiğin şifreyi buradan çeker.
try:
    if "GOOGLE_API_KEY" in st.secrets:
        genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    else:
        st.warning("⚠️ API Anahtarı bulunamadı. Lütfen 'Secrets' ayarlarını kontrol edin.")
except Exception as e:
    st.warning(f"Bağlantı ayarlanırken bir sorun oldu: {e}")

# --- 4. BAŞLIK VE GİRİŞ EKRANI ---
st.title("🔮 What If? (Olasılık Simülatörü)")
st.subheader("Karar vermeden önce, sonucunu yaşa.")
st.write("Aklındaki eylemi yaz, yapay zeka senin için olasılıkları hesaplasın, riskleri ölçsün.")

# --- 5. KULLANICI GİRİŞ ALANI ---
user_input = st.text_area("Ne yapmayı düşünüyorsun?", placeholder="Örn: Eski sevgilime 'özledim' mesajı atarsam ne olur?")

# --- 6. BUTON VE SONUÇ ---
if st.button("Geleceği Gör 🚀"):
    if not user_input:
        st.warning("Lütfen önce aklındaki senaryoyu yaz.")
    else:
        with st.spinner("Olasılıklar hesaplanıyor..."):
            try:
                # Google Gemini Modelini Çağır
                model = genai.GenerativeModel('gemini-pro')
                prompt = f"Sen bir 'What If' simülatörüsün. Kullanıcı şu eylemi yapmak istiyor: '{user_input}'. Bunun olası iyi sonuçlarını, kötü sonuçlarını ve risklerini detaylıca, eğlenceli bir dille anlat."
                
                response = model.generate_content(prompt)
                st.markdown(response.text)
                st.success("Simülasyon tamamlandı!")
                
            except Exception as e:
                st.error(f"Bir hata oluştu: {e}")
