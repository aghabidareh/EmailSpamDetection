from django.shortcuts import render

from detector.modules.predictor import predictor


def index(request):
    if request.method == "POST":
        text = request.POST.get("text")
        result = predictor(text)
        context = {'result': result}
        return render(request, 'index.html', context)
    return render(request, 'index.html')
