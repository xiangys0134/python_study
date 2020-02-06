from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
from app01 import models

def add(request):

    ################################## 绑定一对多关系 ##############################
    # 方式1:
    #book=models.Book.objects.create(title="linux",price=122,pub_date="2012-12-12",publish_id=1)

    # 方式2:
    # pub_obj=models.Publish.objects.filter(name="橘子出版社").first()
    # book=models.Book.objects.create(title="php",price=122,pub_date="2012-12-12",publish=pub_obj)
    # print(book.title)
    # print(book.publish_id)
    # print(book.publish) # book书籍出版社对象
    # 查询go出版社的邮箱
    # models.Publish.objects.filter(id= book.publish_id).first().email
    # book.publish.email

    ########################## 绑定多对多的关系;无非是在关系表创建记录 ##########

    # linux这本书绑定两个作者:alex,egon
    # linux=models.Book.objects.filter(title="linux").first()
    # alex=models.Author.objects.filter(name="alex").first()
    # egon=models.Author.objects.filter(name="egon").first()
    # print(linux.price)
    # print(linux.publish)
    #linux.authors.add(alex,egon)
    #linux.authors.add(1)
    #linux.authors.add(*[1,2])
    #linux.authors.remove(alex,egon)
    #linux.authors.clear()
    #linux.authors.set([1,])

    '''
    #KEY:关联属性:authors
    class Book(models.Model):
            title = models.CharField( max_length=32)
            pub_date=models.DateField()
            price=models.DecimalField(max_digits=5,decimal_places=2)
            publish=models.ForeignKey(to="Publish",to_field="id",on_delete=models.CASCADE,null=True)
            authors=models.ManyToManyField("Author",db_table="book2authors") # 创建关系表
            def __str__(self):
                return self.title

 
    '''

    ###############
    # 正向操作按字段,反向操作按表名小写

    linux = models.Book.objects.filter(title="linux").first()
    go = models.Book.objects.filter(title="go").first()
    alex = models.Author.objects.filter(name="alex").first()
    # 给alex作者绑定两本书籍: linux,go
    alex.book_set.add(linux,go)

    return HttpResponse("添加成功!")

def query(request):
    '''
    一 基于对象的跨表查询( 子查询:以上一次的查询结果作为下一次的查询条件)
       (1)一对多
                         正向查询:按字段 book.publish
         Book对象    ---------------------------------- >  Publish 对象
                      <---------------------------------
                        反向查询:按表名小写_set.all()


        (2)多对多
                       正向查询:按字段 book.authors.all()
         Book对象    ---------------------------------- >  Author 对象
                      <---------------------------------
                        反向查询:按表名小写_set.all()


        (2)一对一
                        正向查询:按字段 book.ad
         Author 对象   ---------------------------------- >  AuthorDetail 对象
                      <---------------------------------
                        反向查询:按表名小写

    二 基于双下划綫的跨表查询:

       KEY:通知ORM引擎如何跨表: 正向查询按字段,反向查询按表名小写

    :param request:
    :return:
    '''
    #################################一基于对象的跨表查询#######################
    #(1)一对多

    # 1 查询linux这本书籍的出版社的地址
    # book=models.Book.objects.filter(title="linux").first()
    # print(book.publish.city)
    # 2 查询苹果出版社出版的所有书籍
    # publish=models.Publish.objects.filter(name="苹果出版社").first()
    # queryset=publish.book_set.all()
    # print(queryset) # <QuerySet [<Book: linux>, <Book: python>]>


    # (2)多对多

    # 1 查询linux书籍的所有作者
    # linux=models.Book.objects.filter(title="linux").first()
    # queryset=linux.authors.all() # <QuerySet [<Author: alex>]>
    # print(queryset)
    # 2 查询alex作者出版过得所有书籍
    # alex=models.Author.objects.filter(name="alex").first()
    # queryset=alex.book_set.all()
    # print(queryset) # <QuerySet [<Book: linux>, <Book: go>]>

   # (3)一对一
    # 1  查询alex的手机号
    # alex = models.Author.objects.filter(name="alex").first()
    # print(alex.ad.telephone)

    # 2 查询手机号为911的作者的名字
    # ad=models.AuthorDetail.objects.filter(telephone=911).first()
    # print(ad.author.name)
    ######################基于双下划线的跨表查询(join查询)#################################
    # 1 查询linux这本书籍的出版社的地址
    '''
    SELECT app01_publish.city from app01_book INNER JOIN app01_publish 
                                  ON app01_book.publish_id = app01_publish.id 
                                  WHERE app01_book.title ="linux"
    
    '''
    # 方式1
    # queryset=models .Book.objects.filter(title="linux").values("price","publish__city")
    # print(queryset)
    # # 方式2
    # queryset=models.Publish.objects.filter(book__title="linux").values("city")
    # print(queryset)

    # 2 查询linux书籍的所有作者
    #queryset=models.Book.objects.filter(title="linux").values("authors__name")
    #queryset=models.Book.objects.filter(title__startswith="l").values("authors__name") # ********
    #print(queryset) # <QuerySet [{'authors__name': 'alex'}, {'authors__name': 'alex'}, {'authors__name': 'egon'}]>

    # queryset=models.Author.objects.filter(book__title="linux").values("name")

    # 3  查询alex的手机号

    # queryset=models.Author.objects.filter(name="alex").values("ad__telephone")
    # queryset=models.AuthorDetail.objects.filter(author__name="alex").values("telephone")
    # print(queryset) # <QuerySet [{'telephone': 110}]>

    # 连续跨表
    # 4 查询人民出版社出版过的所有书籍的名字以及作者的姓名
    # queryset=models.Book.objects.filter(publish__name="人民出版社").values("title","authors__name")
    # models.Author.objects.filter(book__publish__name="人民出版社").values("book__title","name")
    # 5 手机号以151开头的作者出版过的所有书籍名称以及出版社名称
    # queryset=models.Book.objects.filter(authors__ad__telephone__contains="1").values("title","publish__name")
    # print(queryset)
    ####################################### 分组查询 #####################################

    ############### 单表分组查询

    #queryset=models.Emp.objects.all() # select * from emp
    # queryset=models.Emp.objects.values("name") # select name from emp;
    # print(queryset)

    '''
    单表分组查询:
    #查询每一个部门名称以及对应的员工数
    
    sql:
        select dep,Count(*) from emp group by dep;        
        select dep,AVG(salary) from emp group by dep;
        
    orm:
        queryset=models.Emp.objects.values("dep").annotate(c=Count("*"))
    '''
    from django.db.models import Avg,Count,Max,Min

    # 查询每一个部门的人数
   #  queryset=models.Emp.objects.values("dep").annotate(c=Count("*"))
   #  print(queryset)  # <QuerySet [{'dep': '销售部', 'c': 1}, {'dep': '人事部', 'c': 2}]>
   #
   # # 查询每一个省份的平均薪水
   #  queryset=models.Emp.objects.values("province").annotate(avg_salary=Avg("salary"))
   #  print(queryset) # <QuerySet [{'province': '山东', 'avg_salary': 4500.0}, {'province': '河北', 'avg_salary': 5000.0}]>

    ############### 多表分组查询
    # 1 查询每一个出版社的名字和出版过的书籍的平均价格
    '''
       
        -- sql语句:
        SELECT app01_publish.name,AVG(app01_book.price) from app01_book LEFT JOIN app01_publish on 
                                 app01_book.publish_id = app01_publish.id
                                 group by app01_publish.id,app01_publish.name
    '''

    # queryset=models.Publish.objects.values("id","name").annotate(avg_price=Avg("book__price"))
    # queryset=models.Publish.objects.values("id","name","email","city").annotate(avg_price=Avg("book__price"))
    # [{"id":1,"name":"苹果出版社","eamil":"123","city":"beijing",'avg_price': 119.0},{"id":1,"name":"橘子出版社","eamil":"123","city":"beijing",'avg_price': 155.333333.0}]

    # queryset=models.Publish.objects.all().annotate(avg_price=Avg("book__price"))
    # print(queryset) #<QuerySet [<Publish: 苹果出版社>, <Publish: 橘子出版社>]>
    # for obj in queryset:
    #     print(obj.name,obj.avg_price)

    # 2 查询每一个作者的名字以及出版书籍的个数
    queryset=models.Author.objects.annotate(c=Count("book")).values("name","c")
    print(queryset) # <QuerySet [{'name': 'alex', 'c': 2}, {'name': 'egon', 'c': 2}]>

    # 3 查询每一个书籍的名称以及作者的个数
    queryset=models.Book.objects.annotate(c=Count("authors")).values("title","c")
    print(queryset)

    # 4 查询作者个数大于1 的每一本书籍的名称和作者个数
    queryset=models.Book.objects.annotate(c=Count("authors")).filter(c__gt=1).values("title","c")
    print(queryset) # <QuerySet [{'title': 'python', 'c': 2}, {'title': 'go', 'c': 2}]>

    # 5 查询书籍名称包含"h"的书籍名称和作者个数
    queryset=models.Book.objects.filter(title__contains="h").annotate(c=Count("authors")).values("title","c")

    ###################################### F查询与Q查询
    #  F查询
    from django.db.models import F,Q,Avg
    # 1 查询评论数大于100的文章
    # queryset=models.Article.objects.filter(comment_num__gt=100)
    # print(queryset)
    # 2 查询评论数大于点赞数的文章
    # queryset=models.Article.objects.filter(comment_num__gt=F("poll_num"))
    # print(queryset) # <QuerySet [<Article: 那一夜>]>
    # 3 查询点赞数大于两倍评论数
    # queryset=models.Article.objects.filter(poll_num__gt=F("comment_num")*2)
    # print(queryset)  # <QuerySet [<Article: 那一天>]>
    # 4 将所有的书籍的价格提高100元
    # models.Book.objects.all().update(price=F("price")+100)
    # Q查询
    # 5 查询价格大于300或者名称以p开头的书籍
    # Q : & | ~
    # queryset=models.Book.objects.filter(Q(title__startswith="p")&Q(price__gt=300))
    # print(queryset) # <QuerySet [<Book: python>, <Book: php>, <Book: pJS>]>
    # # 5 查询价格大于300或者不是2019年一月份的书籍
    # lq=Q(price__gt=300)|~Q(Q(pub_date__year=2019)&Q(pub_date__month=1))
    queryset = models.Book.objects.filter(q)
    # print(queryset)


    return HttpResponse("查询成功!")





def books(request):

    queryset=models.Book.objects.all()


    return render(request,"books.html",{"queryset":queryset})


def delbook(request,id):
    models.Book.objects.filter(pk=id).delete()


    return  redirect("/books/")


def addbook(request):
    if request.method=="POST":

        data=request.POST.dict()
        data.pop("csrfmiddlewaretoken")
        data.pop("author_list")
        book=models.Book.objects.create(**data)  #  保证提交键值对的键必须和数据库表字段一致
        #  为书籍绑定作者关系
        author_list=request.POST.getlist("author_list")
        print(author_list) # ['1', '2']
        book.authors.add(*author_list)

        return redirect("/books/")
    else:

        publish_list=models.Publish.objects.all()
        author_list=models.Author.objects.all()
        return render(request,'addbook.html',locals())


def editbook(request,edit_book_id):
    edit_book = models.Book.objects.filter(pk=edit_book_id).first()
    if request.method=="POST":
        # 方式1:
        # title=request.POST.get("title")
        # price=request.POST.get("price")
        # pub_date=request.POST.get("pub_date")
        # publish_id=request.POST.get("publish_id")
        # author_list=request.POST.getlist("author_list")
        # models.Book.objects.filter(pk=edit_book_id).update(title=title,price=price,pub_date=pub_date,publish_id=publish_id)  # update只有queryset才能调用
        # edit_book.authors.set(author_list)

        #  方式2:

        data=request.POST.dict()
        data.pop("csrfmiddlewaretoken")
        author_list=data.pop("author_list")
        models.Book.objects.filter(pk=edit_book_id).update(**data)  #  保证提交键值对的键必须和数据库表字段一致
        #  为书籍绑定作者关系
        author_list=request.POST.getlist("author_list")
        edit_book.authors.set(author_list)

        return redirect("/books/")
    else:

        publish_list=models.Publish.objects.all()
        author_list=models.Author.objects.all()
        return render(request,'editbook.html',locals())



from app01.models import UserInfo
import json
from django.http import JsonResponse

def login(request):

    if request.method=="GET":
        return render(request,"login.html")
    else:
        res={"user":None,"msg":None}
        user=request.POST.get("user")
        pwd=request.POST.get("pwd")
        user_obj=UserInfo.objects.filter(user=user,pwd=pwd).first()
        if user_obj:
            # 登陆成功!
            res["user"]=user_obj.user
        else:
            # 登录失败
            res["msg"]='用户名或者密码错误!'
        return JsonResponse(res)


def del_ajax(request):
    res={"state":True}
    try:
        pk=request.GET.get("pk")
        models.Book.objects.filter(pk=pk).delete()
    except Exception as e:
        res["state"]=False
    return JsonResponse(res);


