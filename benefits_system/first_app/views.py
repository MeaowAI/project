from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#หน้าหลักของเว็บ
def index(request):
    my_dict = {'insert_me':'Now I am coming from first_app/index.html'}
    return render(request,'index.html',context=my_dict)
#หน้าสมัครสมาชิกกลุ่มสวัสดิการ
def create_accout(request):
    return render(request,'cr_acc.html')
#หน้าคำร้องขอสวัสดิการ
def requests(request):
    return render(request,'request.html')
#ขอเพิ่มหุ้นสมาชิกกลุ่มสวัสดิการ
def inc_share_form(request):
    return render(request,'inc_share.html')
#ลาหุ่น/ถอนหุ่นบางส่วนจากกลุ่มสวัสดิการ
def withdraw_form(request):
    return render(request,'withdraw.html')
#ใบสำคัญรับเงิน
def reciept_form(request):
    return render(request,'reciept.html')
#หน้าล็อกอิน
def signin_form(request):
    return render(request,'login/signin.html')
