from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,"text/index.html")
 
def analyze(request):

    djtext = request.POST.get('text','default')

    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    charcount = request.POST.get('charcount','off')
    if (removepunc == "on"):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed= ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        context = {'purpose' : "Remove puncuations",'analyzed_text':analyzed}
        djtext = analyzed

    if(fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        context = {'purpose' : "Changed to upperCase",'analyzed_text':analyzed}
        djtext = analyzed
        
    if(newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char !="\r":
                analyzed = analyzed + char
        context = {'purpose' : "Removed NewLines",'analyzed_text':analyzed}
        djtext = analyzed

    if(extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char
                
        context = {'purpose' : "Removed NewLines",'analyzed_text':analyzed}
        djtext = analyzed

    if(removepunc !="on" and newlineremover !="on" and fullcaps !="on" and extraspaceremover !="on"):
        return HttpResponse("Please select any operation and try again")
    
    return render(request,"text/analyze.html",context)