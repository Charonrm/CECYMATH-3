from django.shortcuts import render

def resta_view(request):
    resultado = None
    if request.method == "POST":
        a = float(request.POST['a'])
        b = float(request.POST['b'])
        resultado = a - b
    return render(request, 'resta/resta.html', {"resultado": resultado})
