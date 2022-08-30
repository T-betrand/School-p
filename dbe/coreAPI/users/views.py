from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import User, ServiceProvider, Skills, Jobs 
from .serializers import UserSerializer, UserCreateSerializer, ServiceProviderSerializer, SkillsSerializer, JobsSerializer 


# Create your views here.
class UserViewSet(viewsets.ViewSet):
    
    def list(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK) 

    def create(self, request):
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED) 

    def retrieve(self, request, pk=None):
        user = User.objects.get(id=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        user = User.objects.get(id=pk)
        serializer = UserCreateSerializer(instance=user, data=request.data)
        serializer.is_valid(raise_exception=True) 
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        user = User.objects.get(id=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 


class ServiceProviderViewSet(viewsets.ViewSet):
    
    def list(self, request):

        service_provider = ServiceProvider.objects.all()
        serializer = ServiceProviderSerializer(service_provider, many=True)     
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = ServiceProviderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        service_provider = ServiceProvider.objects.get(id=pk)
        skill_list = []
        skills = Skills.objects.filter(owner=service_provider.id)
        for skill in skills:
            skill_list.append({'name': skill.name})
        service_provider.skills = Skills.objects.filter(owner=service_provider.id)

        serializer = ServiceProviderSerializer(service_provider) 
       #list of skills 
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        service_provider = ServiceProvider.objects.get(id=pk)
        serializer = ServiceProviderSerializer(instance=service_provider, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        service_provider = ServiceProvider.objects.get(id=pk)
        service_provider.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SkillsViewSet(viewsets.ViewSet):
    
    def list(self, request):
        skills = Skills.objects.all()
        serializer = SkillsSerializer(skills, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = SkillsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED) 

    def retrieve(self, request, pk=None):
        skill = Skills.objects.get(skill_id=pk)
        serializer = SkillsSerializer(skill)
        return Response(serializer.data, status=status.HTTP_200_OK)
        # skills = Skills.objects.all()
        # for s in skills:
        #     if int(s.skill_id) == int(skill.skill_id):
        #         serializer = SkillsSerializer(skill)
        #         return Response(serializer.data, status=status.HTTP_200_OK)
        #     else:
        #         return Response({"message": "skill doesn't exist"}, status=status.HTTP_404_DOES_NOT_EXIST)
  

    def update(self, request, pk=None):
        skill = Skills.objects.get(skill_id=pk)
        serializer = SkillsSerializer(instance=skill, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        skill = Skills.objects.get(skill_id=pk)
        skill.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class JobsViewSet(viewsets.ViewSet):
    
    def list(self, request):
        jobs = Jobs.objects.all()
        serializer = JobsSerializer(jobs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = JobsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED) 

    def retrieve(self, request, pk=None):
        job = Jobs.objects.get(job_id=pk)
        serializer = JobsSerializer(job)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        job = Jobs.objects.get(job_id=pk)
        serializer = JobsSerializer(instance=job, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        job = Jobs.objects.get(job_id=pk)
        job.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 


# class PhotoViewSet(viewsets.ViewSet):
#     pass 