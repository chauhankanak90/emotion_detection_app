# # import streamlit as st
# # import pickle
# # import string
# # import nltk
# # from nltk.corpus import stopwords

# # Download stopwords (first time only)
# nltk.download('stopwords')

# stop_words = set(stopwords.words('english'))

# Cleaning function
def clean_text(txt):
    txt = txt.lower()
    txt = txt.translate(str.maketrans('', '', string.punctuation))
    txt = ''.join([i for i in txt if not i.isdigit()])
    words = txt.split()
    words = [w for w in words if w not in stop_words]
    return " ".join(words)

# Load saved files
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# Emotion labels
emotion_map = {
    0: "Sadness",
    1: "Anger",
    2: "Love",
    3: "Surprise",
    4: "Fear",
    5: "Joy"
}

# UI
st.title("😊 Emotion Detection App")

user_input = st.text_area("Enter text:")

if st.button("Predict"):
    if user_input.strip() != "":
        
        # Clean input
        cleaned = clean_text(user_input)

        # Vectorize
        vec = vectorizer.transform([cleaned])

        # Predict
        pred = model.predict(vec)[0]

        st.success(f"Predicted Emotion: {emotion_map[pred]}")
    else:
        st.warning("Please enter some text!")
