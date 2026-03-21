import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download required NLTK data
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)

def preprocess_text(text: str) -> str:
    """
    Preprocess text by:
    1. Converting to lowercase
    2. Removing special characters
    3. Tokenizing using NLTK
    4. Removing English stopwords
    5. Returning cleaned text as a single string
    """
    # 1. Convert to lowercase
    text = text.lower()

    # 2. Remove special characters (keep only letters, numbers, and spaces)
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)

    # 3. Tokenize using NLTK
    tokens = word_tokenize(text)

    # 4. Remove English stopwords
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [token for token in tokens if token not in stop_words]

    # 5. Join tokens back into a single string
    cleaned_text = ' '.join(filtered_tokens)

    return cleaned_text