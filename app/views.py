from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import BattleForm
from app import BattleField


def index(request):
    if request.method == 'POST':
        my_form = BattleForm(request.POST)
        if my_form.is_valid():
            soldiers = int(request.POST['soldiers'])
            vehicles = int(request.POST['vehicles'])
            squads_number_ = int(request.POST['squads_number'])
            armies_number_ = int(request.POST['armies_number'])
            strategy_ = request.POST['strategy']
            if 5 <= soldiers + vehicles <= 10 and squads_number_ >= 2 \
                    and armies_number_ >= 2:
                battle = BattleField.BattleField(armies_number=armies_number_,
                                                 strategy=strategy_,
                                                 squads_number=squads_number_,
                                                 soldiers_number=soldiers,
                                                 vehicles_number=vehicles)
                win = battle.start()
            else:
                win = 0
            return redirect('result', win=win)
    else:
        my_form = BattleForm()
    return render(request, 'index.html', {'form': my_form})


def result(request, win):
    return render(request, 'result.html', {'win': win})
