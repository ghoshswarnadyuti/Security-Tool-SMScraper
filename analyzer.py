import nltk

# You'll likely need to download NLTK resources
# nltk.download('punkt')
# nltk.download('stopwords')

def analyze_text(text):
    """Performs basic text analysis."""
    words = nltk.word_tokenize(text)
    stop_words = nltk.corpus.stopwords.words('english')
    filtered_words = [w for w in words if w.lower() not in stop_words and w.isalpha()] 

    # More advanced analysis could involve sentiment analysis, topic modeling, etc.  
    return filtered_words