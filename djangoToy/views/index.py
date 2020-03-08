from django.http import HttpResponse

def testindex(request):
  return HttpResponse("first View Page")