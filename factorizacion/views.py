from django.shortcuts import render
import math

def factorizacion_view(request):
    resultado = None
    error = None

    if request.method == "POST":
        a = float(request.POST['a'])
        b = float(request.POST['b'])
        c = float(request.POST['c'])

        disc = b*b - 4*a*c

        if disc < 0:
            error = "No se puede factorizar (raíces complejas)."
        else:
            r1 = (-b + math.sqrt(disc)) / (2*a)
            r2 = (-b - math.sqrt(disc)) / (2*a)
            resultado = f"{a}(x - {r1})(x - {r2})"

    return render(request, 'factorizacion/factorizacion.html', {
        "resultado": resultado, "error": error
    })
