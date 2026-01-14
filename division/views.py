from django.shortcuts import render

def division_view(request):
    resultado = None
    error = None

    if request.method == "POST":
        a = float(request.POST['a'])
        b = float(request.POST['b'])

        if b == 0:
            error = "No se puede dividir entre cero."
        else:
            resultado = a / b

    return render(request, 'division/division.html', {"resultado": resultado, "error": error})
