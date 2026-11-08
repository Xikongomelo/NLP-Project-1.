
import streamlit as st
import joblib
import re
from nltk.stem import WordNetLemmatizer


# load the trained model and tf-idf vectorizer
model = joblib.load("svm_model.pkl")
tfidf = joblib.load("tfidf_vectorizer.pkl")

lemmatizer = WordNetLemmatizer()


# preprocess the new abstract
def clean_text(text):

    text = text.lower()
    text = re.sub(r'[^a-z\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text)

    words = text.split()
    words = [lemmatizer.lemmatize(word) for word in words]

    return " ".join(words).strip()


# page configuration
st.set_page_config(page_title="Researchly Research Abstract Classifier",page_icon="📄")


# title
st.title("Researchly Research Abstract Classifier")

st.write("This app classifies research abstracts as either "
    "AI-related or classical research.")


# abstract input
abstract = st.text_area("Enter research abstract:",height=200)

# classification
if st.button("Classify Abstract"):

    if abstract.strip():
        # preprocess the abstract
        cleaned_text = clean_text(abstract)

        # convert the abstract to tf-idf
        text_features = tfidf.transform([cleaned_text])

        # make the prediction
        prediction = model.predict(text_features)[0]

        # make the label lowercase
        prediction = str(prediction).lower()

        st.subheader("Prediction")

        if prediction == "ai":
            st.success("The abstract is classified as: artificial intelligence")

        else:
            st.success("The abstract is classified as: classical research")
    else:
        st.warning("Please enter a research abstract.")
