from django.shortcuts import render

# Create your views here.

import urllib.request
import json

def index(request):
	source = urllib.request.urlopen('https://www.7timer.info/bin/astro.php?lon=113.2&lat=23.1&ac=0&unit=metric&output=json&tzshift=0').read()
	list_of_data = json.loads(source)
	return render(request,'index.html',locals())












