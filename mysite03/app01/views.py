from django.shortcuts import render,HttpResponse,redirect

# Create your views here.

import datetime
def index(request):
    # return HttpResponse('<h1>index</h1>')
    good_list=['小米冰箱','海尔冰箱','美的冰箱']
    list_info = {"name":"alex","age":20,"hooby":"pingpang"}
    class Animo:
        def __init__(self,name,age):
            self.name = name
            self.age = age
        def ps(self):
            return 666
    alex = Animo('alex',25)
    egon = Animo('egon',20)
    list_person = [alex,egon]
    now = datetime.datetime.now()
    book_list = []
    size=31235544
    shi='十月之交，朔月辛卯。日有食之，亦孔之丑。彼月而微，此日而微；今此下民，亦孔之哀。日月告凶，不用其行。四国无政，不用其良。彼月而食，则维其常；此日而食，于何不臧。'
    num_a = 5
    #return render(request,'index.html',{"num_a":num_a,"shi":shi,"good_list":good_list,"list_info":list_info,"list_person":list_person,"now":now,"book_list":book_list,"size":size})
    return render(request,'index.html',locals())


def timer(reqyest):
    s = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return HttpResponse(s)

def login(request):
    # return render(request,'login.html')
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        if user == 'alex' and pwd == '123':
            return redirect('/app01/index/')
        else:
            return render(request, 'login.html')

def articles(request,y):
    return HttpResponse('articles_{}'.format(y))