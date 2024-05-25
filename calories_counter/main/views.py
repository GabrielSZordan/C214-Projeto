from django.shortcuts import render
from django.http import JsonResponse
import requests
import json

def index(request):
    if request.POST:
        alimentos = request.POST.getlist('alimentos[]')
        pesos = request.POST.getlist('pesos[]')

        resultados = []

        for alimento, peso in zip(alimentos, pesos):
            consulta = f"{peso}g {alimento}"
            api_url = f'https://api.api-ninjas.com/v1/nutrition?query={consulta}'
            response = requests.get(api_url, headers={'X-Api-Key': 'mXQkKui50jO0+SOKXc8MRA==SBvHrJvnNrAIvTCk'})

            if response.status_code == requests.codes.ok:
                dados = json.loads(response.text)[0]
                calorias = dados.get('calories', 0)
                resultados.append({'alimento': alimento, 'calorias': calorias})
            else:
                resultados.append({'alimento': alimento, 'calorias': 0})

        # Agora 'resultados' é uma lista de dicionários com os resultados de cada consulta

        # Calcular a soma total das calorias
        total_calorias = sum(resultado['calorias'] for resultado in resultados)

        # Adicionar os resultados e a soma total ao contexto
        context = {
            'resultados': resultados,
            'total_calorias': total_calorias,
        }

        print(context['total_calorias'])

        return JsonResponse(context)
    else:
        return render(request, "main/index.html")


