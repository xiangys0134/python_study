from django.shortcuts import render

# Create your views here.


from django.shortcuts import render,redirect,HttpResponse

# Create your views here.

import  random
from app01.models import UserInfo

def login(request):
    if request.method == "GET":
        return render(request,"login.html")
    else:
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        validCode = request.POST.get("validCode")
        if validCode.upper() == request.session["str_rand"].upper():
            return HttpResponse("ok")
        else:
            return HttpResponse("error")

        user_obj = UserInfo.objects.filter(name=user,pwd=pwd).first()

        if user_obj:
            obj = redirect("/index_session/")
            request.session["is_login"] = True
            request.session["username"] = user
            username = request.session.get("username")
            return obj
        return HttpResponse("Error!")

def index(request):
    is_login = request.session.get("is_login")
    username = request.session.get("username")
    return render(request,"index.html",locals())


def logout_session(request):
    obj = redirect("/login_session/")
    request.session.flush()
    return obj

def get_random_color():
    return random.randint(0,255),random.randint(0,255),random.randint(0,255)

def valid_img(request):
    from PIL import Image,ImageDraw,ImageFont

    # img = Image.new("RGB",(250,40),get_random_color())
    # f = open("validcode.png","wb")
    # img.save(f,"png")
    # with open("validcode.png","rb") as f:
    #     data = f.read()

    from io import BytesIO
    img = Image.new("RGB",(250,40),get_random_color())
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("static/font/kumo.ttf",34)

    #噪点噪线
    width = 250
    height = 40

    for i in range(10):
        x1 = random.randint(0,width)
        x2 = random.randint(0,width)
        y1 = random.randint(0,height)
        y2 = random.randint(0,height)
        draw.line((x1,y1,x2,y2),fill=get_random_color())

    for i in range(100):
        draw.point([random.randint(0,width),random.randint(0,height)],fill=get_random_color())
        x = random.randint(0,width)
        y = random.randint(0,height)
        draw.arc((x,y,x+4,y+4),0,90,fill=get_random_color())

    l1 = []
    for i in range(5):
        list1 = [chr(i) for i in range(65, 91)]
        list2 = [chr(i) for i in range(97,123)]
        list3 = [str(i) for i in range(0,9)]

        str_list = list1 + list2 +list3
        random_num = random.choice(str_list)
        l1.append(str(random_num))

    str_rand = "".join(l1)
    draw.text((50,0),str_rand,"red",font=font)

    f=BytesIO()
    img.save(f,"png")
    data = f.getvalue()
    request.session["str_rand"] = str_rand
    return HttpResponse(data)

