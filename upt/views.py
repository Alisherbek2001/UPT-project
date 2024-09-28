from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import *
from .serializers import *

class HomePageAPIView(APIView):
    def get(self,request):
        project = Project.objects.all()
        serializer = ProjectsSerializer(project, many=True, context={'request': request})
        return Response(serializer.data)
    
class ProjectPageAPIView(APIView):
    def get(self,request):
        data = {
            'projects':Project.objects.all(),
            'feedback':Feedback.objects.all(),
        }
        serializers = ProjectsPageSerializer(data,context={'request':request})
        return Response(serializers.data)
    
    
class MemberAPIView(APIView):
    def get(self,request):
        member = Member.objects.all()
        serializer = MemberSerializer(member, many=True, context={'request': request})
        return Response(serializer.data)