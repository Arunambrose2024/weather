from django.shortcuts import render,redirect
import  requests
from .models import cities

def weatherapp(request):
    url='http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=c1d7bced3d399e87052d44c73c4937e3'

    weather_data=[]
    cities_list=cities.objects.all()
    if request.method =='POST':
        city=request.POST.get('city')
        if city:
            add_city = cities.objects.create(city=city)
            add_city.save()
            return redirect('/')
    for city in cities_list:
        get_weather = requests.get(url.format(city)).json()
        
        weather ={
            'city':city,
            'temp':get_weather['main']['temp'],
            'humidity':get_weather['main']['humidity'],
            'desc':get_weather['weather'][0]['description'],
            'icon':get_weather['weather'][0]['icon'],
        }
        
        weather_data.append(weather)
    context = {'weather_data':weather_data}    
    return render(request,'weather.html',context)
