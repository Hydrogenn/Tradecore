from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

#from django.http import HttpResponseRedirect

@login_required
def profile(request):
    user = request.user
    context = {'user': user}
    return render(request, 'tradecore/profile.html', context)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('tradecore:profile')
    else:
        form = UserCreationForm()
    return render(request, 'tradecore/signup.html', {'form': form})