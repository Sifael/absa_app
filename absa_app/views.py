from typing import Any
from django.http.request import HttpRequest as HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from absa_app.forms import TextForSentiment


# Importing PreProcessors
from .preprocessors import preprocess, load_pickled_file
import os

count_vectorizer = load_pickled_file('./absa_app/yelp_count_vectorizer.pk')
tfidf_vectorizer = load_pickled_file('./absa_app/yelp_tfidf_vectorizer.pk')

naive_bayes_model = load_pickled_file('./absa_app/naive_bayes_tfidf.pk')

# Create your views here.
base = 'absa_app'


class HomeView(TemplateView):
	template_name = f"{base}/home.html"

	def get(self, request) -> HttpResponse:
		textform = TextForSentiment()
		return render(request, self.template_name, context={'textform': textform})
	
	def post(self, request):
		textform = TextForSentiment(request.POST)
		if textform.is_valid():
			text = textform.cleaned_data['text']
			textform = TextForSentiment()

			args = { 'textform': textform,
		             'value': ' '.join(['Your Text:' , text]),
					 'preprocess': ' '.join(['Step 1 Preprocess:', preprocess(text)]),
					 'count_vectorizer':  ' '.join(['Vectorizer:', str( tfidf_vectorizer.transform([text]).toarray() ) ] ),
					 'model_prediction':  ' '.join(['Model Rating Prediction:', str(naive_bayes_model.predict(  tfidf_vectorizer.transform([text]).toarray())[0]) ] ),
					 'model_prediction_probability':  ' '.join(['Model Rating Prediction:', 
												          str(100 * (naive_bayes_model.predict_proba( tfidf_vectorizer.transform([text]).toarray())))  ] )   }


			return render(request, self.template_name, args)

		else:
			return redirect('absa_app:home')



class TechnicalNotes(TemplateView):
	template_name = f"{base}/technical-notes.html"