import pandas as pd
import os
from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from wordcloud import WordCloud
from nltk.stem.lancaster import LancasterStemmer


BASEDIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(BASEDIR)

def create_wc(word_list):
	wordcloud = WordCloud().generate(' '.join(word_list))
	image = wordcloud.to_image()
	image.show()

def word_process(raw_list):
	tokenizer = RegexpTokenizer(r'\w+')
	raw = ''.join(raw_list).lower()
	tokens = tokenizer.tokenize(raw)
	en_stop = get_stop_words('en')
	stopped_tokens = [i for i in tokens if not i in en_stop]
	create_wc(stopped_tokens)
	st = LancasterStemmer()
	stemmed_tokens = [st.stem(i) for i in stopped_tokens]
	create_wc(stemmed_tokens)
	return stemmed_tokens



if __name__ == '__main__':
	word_process(data)