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
        uni += (str(ord(c)) + " ")
        print(c + str(ord(c)))

    print(uni)

    return render(request, 'unicode.html', {'text':text, 'conv':uni})