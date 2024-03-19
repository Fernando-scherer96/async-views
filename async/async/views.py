'''import time

from django.http import JsonResponse

def api(request):
    time.sleep(1)
    payload = {'message': 'hello from crowbotics!'}

    if 'task_id' in request.GET:
        payload['task_id'] = request.GET["task_id"]
    return JsonResponse(payload)'''

from time import sleep
import asyncio
import httpx
from django.http import HttpResponse

# Função assíncrona para realizar chamadas HTTP
async def http_call_async():
    # Loop para simular uma operação demorada, pausando por 1 segundo em cada iteração
    for num in range(1, 6):
        await asyncio.sleep(1)  # Pausa assíncrona
        print(num)

    # Iniciando uma sessão HTTP assíncrona
    async with httpx.AsyncClient() as client:
        # Fazendo uma chamada GET assíncrona para um serviço de teste
        response = await client.get('https://httpbin.org/get')
        print(response)  # Imprimindo a resposta da chamada HTTP

# Função síncrona para realizar chamadas HTTP
def http_call_sync():
    # Loop para simular uma operação demorada, pausando por 1 segundo em cada iteração
    for num in range(1, 6):
        sleep(1)  # Pausa síncrona
        print(num)

    # Realizando uma chamada GET síncrona
    response = httpx.get('https://httpbin.org/get')
    print(response)  # Imprimindo a resposta da chamada HTTP

# Visão assíncrona do Django para tratar requisições
async def async_view(request):
    # Inicia a tarefa assíncrona sem aguardar sua conclusão
    asyncio.create_task(http_call_async())

    # Retorna uma resposta HTTP imediatamente, não bloqueia a requisição
    return HttpResponse('Non-blocking HTTP request')

# Visão síncrona do Django para tratar requisições
def sync_view(request):
    # Executa uma função síncrona que bloqueia até sua conclusão
    http_call_sync()

    # Retorna uma resposta HTTP após a conclusão da função síncrona
    return HttpResponse('Blocking HTTP request')

