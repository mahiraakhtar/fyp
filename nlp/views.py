from django.views.generic.edit import CreateView, UpdateView
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
from django.views import generic
from django.shortcuts import render
from django.shortcuts import redirect
from .forms import TextForm

class IndexView(generic.ListView):
	model=umls
	template_name = 'nlp/diseaseindex.html'
	context_object_name='object_list'
	def get_queryset(self):
		return umls.objects.all()

def home(request):
	return render( request, 'nlp/home.html')

class DetailView(generic.DetailView):
	model=umls
	template_name='nlp/diseasedetail.html'
# Create your views here.
 


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

def get_text(request):
	form=TextForm()
	return render(request, 'nlp/text_input.html',{'form':form})




def info_ext(request):
# 	words=(word_tokenize(text))
	# 

	# for w in filtered_text:
	# 	stemmed.append()

	# lemmatized=[]
	form=TextForm(request.POST)
	if form.is_valid():
		text=form.cleaned_data['text']
		

	# args={'form':form, 'text':text}
	# return render(request, 'nlp/text_input.html',{'form':form})
	
	sentence_re = r'(?:(?:[A-Z])(?:.[A-Z])+.?)|(?:\w+(?:-\w+)*)|(?:\$?\d+(?:.\d+)?%?)|(?:...|)(?:[][.,;"\'?():-_`])'

	grammar = r"""
	NBAR:
		{<NN.*|JJ>*<NN.*>}  # Nouns and Adjectives, terminated with Nouns
        
	NP:
		{<NBAR>}
		{<NBAR><IN><NBAR>}  # Above, connected with in/of/etc...
	"""

	toks = nltk.regexp_tokenize(text, sentence_re)
	filtered_toks=[w for w in toks if not w in stop_words]
	tagged = nltk.tag.pos_tag(filtered_toks)

		
	# chunkgram=r"""Chunk: {<JJ>+<JJ.>*<NN.>+<NN>?} """
	chunkParser=nltk.RegexpParser(grammar)
	chunkedtree=chunkParser.parse(tagged)

	terms = get_terms(chunkedtree)

	# for term in terms:
	# 	for word in term:
	# 		print (word),
	# 	print

	context ={
		'terms':terms,
	}

	return render(request,'nlp/text_ext.html',context)
	

def leaves(tree):
	# """Finds NP (nounphrase) leaf nodes of a chunk tree."""
    for subtree in tree.subtrees(filter = lambda t: t.label()=='NP'):
    	yield subtree.leaves()

def normalise(word):
#     """Normalises words to lowercase and stems and lemmatizes it."""
	word = word.lower()
    # word = stemmer.stem_word(word) #if we consider stemmer then results comes with stemmed word, but in this case word will not match with comment
		# ps.stem(word)
	# word = lemmatizer.lemmatize(word)
	return word

def acceptable_word(word):
	w=' '.join(word)
	dis=umls.objects.filter(Diseasename__icontains=w)
	ws='not found'
	if dis.exists():
		return dis
	
	else: 
		return ws



def get_terms(tree):
	for leaf in leaves(tree):
		term = [ normalise(w) for w,t in leaf ]
		term= acceptable_word(term)
		yield term



