from django.shortcuts import render

from users.models import   CustomUser
# Create your views here.
def home(request):
    return render(request, "player/home.html",
                  {'users': CustomUser.objects.count()})