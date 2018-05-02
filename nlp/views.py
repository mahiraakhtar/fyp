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

