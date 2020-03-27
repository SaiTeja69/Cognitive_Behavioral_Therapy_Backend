from django.http import Http404
from django.shortcuts import render
from .models import Question, Choice 


def survey(request):
	all_questions = Question.objects.all()
	return render(request, 'questionaire/index.html',  {'all_questions': all_questions})

	
def detail(request, question_id):
	try: 
		question = Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		raise Http404("Details to the choice does not exist")
	return render(request, 'questionaire/detail.html',  {'question': question})