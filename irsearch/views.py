from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Book
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