This project is a web application built with Streamlit that provides automated analysis and feedback for essays or assignments. It leverages various Natural Language Processing (NLP) tools to evaluate text based on several criteria, including grammar, sentiment, and readability.

Key Components:
NLP Models: Utilizes spaCy for text processing, nltk's VADER for sentiment analysis, TextBlob for additional text analysis, language_tool_python for grammar checking, and Word2Vec for potential word embedding analysis.
Streamlit UI: Provides an interactive interface for users to input text and receive feedback.

Features:
Word and Sentence Count: Calculates the total number of words and sentences in the essay.
Grammar Checking: Detects and counts grammar errors using LanguageTool.
Sentiment Analysis: Analyzes the sentiment of the essay and provides a sentiment score.
Readability: Calculates the average word length to gauge text readability.
Feedback: Offers suggestions based on analysis results, such as grammar improvements and readability tips.
