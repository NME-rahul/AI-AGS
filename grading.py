import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tag import pos_tag
from collections import Counter

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import os

os.environ['NLTK_DATA'] =  f"c:/Users/{os.getenv('USERNAME')}/AppData/Roaming/nltk_data"


VARIABLES = {
    "vectorizer": None,
    "lammatizer": None,
    "feature_count_x": None,
    "vec1": None,
    "stop_words": None,
    "scale": 10,
}


def feature_count(paragraph):
  sentences = sent_tokenize(paragraph)

  total_words = 0
  total_nouns = 0
  total_adverbs = 0
  total_objects = 0

  for sentence in sentences:
      words = word_tokenize(sentence)
      tagged_words = pos_tag(words)

      num_words = len(words)
      total_words += num_words

      num_nouns = len([word for word, tag in tagged_words if tag.startswith('NN')])
      total_nouns += num_nouns

      num_adverbs = len([word for word, tag in tagged_words if tag.startswith('RB')])
      total_adverbs += num_adverbs

      num_objects = len([word for word, tag in tagged_words if tag.startswith('NN') or tag.startswith('PRP')])
      total_objects += num_objects
  num_sentences = len(sentences)
  return {
    "num_sentences": len(sentences),
    "avg_words_per_sentence": total_words / num_sentences,
    "avg_nouns_per_sentence": total_nouns / num_sentences,
    "avg_adverbs_per_sentence": total_adverbs / num_sentences,
    "avg_objects_per_sentence": total_objects / num_sentences,
  }

def Error(x, y):
  e = 0
  for key in x.keys():
    e += abs(x[key] - y[key])
  return e / len(x)

def download_dependencies():
  nltk.download('punkt')
  nltk.download('averaged_perceptron_tagger')
  nltk.download('stopwords')
  nltk.download('wordnet')

def prepare_true_answer(true_answers):
  true_answers_processed = [preprocess(answer) for answer in true_answers]
  vec1 = VARIABLES["vectorizer"].fit_transform(true_answers_processed)
  return vec1

def preprocess(text):
  tokens = word_tokenize(text.lower())
  tokens = [VARIABLES["lammatizer"].lemmatize(token) for token in tokens if token.isalnum() and token not in VARIABLES["stop_words"]]
  return ' '.join(tokens)

def grade(vec1, written_answers, scale):
    def cosine_similarity_nltk(vec1, vec2):
        return cosine_similarity(vec1, vec2)
    written_answers_processed = [preprocess(answer) for answer in written_answers]
    vec2 = VARIABLES["vectorizer"].transform(written_answers_processed)
    similarity_scores = cosine_similarity_nltk(vec1, vec2)
    scaled_scores = similarity_scores * scale
    return scaled_scores

def get_score(sentence1, sentence2): #text
  y = feature_count(sentence2)
  score = grade(VARIABLES["vec1"], [sentence2], VARIABLES["scale"])
  return score - (Error(VARIABLES["feature_count_x"], y) / VARIABLES["scale"])


def init(true_answers): #text
  try:
    VARIABLES["vectorizer"], VARIABLES['lammatizer'], VARIABLES["stop_words"] = TfidfVectorizer(), WordNetLemmatizer(), set(stopwords.words('english'))
    VARIABLES["feature_count_x"] = feature_count(true_answers)
    VARIABLES["vec1"] = prepare_true_answer([true_answers])
    return True
  except:
    return False