from django.shortcuts import render, redirect
from django.views import View
from .models import *
from userapp.models import Ombor

class MahsulotView(View):
    def get(self, request):
        if request.user.is_authenticated:
            o = Ombor.objects.get(user=request.user)
            m = Mahsulot.objects.filter(ombor=o)
            return render(request, "products.html", {"products":m})
        return redirect("login")

    def post(self,request):
        o = Ombor.objects.get(user=request.user)
        Mahsulot.objects.create(
            nom = request.POST.get("n"),
            brend = request.POST.get("b"),
            miqdor = request.POST.get("m"),
            kelgan_narx = request.POST.get("kn"),
            sotuv_narx = request.POST.get("sn"),
            ombor = o
        )
        return redirect("mahsulotlar")



class BolimView(View):
    def get(self, request):
        return render(request, "bulimlar.html")

class ClientView(View):
    def get(self, request):
        return render(request, "clients.html")

class MahsulotEdit(View):
    def get(self,request,pk):
        m=Mahsulot.objects.get(id=pk)
        return render(request,"product_update.html",{"product":m})
    def post(self,request,pk):
        Mahsulot.objects.filter(id=pk).update(
            miqdor=request.POST.get("m"),
            kelgan_narx=request.POST.get("kn"),
            sotuv_narx=request.POST.get("sn"),
        )
        return redirect("mahsulotlar")


