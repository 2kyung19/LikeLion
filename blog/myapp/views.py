from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Blog
from .models import Guest
from .models import Gallery

def home(request):
    return render(request, 'home.html')

########## wordcount ##########
def wordcount(request):
    return render(request, 'wordcount.html')

def wordcountAbout(request):
    return render(request, 'wordcount_about.html')

########## service_info #########
def service(request):
    return render(request, 'service_info.html')

def wordcountResult(request):
    text = request.GET['fulltext']
    words = text.split()

    word_dictionary = {}

    for word in words:
        if word in word_dictionary: #increase
            word_dictionary[word]+=1
        else:
            word_dictionary[word]=1 #add to dictionary

    return render(request, 'wordcount_result.html', {'full':text, 'total':len(words),'dictionary': word_dictionary.items()})

########## queryset ##########
def queryset(request):
    blogs = Blog.objects #queryset

    return render(request, 'blog.html', {'blogs':blogs})

########## blog #############
def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)

    return render(request, 'blog_detail.html', {'blog':blog_detail})

def guest(request):
    guests = Guest.objects

    return render(request, 'guest.html', {'guests': guests})

def guestWrite(request):
    return render(request, 'guest_create.html')

def guestResult(request, guest_id):
    guest_result = get_object_or_404(Guest, pk=guest_id)

    return render(request, 'guest_result.html', {'guest':guest_result})

def guestCreate(request): #입력받은 내용을 DB에 저장하는 함수
    guest = Guest()
    guest.title = request.GET['title']
    guest.name = request.GET['name']
    guest.body = request.GET['body']
    guest.pub_date = timezone.datetime.now()
    guest.save()
    return redirect('/guest/result/'+str(guest.id))

#return redirect('https://www.google.com') 을 쓰면 저장을 누르자마자 구글 사이트로 이동함

def gallery(request):
    gallery = Gallery.objects
    return render(request, 'gallery.html', {'gallery':gallery})