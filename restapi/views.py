import json, os
from django.http import HttpResponse

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
MODELS = os.path.join(THIS_FOLDER, 'models')

with open(os.path.join(MODELS, 'resModel.json'), 'r') as str:
  resModel = json.load(str)

def ApiIndex(request):
  status = 200
  data = {
    'userAgent': request.headers['User-Agent'],
    'urlPath': request.path
  }
  msg = 'Success!'

  updateStatus = {'status': 200, 'data': data, 'msg': msg}
  resModel.update(updateStatus)

  return HttpResponse(f"{resModel}")

def methodGet(request):
  print('get')
  return HttpResponse('REST API Get Page')

def methodPost(request):
  print('post')
  return HttpResponse('REST API Post Page')

def methodPut(request):
  print('put')
  return HttpResponse('REST API Put Page')

def methodDelete(request):
  print('del')
  return HttpResponse('REST API Delete Page')