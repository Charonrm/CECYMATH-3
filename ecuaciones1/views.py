from django.shortcuts import render

def ecuacion1_view(request):
    x = None
    error = None

    if request.method == "POST":
        a = float(request.POST['a'])
        b = float(request.POST['b'])
        c = float(request.POST['c'])

        if a == 0:
            error = "a no puede ser cero."
        else:
            x = (c - b) / a

    return render(request, 'ecuaciones1/ecuaciones1.html', {"x": x, "error": error})
