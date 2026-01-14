from django.shortcuts import render

def recta_view(request):
    recta = None
    if request.method == "POST":
        ini = int(request.POST['ini'])
        fin = int(request.POST['fin'])
        recta = list(range(ini, fin + 1))

    return render(request, 'recta/recta.html', {"recta": recta})
