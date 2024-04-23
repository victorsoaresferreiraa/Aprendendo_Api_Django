"""from django.http import JsonResponse

# Create your views here.

def aluno(request):
    if request.method == 'GET':
        aluno = {'id':1,  'nome': 'Guilerme'}
        return JsonResponse(aluno)"""

from rest_framework import viewsets
from escola.models import Aluno, Curso
from serializer import AlunoSerializer, CursoSerializer

class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos e alunas"""
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
