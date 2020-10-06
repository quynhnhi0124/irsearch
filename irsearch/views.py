import re
from django.shortcuts import render
# from django.http import HttpResponse
# from django.views import View
from .models import Book
# from docx import Document
# Create your views here.


# Hiện trang

def index_result(request):
    return render(request, 'pages/result.html')


# Hiện trang với thông tin từ db (thông tin dc lấy là một dictionary)
def display(request):
    book = Book.objects.all() # lấy mọi dòng từ bảng Book trong db
    # context: dictionary bao gồm cặp tên biến & giá trị: {'key': value}
    context = {
        'book': book,
    }
    return render(request, 'pages/base.html',context) #render trang với context

def test(request, id):
    t = Book.objects.filter(id = id)
    nd = Book.objects.values('noi_dung').filter(id = id) # lấy tên của sách (cột noi_dung) được chọn theo id
    vals = list(nd.values())[0]['noi_dung']
    f = open("static/docxfile/" + vals, "r", encoding = 'latin-1')
    file_content = f.read()
    f.close()
    context = {
        't' : t , 
        'file_content' :file_content ,
    }
    return render(request, 'pages/test.html', context)
#sửa lỗi class has no 'objects' member
# cmd:  pip install pylint-django
#       Ctrl + shift + P > Preferences: Configure Language Specific Settings > Python
#       sửa file settings.json thành:
#     {
#       "python.linting.pylintArgs": [
#         "--load-plugins=pylint_django"
#       ],

#       "[python]": {

#     }
# }