from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
import urllib
import requests
api_key = ''   # add api key here
url='https://maps.googleapis.com/maps/api/geocode/json?address=&key=YOUR_API_KEY'
@csrf_exempt
def getCoordinates(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    address = body['address']
    output_format = body['output_format']
    url='https://maps.googleapis.com/maps/api/geocode/json?address='
    
    address = address.split()
    address.remove('#')
    url +=address[0]
    for i in address[1:]:
        url = url + '+' +i
    url = url+ f'&key={api_key}'
    res = requests.get(url)
    data=res.json()
    location = data["results"][0]['geometry']['location']
    if output_format == 'json':
        return JsonResponse({"location":location,"address":body['address']})
    
    print(address)
    context = {
        'address':body['address'],
        'lat':location['lat'],
        'lng':location['lng']
    }
    return render(request, 'xmltemplate.xml', context, content_type='text/xml')