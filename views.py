from django.shortcuts import render

# Create your views here.

def pagina_inicial (request):
    context = {
    "nome": "joao", 
    "cachorros": 
    ["mel", "tobias","cacau", "bob", "madonna", "radija"]
    }
    return render(request, 'index.html', context)