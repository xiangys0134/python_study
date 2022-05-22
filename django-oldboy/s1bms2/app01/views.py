from django.shortcuts import render,redirect,HttpResponse

# Create your views here.

from app01.models import Book,Publish,Author,AuthorDetail,Emp

def add(request):
    # Publish.objects.create(name="苹果出版社",addr="北京")

    # Book.objects.create(title="linux",price=122,pub_date="2012-12-12",publish_id=1)
    publish = Publish.objects.filter(name="苹果出版社").first()
    book_obj = Book.objects.create(title="istio", price=176, pub_date="2012-12-1", publish=publish)

    authors_list = Author.objects.filter(name__in=["张三","alex"])
    book_obj.authors.add(*authors_list)
    return  HttpResponse("OK")

def delete(request):
    book = Book.objects.filter(title="prometheus").first()
    author_list = Author.objects.filter(name="alex")
    book.authors.remove(*author_list)
    return HttpResponse("删除成功")

def addauthor(request):
    # 通过书籍绑定作者
    # book = Book.objects.filter(title="istio").first()
    # authors = Author.objects.filter(name="alex")
    # book.authors.set(authors)

    # 通过作者绑定书籍
    author = Author.objects.filter(name="alex").first()
    books = Book.objects.filter(title__in=["linux","go"])
    author.book_set.set(books)

    return HttpResponse("更新作者成功")

def query(request):
    # 对象查询(子查询)
    # 查询python书籍的出版社地址
    # obj = Publish.objects.filter(book__title="linux").first()
    #
    # print(obj.addr)

    # 查询苹果出版社出版过的所有书籍名称
    # publishs = Book.objects.filter(publish__name="苹果出版社").values("title")
    # print(publishs)

    # publish_obj = Publish.objects.filter(name="苹果出版社").first()
    # obj = publish_obj.book_set.all().values("title")
    # print(obj)

    # 多对多
    # 查询linux书籍所有作者的名字
    # obj = Author.objects.filter(book__title="linux").all().values("name")
    # print(obj)

    # book_obj = Book.objects.filter(title="linux").first()
    # obj = book_obj.authors.all().values("name")
    # print(obj)

    # 查询alex作者出版过所有书籍的名称
    # obj = Book.objects.filter(authors__name="alex").all().values("title")
    # print(obj)

    # 一对一
    # 查询alex的女朋友的名字
    # obj = AuthorDetail.objects.filter(author__name="alex").values("gf")
    # print(obj)

    # 查询女朋友叫铁锤的作者的名字
    # obj = Author.objects.filter(authordetail__gf="铁锤").values("name")
    # print(obj)

    # 基于双下划线的join查询
    # python书籍的出版社地址
    # obj = Book.objects.filter(title="linux").all().values("publish__addr")
    # print(obj)

    # 查询linux书籍所有作者的名字
    # obj = Book.objects.filter(title="linux").values("authors__name")
    # print(obj)

    # 查询alex的女朋友的名字

    # obj = Author.objects.filter(name="alex").values("authordetail__gf")
    # print(obj)

    # 连续跨表：查询苹果出版社出版过的所有书籍的名字及作者的名字
    # obj = Publish.objects.filter(name="苹果出版社").values("book__title","book__authors__name")
    # print(obj)

    # 查询平均价格
    from django.db.models import Avg,Max,Min,Count

    # ret = Book.objects.all().aggregate(Avg("price"))
    # print(ret)

    # 查询主键大于5的所有书籍的平均价格
    # obj = Book.objects.filter(id__gt=5).aggregate(Avg("price"))
    # print(obj)

    #单表分组查询
    # obj = Emp.objects.values("dep").annotate(avgAalary=Avg("salary"))
    # print(obj)

    # 查询每一个省份的员工数
    obj = Emp.objects.values("province").annotate(c=Count("*"))
    print(obj)



    return HttpResponse("查询成功")

