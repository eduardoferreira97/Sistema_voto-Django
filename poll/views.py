from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from .models import Question

# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = { 'latest_question_list': latest_question_list,}
    return render(request, 'poll/index.html',context)

def detail(request, question_id):
    
    question = get_object_or_404(Question,pk=question_id)

    return render(request, 'poll/detail.html',{'question': question})

def results(request, question_id):
    responde = "You're loking at the results of questions %s"

def vote(request, question_id):
    return HttpRequest("You're voting on question %s." % question_id)