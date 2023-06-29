from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View

from .models import Pergunta, Alternativa

class IndexView(View):
    def get(self, request, *args, **kwargs):
        lista_perguntas = Pergunta.objects.order_by('-data_pub')[:5]
        contexto = {'pergunta_list': lista_perguntas}
        return render(request, 'polls/index.html', contexto)

class DetalhesView(View):
    def get(self, request, *args, **kwargs):
        pergunta = get_object_or_404(Pergunta, pk = kwargs['pk'])
        return render(request, 'polls/detalhes.html', {'pergunta': pergunta})

class ResultadosView(View):
    def get(self, request, *args, **kwargs):
        pergunta = get_object_or_404(Pergunta, pk = kwargs['pk'])
        lista_resultados = Alternativa.objects.filter(pergunta = pergunta).order_by('-votos')
        contexto = {'pergunta':pergunta, 'lista_resultados':lista_resultados,}
        return render(request, 'polls/resultados.html', contexto)

class VotosView(View):
    def post(self, request, *args, **kwargs):
        pergunta = get_object_or_404(Pergunta, pk = kwargs['pk'])
        try:
            selected_alternativa = request.POST['alternativa']
            selected_pergunta = pergunta.alternativa_set.get(pk = selected_alternativa)
        except (KeyError, Alternativa.DoesNotExist):
            contexto = {
                'pergunta':pergunta, 'erro':"Selecione uma opção",
            }
            return render(request, 'polls/pergunta_detail.html', contexto)
        else:
            selected_pergunta.votos += 1
            selected_pergunta.save()
            return HttpResponseRedirect(reverse('polls:resultados', args = (kwargs['pk'],)))