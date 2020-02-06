from django.shortcuts import render,redirect,HttpResponse
from app01 import models
from django import forms
# Create your views here.

class BookForm(forms.Form):
    title = forms.CharField(max_length=32)
    price = forms.DecimalField(max_digits=5,decimal_places=2)
    pub_date = forms.DateField()
    state = forms.ChoiceField(choices=((1,"已出版"),(2,"未出版")))
    # publish = forms.ChoiceField(choices=list(models.Publish.objects.all().values_list("pk","name")))
    publish = forms.ModelChoiceField(queryset=models.Publish.objects.all())
    authors = forms.ModelMultipleChoiceField(queryset=models.Author.objects.all())


class BookModelForm(forms.ModelForm):
    class Meta:
        model = models.Book
        # fields = ["title","price"]
        fields="__all__"

def books(request):
    queryset = models.Book.objects.all()
    return render(request,"books.html",locals())

def addbook(request):
    if request.method =="POST":
        '''
        data = request.POST.dict()
        data.pop("csrfmiddlewaretoken")
        data.pop("author_list")
        author_list = request.POST.getlist("author_list")
        book = models.Book.objects.create(**data)
        book.authors.add(*author_list)
        return redirect("/books/")
        '''
        form = BookModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/books/")
        else:
            return render(request,"addbook.html",locals())
    else:
        # form = BookForm()
        form = BookModelForm()
        publish_list = models.Publish.objects.all()
        author_list = models.Author.objects.all()
        return render(request,"addbook.html",locals())

def delbook(request,id):
    print(">>>>",id)
    models.Book.objects.filter(pk=id).delete()
    return redirect("/books/")


def editbook(request,id):
    edit_boot = models.Book.objects.filter(pk=id).first()
    if request.method=="POST":
        form = BookModelForm(request.POST,instance=edit_boot)
        if form.is_valid():
            form.save()
            return redirect("/books/")
        else:
            return render(request, "edit.html", locals())
    else:
        form = BookModelForm(instance=edit_boot)
        return render(request,"edit.html",locals())