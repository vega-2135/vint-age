from django.shortcuts import render

from .models import Question


def faq(request):
    questions = Question.objects.all()
    return render(request, "faq/faq.html", {"questions": questions})
