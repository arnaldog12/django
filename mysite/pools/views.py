from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from django.http import Http404
from django.shortcuts import get_object_or_404, render

from .models import Question

def index(request):
    # isso torna o import de loader e HttpResponse desnecessário
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'pools/index.html', context)

    # template = loader.get_template('pools/index.html')
    # return HttpResponse(template.render(context, request))

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'pools/details.html', {'question':question})

def results(request, question_id):
    return HttpResponse("You're looking at the results of question {}".format(question_id))

def vote(request, question_id):
    return HttpResponse("You're voting on question {}".format(question_id))