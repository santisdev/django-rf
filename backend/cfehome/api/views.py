import json
from django.http import JsonResponse

def api_home (request, *args, **kwargs):
  print(request.GET) # url query params
  body = request.body  #JSON byte string body
  data = {}
  try:
    data = json.loads(body) # string of jsondata -> python dictionary
  except:
    pass
  print(data)
  data['params'] = dict(request.GET)
  data['headers'] = dict(request.headers)
  data['content_type'] = request.content_type
  return JsonResponse(data)

 