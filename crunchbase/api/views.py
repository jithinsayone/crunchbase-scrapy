from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from .models import People_Crunchbase,Company_Crunchbase
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json,zlib





class CompanySave(APIView):
  permission_classes = (permissions.IsAuthenticated, )
  authentication_classes = (TokenAuthentication,)



  def get(self, request, format=None):
        return Response({'data_status':True})

  def post(self,request, *args, **kwargs):
      try:

          file_obj = request.FILES["file"]
          compress_data = file_obj.read()
          decompress_data = zlib.decompress(compress_data)
          decompress_data = decompress_data.decode("utf-8")
          data = json.loads(decompress_data)
          if data:
              for entry in data["scrapy"]:

                  obj_company=Company_Crunchbase()
                  obj_company.name = entry["name"]
                  obj_company.description = entry["description"]
                  obj_company.rank = entry["rank"]
                  obj_company.category  = entry["category"]
                  obj_company.location = entry["location"]
                  obj_company.website = entry["website"]
                  obj_company.facebook = entry["facebook"]
                  obj_company.twitter = entry["twitter"]
                  obj_company.linkdin = entry["linkdin"]
                  obj_company.phone = entry["phone"]
                  obj_company.email = entry["email"]
                  obj_company.save()
                  return Response({'data_status':True})
          else:
              return Response({'data_status':False})

      except:
         return Response({'data_status':False})



class PeopleSave(APIView):
  permission_classes = (permissions.IsAuthenticated, )
  authentication_classes = (TokenAuthentication,)





  def get(self, request, format=None):
        return Response({'data_status':True})

  def post(self,request, *args, **kwargs):

      try:
          obj_person=People_Crunchbase()
          obj_person.name = request.data["name"]
          obj_person.gender = request.data["gender"]
          obj_person.designation = request.data["designation"]
          obj_person.first_name  = request.data["first_name"]
          obj_person.last_name = request.data["last_name"]
          obj_person.rank = request.data["rank"]
          obj_person.twitter = request.data["twitter"]
          obj_person.facebook = request.data["facebook"]
          obj_person.company = request.data["company"]
          obj_person.location = request.data["location"]
          obj_person.linkdin = request.data["linkdin"]
          obj_person.save()
          return Response({'data_status':True})
      except:
         return Response({'data_status':False})
