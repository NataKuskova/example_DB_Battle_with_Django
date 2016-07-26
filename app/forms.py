from django import forms


class BattleForm(forms.Form):
    soldiers = forms.IntegerField(required=True)
    vehicles = forms.IntegerField(required=True)
    squads_number = forms.IntegerField(required=True)
    armies_number = forms.IntegerField(required=True)

    CHOICES = (('random', 'Случайная',), ('weakest', 'Слабейшая',),
               ('strongest', 'Сильнейшая',))
    strategy = forms.ChoiceField(widget=forms.Select,
                                 required=True,
                                 choices=CHOICES)



