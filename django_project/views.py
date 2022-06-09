# from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

def greeting(request):
 context = {
  'greeting': 'Manga é bom demais. :)',
       'today': datetime.now()
}
 return render(request, 'greeting.html', context)