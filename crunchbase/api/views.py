from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from .models import People_Crunchbase,Company_Crunchbase
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt






class CompanySave(APIView):
  permission_classes = (permissions.IsAuthenticated, )
  authentication_classes = (TokenAuthentication,)



  def get(self, request, format=None):
        return Response({'data_status':True})

  def post(self,request, *args, **kwargs):


      try:
          if not Company_Crunchbase.objects.filter(name=request.data["name"]).exists():
              obj_company=Company_Crunchbase()
              obj_company.name = request.data["name"]
              obj_company.description = request.data["description"]
              obj_company.rank = request.data["rank"]
              obj_company.category  = request.data["category"]
              obj_company.location = request.data["location"]
              obj_company.website = request.data["website"]
              obj_company.facebook = request.data["facebook"]
              obj_company.twitter = request.data["twitter"]
              obj_company.linkdin = request.data["linkdin"]
              obj_company.phone = request.data["phone"]
              obj_company.email = request.data["email"]
              obj_company.status = request.data["email"]
              obj_company.last_funding_type = request.data["last-funding-type"]
              obj_company.save()
              return Response({'data_status':True})
          else:
              return Response({'data_status':True})
      except:
         return Response({'data_status':False})



class PeopleSave(APIView):
  permission_classes = (permissions.IsAuthenticated, )
  authentication_classes = (TokenAuthentication,)





  def get(self, request, format=None):
        return Response({'data_status':True})

  def post(self,request, *args, **kwargs):


      try:
          if not People_Crunchbase.objects.filter(name=request.data["name"]).exists():
              obj_person=People_Crunchbase()
              obj_person.name = request.data["name"]
              obj_person.gender = request.data["gender"]
              obj_person.designation = request.data["designation"]
              obj_person.first_name  = request.data["first_name"]
              obj_person.last_name = request.data["last_name"]
              obj_person.rank = request.data["rank"]
              obj_person.twitter = request.data["twitter"]
              obj_person.facebook = request.data["facebook"]
              obj_person.company_name = request.data["company"]
              obj_person.location = request.data["location"]
              obj_person.linkdin = request.data["linkdin"]
              obj_person.biography=request.data["biography"]
              obj_person.save()
              return Response({'data_status':True})
          else:
              return Response({'data_status':True})

      except:
         return Response({'data_status':False})



