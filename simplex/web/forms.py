from django import forms


class KnapsackForm(forms.Form):
    peso_mochila = forms.IntegerField(min_value=1)
    peso_notebook = forms.IntegerField(min_value=1)
    beneficio_notebook = forms.IntegerField(min_value=1)
    peso_tenis = forms.IntegerField(min_value=1)
    beneficio_tenis = forms.IntegerField(min_value=1)
    peso_caderno = forms.IntegerField(min_value=1)
    beneficio_caderno = forms.IntegerField(min_value=1)
