# Import necessary libraries and models
import streamlit as st
import spacy
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob
import language_tool_python
from gensim.models import Word2Vec


nltk.download('vader_lexicon')
# Load NLP models
nlp = spacy.load("en_core_web_sm")
tool = language_tool_python.LanguageTool('en-US')
sia = SentimentIntensityAnalyzer()

# Streamlit UI
st.title("Automated Essay Analysis and Feedback")

# Input text area
st.subheader("Enter the Student Essay or Assignment:")
input_text = st.text_area("Paste the text here:")

# Function to analyze and provide feedback
def analyze_essay(essay):
    # Tokenize the essay using spaCy
    doc = nlp(essay)

    # Calculate the number of words and sentences
    num_words = len(doc)
    num_sentences = len(list(doc.sents))

    # Check grammar using LanguageTool
    grammar_errors = len(tool.check(essay))

    # Calculate sentiment using NLTK's VADER
    sentiment = sia.polarity_scores(essay)

    # Calculate the average word length
    avg_word_length = sum(len(token.text) for token in doc) / num_words if num_words > 0 else 0

    return num_words, num_sentences, grammar_errors, sentiment, avg_word_length

if input_text:
    # Analyze the essay
    num_words, num_sentences, grammar_errors, sentiment, avg_word_length = analyze_essay(input_text)

    st.subheader("Analysis Results:")
    st.write(f"Number of Words: {num_words}")
    st.write(f"Number of Sentences: {num_sentences}")
    st.write(f"Grammar Errors: {grammar_errors}")
    st.write(f"Sentiment Analysis: {sentiment['compound']:.2f} (Negative: {sentiment['neg']:.2f}, Neutral: {sentiment['neu']:.2f}, Positive: {sentiment['pos']:.2f})")
    st.write(f"Average Word Length: {avg_word_length:.2f}")

    # Provide feedback based on analysis
    st.subheader("Feedback:")
    if grammar_errors > 0:
        st.warning("Grammar issues detected. Consider proofreading your essay.")
    if sentiment['compound'] < -0.2:
        st.warning("The sentiment of your essay appears to be negative.")
    elif sentiment['compound'] > 0.2:
        st.success("The sentiment of your essay appears to be positive.")
    else:
        st.info("The sentiment of your essay is neutral.")

    if avg_word_length > 6:
        st.warning("Consider using shorter words for better readability.")

# Instructions
st.markdown("### Instructions:")
st.write("1. Paste the student's essay or assignment in the text area above.")
st.write("2. Click the 'Analyze' button to get feedback on the essay's word count, sentence count, grammar errors, sentiment, and average word length.")
st.write("3. Review the feedback provided to improve the essay.")
