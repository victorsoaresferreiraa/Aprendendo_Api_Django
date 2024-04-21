from django.http import JsonResponse

# Create your views here.

def aluno(request):
    if request.method == 'GET':
        aluno = {'id':1,  'nome': 'Guilerme'}
        return JsonResponse(aluno)
