# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View

from web.forms import KnapsackForm
from knapsack import knapsack


class Knapsack(View):
    def get(self, request):
        return render(request, 'knapsack.html')

    def post(self, request):
        form = KnapsackForm(request.POST)
        if form.is_valid():
            peso_mochila = form.cleaned_data.get('peso_mochila')
            peso_notebook = form.cleaned_data.get('peso_notebook')
            beneficio_notebook = form.cleaned_data.get('beneficio_notebook')
            peso_tenis = form.cleaned_data.get('peso_tenis')
            beneficio_tenis = form.cleaned_data.get('beneficio_tenis')
            peso_caderno = form.cleaned_data.get('peso_caderno')
            beneficio_caderno = form.cleaned_data.get('beneficio_caderno')

            # peso cada objeto
            wi = {
                'notebook': peso_notebook,
                'tenis': peso_tenis,
                'caderno': peso_caderno
            }
            # beneficio/valor de cada objeto
            vi = {
                'notebook': beneficio_notebook,
                'tenis': beneficio_tenis,
                'caderno': beneficio_caderno
            }
            status, resposta = knapsack(peso_mochila, wi, vi)

            return JsonResponse({
                'status': status,
                'resposta': ', '.join(resposta)
            })
        return JsonResponse({'erro': form.errors.as_text()}, status=400)
