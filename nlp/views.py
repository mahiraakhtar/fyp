from django.shortcuts import render
from django.http import HttpResponse
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize, PunktSentenceTokenizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import os
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
from nltk.classify.scikitlearn import  SklearnClassifier
import string
from string import punctuation
from .models import umls
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize
# Create your views here.
 
def index(request):
	return HttpResponse("<h1>NLP ")

def insertdatabase(self):
	os.chdir('C:/Users/MAHIRA/Desktop/fyp')
	file = open('diabetes.txt', 'r') 
	mesh=open('diseases mesh.txt', 'r')
	line = mesh.readline()
	meshdiseases=[]
	meshcodes=[]
	oneworddis=[]
	# f= open("disonly.txt","w+")
    
	while line:
		line = mesh.readline()
		splitline=line.split(";")
		# f.write(splitline[0]+"\n")
		meshdiseases.append(splitline[0])
		dis=splitline[0]

		singlewords=splitline[0].split(" ")
		y=0
		for y in range(len(singlewords)):
			oneworddis.append(singlewords[y])                              
			y+=1 
		c=""
		if len(splitline)>1:
			meshcodes.append(splitline[1])
			c=splitline[1]
		createumls(dis,c)
	return HttpResponse("<h1>Diseasenames and Codes inserted into Database!")		
		

def createumls(dis,c):
	d=umls(Diseasename=dis, Code=c)
	d.save()


stop_words= set(stopwords.words("english"))
ps=PorterStemmer()
lemmatizer =WordNetLemmatizer()
sentence_re = r'(?:(?:[A-Z])(?:.[A-Z])+.?)|(?:\w+(?:-\w+)*)|(?:\$?\d+(?:.\d+)?%?)|(?:...|)(?:[][.,;"\'?():-_`])'

def info_ext(text):
# 	words=(word_tokenize(text))
	# 

	# for w in filtered_text:
	# 	stemmed.append()

	# lemmatized=[]

	grammar = r"""
	NBAR:
		{<NN.*|JJ>*<NN.*>}  # Nouns and Adjectives, terminated with Nouns
        
	NP:
		{<NBAR>}
		{<NBAR><IN><NBAR>}  # Above, connected with in/of/etc...
	"""

	toks = nltk.regexp_tokenize(text, sentence_re)
	filtered_toks=[w for w in tagged if not w in stop_words]
	tagged = nltk.tag.pos_tag(filtered_toks)

		
	# chunkgram=r"""Chunk: {<JJ>+<JJ.>*<NN.>+<NN>?} """
	chunkParser=nltk.RegexpParser(grammar)
	chunkedtree=chunkParser.parse(tagged)

	terms = get_terms(chunkedtree)

	for term in terms:
		for word in term:
			print (word),
		print

	
def leaves(tree):
	# """Finds NP (nounphrase) leaf nodes of a chunk tree."""
    for subtree in tree.subtrees(filter = lambda t: t.label()=='NP'):
    	yield subtree.leaves()

def normalise(word):
#     """Normalises words to lowercase and stems and lemmatizes it."""
	word = word.lower()
    # word = stemmer.stem_word(word) #if we consider stemmer then results comes with stemmed word, but in this case word will not match with comment
		# ps.stem(word)
	word = lemmatizer.lemmatize(word)
	return word

def acceptable_word(word):
    # """Checks conditions for acceptable word: length
	accepted = bool(2 <= len(word) <= 40 and word.lower() )
	return accepted


def get_terms(tree):
	for leaf in leaves(tree):
		term = [ normalise(w) for w,t in leaf ]
		# if acceptable_word(w) ]
		yield term



