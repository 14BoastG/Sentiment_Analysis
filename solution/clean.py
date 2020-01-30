def Cleaner(text):

  # import/download relevant packages
  import string
  import nltk
  nltk.download('punkt')
  nltk.download('stopwords')

  # split into words
  from nltk.tokenize import word_tokenize
  tokens = word_tokenize(text)

  # convert to lower case
  tokens = [w.lower() for w in tokens]

  # remove punctuation from each word
  table = str.maketrans('', '', string.punctuation)
  stripped = [w.translate(table) for w in tokens]

  # remove remaining tokens that are not alphabetic
  words = [word for word in stripped if word.isalpha()]

  # filter out stop words
  from nltk.corpus import stopwords
  stop_words = set(stopwords.words('english'))
  words = [w for w in words if not w in stop_words]

  # stemming of words
  from porter2stemmer import Porter2Stemmer
  stemmer = Porter2Stemmer()
  stemmed = [stemmer.stem(word) for word in words]

  # final output
  global clean_text
  clean_text = stemmed
  return clean_text