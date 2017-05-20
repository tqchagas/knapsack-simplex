from django import forms


class KnapsackForm(forms.Form):
    peso_mochila = forms.IntegerField(min_value=1, label="Peso total da mochila")
    peso_notebook = forms.IntegerField()
    beneficio_notebook = forms.IntegerField()
    peso_tenis = forms.IntegerField()
    beneficio_tenis = forms.IntegerField()
    peso_caderno = forms.IntegerField()
    beneficio_caderno = forms.IntegerField()
