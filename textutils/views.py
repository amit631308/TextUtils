from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    # get the text
    hello = request.POST.get('text','default')
    # check the checkbox values
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    remnewln = request.POST.get('remnewln','off')
    removeextraline = request.POST.get('removeextraline','off')
    charcount = request.POST.get('charcount','off')

    # condition on the basis of checkboxes status
    if removepunc == "on":
        analyzed = ""
        punctuation = '''!"#$%&'()*+,-./:;<=>?@[\]^`{|}~'''
        for char in hello:
            if char not in punctuation:
                analyzed = analyzed + char
        params = { 'purpose':'Remove punchuation', 'result':analyzed}
        hello = analyzed

    if fullcaps == "on":
        analyzed = ""
        for char in hello:
            analyzed = analyzed + char.upper()
        params = {'purpose':'full capitalized','result':analyzed}
        hello = analyzed

    if remnewln == "on":
        analyzed = ""
        for char in hello:
            if char !="\n" and char !="\r":
                analyzed = analyzed + char
        params = {'purpose':'Remove new line','result':analyzed}
        hello = analyzed

    if removeextraline == "on":
        analyzed = ""
        for index, char in enumerate(hello):
            if not(hello[index] == ' ' and hello[index+1] == ' '):
                analyzed = analyzed + char
        params = {'purpose':'Extra space remover','result':analyzed}
        hello = analyzed

    if charcount == "on":
        analyzed = 0
        for char in hello:
            if char != " ":
                analyzed = analyzed + 1
        params = {'purpose':'count character','result':analyzed}
    # condtion if not any of the check box enables
    if (removepunc!="on" and fullcaps!="on" and remnewln!="on" and removeextraline!="on" and charcount!="on"):
        return HttpResponse("please enable one of the action")

    return render(request,'analyzed.html',params)

