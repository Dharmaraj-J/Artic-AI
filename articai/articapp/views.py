from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .forms import SignupForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


import sumy
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer



from textblob import TextBlob


@login_required(login_url='login')
def summarize(request):
    if request.method == 'POST':
            #title
            text = request.POST.get('text')
            blob = TextBlob(text)
            noun_phrases = blob.noun_phrases
            title = " ".join(noun_phrases[:2]).capitalize()
             
            #summarize 
            parser = PlaintextParser.from_string(text, Tokenizer('english'))
            summarizer = LexRankSummarizer()
            summary = summarizer(parser.document, sentences_count=3)
            summary = ''.join(str(sentence) for sentence in summary)


            return render(request, 'summarize.html', {'summary': summary,'title': title})
     
    else:
        return render(request, 'summarize.html')




def registeruser(request):

    if request.method == 'POST':
       form = SignupForm(request.POST)
       if form.is_valid():
                user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
    
                login(request, user)
                return redirect('login')

    return render(request,'register.html')

    


@login_required(login_url='login')
def index(request):
     return render(request,"index.html")




def loginuser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user = authenticate(request,username=username,password = password)
        if user is not None:
                login(request,user)
                return redirect('/')

    return render(request,"loginpage.html")



   

    
    