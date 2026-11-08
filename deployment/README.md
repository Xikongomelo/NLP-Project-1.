# Deployment Guide

## About  Application

Researchly is a web application developed using Streamlit. It allows users to enter a research abstract and classify it as either AI-related research or classical research.

The application uses a trained SVM model and a TF-IDF vectorizer to make predictions.

## Files Required

Make sure the following files are in the deployment folder:

- `app.py`
- `svm_model.pkl`
- `tfidf_vectorizer.pkl`
- `requirements.txt`

## How to Run the Application

**Step 1: Download the project**

Clone the repository from GitHub:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Open the downloaded project and navigate to the deployment folder.

**Step 2: Install the required packages**

Open a terminal in the deployment folder and run:

```bash
pip install -r requirements.txt
```

**Step 3: Download the NLTK WordNet data**

The application uses WordNet for lemmatisation. Download the required resource by running:

```bash
python -m nltk.downloader wordnet
```

**Step 4: Start the application**

Run the following command:

```bash
streamlit run app.py
```

**Step 5: Open the application**

Streamlit will provide a local URL in the terminal. Open this URL in a browser to use the application.

## Using Researchly

1. Enter a research abstract in the text box.
2. Click the **Classify Abstract** button.
3. The application will display whether the abstract is classified as AI-related or classical research.
