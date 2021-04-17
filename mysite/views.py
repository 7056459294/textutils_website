from django.http import HttpResponse

from django.shortcuts import render



#pipeline
def home(request):
 return render(request, 'index.html')
   # return HttpResponse("home") 
   


def analyzer(request):
    #get text
    text=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    uppercase=request.POST.get('uppercase','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    charactercounter=request.POST.get('charactercounter','off')
    #analyze text
    
    if removepunc=='on':
        puncl='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed=""
        for char in text:
            if char not in puncl:
                analyzed=analyzed+char
            
        para={'analyzed_text':analyzed}
        #return render(request,'removepunc.html',para)
        text=analyzed
    if uppercase=='on':
        analyzed=""
        for char in text:
            analyzed=analyzed+char.upper()
        para={'analyzed_text':analyzed}
        #return render(request,'removepunc.html',para)
        text=analyzed
    if extraspaceremover=='on':
        analyzed=""
        for index,char in enumerate(text):
            if text[index]==" " and  text[index+1]==" ":
                pass
            else:
                analyzed=analyzed+char
        para={'analyzed_text':analyzed}
        #return render(request,'removepunc.html',para)
        text=analyzed
    if charactercounter=='on':
        analyzed=0
        for i in text:
            analyzed=analyzed+1
        para={'analyzed_text':analyzed}
        #return render(request,'removepunc.html',para)
        text=analyzed
    
    if (charactercounter != 'on' and extraspaceremover != 'on' and uppercase != 'on' and removepunc !='on'):
        return HttpResponse("please select any choice")
    return render(request,'removepunc.html',para)



        