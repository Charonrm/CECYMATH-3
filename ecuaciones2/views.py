from django.shortcuts import render
import math

def ecuacion2_view(request):
    x1 = x2 = None
    error = None

    if request.method == "POST":
        a = float(request.POST['a'])
        b = float(request.POST['b'])
        c = float(request.POST['c'])

        if a == 0:
            error = "a no puede ser cero."
        else:
            disc = b*b - 4*a*c
            if disc < 0:
                error = "No hay soluciones reales."
            else:
                x1 = (-b + math.sqrt(disc)) / (2*a)
                x2 = (-b - math.sqrt(disc)) / (2*a)

    return render(request, 'ecuaciones2/ecuaciones2.html', {
        "x1": x1, "x2": x2, "error": error
    })
