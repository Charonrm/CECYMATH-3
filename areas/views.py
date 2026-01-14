from django.shortcuts import render
import math

def areas(request):
    resultado = None
    perimetro = None
    figura = request.POST.get("figura", None)
    mostrar = False

    # Cuando solo elige figura
    if request.method == "POST" and "seleccionar" in request.POST:
        mostrar = True

    # Cuando ya calcularon
    if request.method == "POST" and "calcular" in request.POST:

        if figura == "circulo":
            radio = float(request.POST.get("radio", 0))
            area = math.pi * radio**2
            per = 2 * math.pi * radio
            resultado = f"Área del círculo: {round(area, 2)}"
            perimetro = f"Perímetro del círculo: {round(per, 2)}"

        elif figura == "cuadrado":
            lado = float(request.POST.get("lado", 0))
            area = lado * lado
            per = 4 * lado
            resultado = f"Área del cuadrado: {round(area, 2)}"
            perimetro = f"Perímetro del cuadrado: {round(per, 2)}"

        elif figura == "rectangulo":
            base = float(request.POST.get("base", 0))
            altura = float(request.POST.get("altura", 0))
            area = base * altura
            per = 2 * (base + altura)
            resultado = f"Área del rectángulo: {round(area, 2)}"
            perimetro = f"Perímetro del rectángulo: {round(per, 2)}"

        elif figura == "triangulo":
            base = float(request.POST.get("base_triangulo", 0))
            altura = float(request.POST.get("altura_triangulo", 0))
            area = (base * altura) / 2
            # Suponemos triángulo rectángulo (si no, tú dices)
            per = base + altura + math.sqrt(base**2 + altura**2)
            resultado = f"Área del triángulo: {round(area, 2)}"
            perimetro = f"Perímetro del triángulo: {round(per, 2)}"

        mostrar = True

    return render(request, "areas/areas.html", {
        "resultado": resultado,
        "perimetro": perimetro,
        "figura": figura,
        "mostrar": mostrar
    })
