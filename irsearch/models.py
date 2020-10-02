from django.db import models

# Create your models here.
class Book(models.Model):
    ten_sach = models.CharField(max_length = 255, null = False, blank = False)
    ten_tac_gia = models.CharField(max_length = 255, null = False, blank = False)
    nam_xuat_ban = models.CharField(max_length = 4, null = False)
    so_trang = models.IntegerField(null = False)
    noi_dung = models.TextField(null = False)