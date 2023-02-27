from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout


import sumy
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer





def summarize(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        parser = PlaintextParser.from_string(text, Tokenizer('english'))
        summarizer = LexRankSummarizer()
        summary = summarizer(parser.document, sentences_count=3)
        summary = ''.join(str(sentence) for sentence in summary)
        return render(request, 'summarize.html', {'summary': summary})
    else:
        return render(request, 'summarize.html')



def index(request):
     return render(request,'index.html')




def loginuser(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user = authenticate(request,username=username,password = password)
        if user is not None:
                login(request,user)
                return redirect('/')

    return render(request,"loginpage.html",{'page':page})


