from django.shortcuts import render

def jerarquia_view(request):
    resultado = None
    error = None

    if request.method == "POST":
        expresion = request.POST['expresion']

        try:
            resultado = eval(expresion, {"__builtins__": None}, {})
        except:
            error = "Expresión inválida"

    return render(request, 'jerarquia/jerarquia.html', {
        "resultado": resultado,
        "error": error
    })
