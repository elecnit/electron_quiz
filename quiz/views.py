from typing import Final
from django.shortcuts import render
from .models import Questions, Stages

from random import choice
# Create your views here.
#def CategoryView(request,cats):
 #   cats1 = Category.objects.get(name=cats.replace('-',' '))
  #  print(cats1)
 #@   category_post = Post.objects.filter(category=cats1.id)
 #   return render(request, 'categories.html',{"cats":cats.title().replace('-',' '),"category_post":category_post})


count = 0
score = 0
def HomeView(request):
    global score
    score = 00
    return render(request,'home.html')

def Stage1View(request):
    stage_sel =Stages.objects.get(stages="stage_1")
    
    questions = Questions.objects.filter(stage_id=stage_sel.id)  
    sel_ids = []
    for i in questions:
        sel_ids.append(i.id)
    sel_id =  choice(sel_ids)
    question = Questions.objects.filter(id=sel_id)  
    return render(request,'stage1.html',{"question":question,"score":score})



def Stage1Correcter(request,answer,correct_answer):
    global count
    global score
    count+=1
    if answer == correct_answer:
         score+=20
    else:
        score-=10
    if count<3:
        return Stage1View(request)  
    else:
        count=0
        return Stage2View(request)   
     

def Stage2View(request):
    global score
    stage_sel =Stages.objects.get(stages="stage_2")
    questions = Questions.objects.filter(stage_id=stage_sel.id)  
    sel_ids = []
    for i in questions:
        sel_ids.append(i.id)
    sel_id =  choice(sel_ids)
    question = Questions.objects.filter(id=sel_id) 
    return render(request,'stage2.html',{'question':question,'score':score})


def Stage2Correcter(request,answer,correct_answer):
    global score
    
    if answer == correct_answer:
         score+=30
    else:
        score-=15
    return Stage3View(request)    



def Stage3View(request):
    global score
    if score>60:
        sel_id = 12
        question = Questions.objects.filter(id=sel_id)  
        return render(request,'stage3_type3.html',{'question':question,'score':score})  
    elif score>30:    
         sel_id = 11
         question = Questions.objects.filter(id=sel_id)  
         return render(request,'stage3_type2.html',{'question':question,'score':score})  
    else:
        sel_id=10  
        question = Questions.objects.filter(id=sel_id)  
        return render(request,'stage3_type1.html',{'question':question,'score':score})     

      


def Stage3Correcter(request,answer,correct_answer):
    global score
    if answer == correct_answer:
         score+=50
    else:
        score-=30

    return FinalPage(request)    

def FinalPage(request):
    global score
    if score>75:
        return render(request,"finalpage.html",{'score':score}) 
    elif score>50:
        return render(request,"finalpage2.html",{'score':score}) 
    else:    
         return render(request,"finalpage3.html",{'score':score}) 
score = 00       