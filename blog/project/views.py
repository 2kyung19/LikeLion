from django.shortcuts import render

from .models import Text

# Create your views here.
def p_main(request):
    return render(request, 'p_main.html')

def unicode(request):
    text = Text()
    text.text = request.GET['text']

    conv = str(text.text)

    uni = ""

    for c in conv:
        uni += ("%u"+str(hex(ord(c)))[2:])

    return render(request, 'unicode.html', {'text':text, 'conv':uni})