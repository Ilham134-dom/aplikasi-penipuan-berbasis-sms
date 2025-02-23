import pickle
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer

#load save model
model_fraud = pickle.load(open('model_fraud.sav','rb'))

tfidf = TfidfVectorizer

loaded_vec = TfidfVectorizer(decode_error="replace", vocabulary=set(pickle.load(open("new_selected_feature_tf-idf.sav", "rb"))))

#judul halaman
st.title ('PREDIKSI PENIPUAN BERBASIS SMS')

clean_teks = st.text_input('Masukan Teks SMS')

fraud_detection = ''

if st.button('Hasil Deteksi'):
    predict_fraud = model_fraud.predict(loaded_vec.fit_transform([clean_teks]))

    if(predict_fraud == 0):
        fraud_detection = 'SMS NORMAL'
    elif(predict_fraud == 1):
        fraud_detection = 'SMS FRAUD'
    else:
        fraud_detection = 'SMS PROMO'

st.success(fraud_detection)
