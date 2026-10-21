from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from service_requests.models import ServiceRequest

from service_requests.serializers import UserSerializer,ServiceRequestSerializer

from service_requests.permissions import IsServiceRequestOwner

class SignUpView(APIView):

    def post(self, request):

        form_data = request.data

        serializer = UserSerializer(data=form_data)

        if serializer.is_valid():

            cleaned_data = serializer.validated_data

            user_object = User.objects.create_user(**cleaned_data)

            instance = UserSerializer(user_object)

            return Response(data=instance.data)

        else: return Response(serializer.errors)


class ServiceRequestListCreateView(APIView):

    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request):

        qs = ServiceRequest.objects.filter(user=request.user)

        serializer = ServiceRequestSerializer(qs,many=True)

        return Response(data=serializer.data)

    def post(self,request):

        form_data = request.data

        serializer = ServiceRequestSerializer(data=form_data)

        if serializer.is_valid():

            serializer.save(user=request.user)

            return Response(data=serializer.data)

        else: return Response(data=serializer.errors)

class ServiceRequestRetrieveUpdateDetailView(APIView):

    authentication_classes = [authentication.BasicAuthentication]

    permission_classes = [permissions.IsAuthenticated, IsServiceRequestOwner]

    def get(self, request, pk):

        instance = get_object_or_404(ServiceRequest,id=pk)

        self.check_object_permissions(request, instance)

        serializer = ServiceRequestSerializer(instance)

        return Response(data=serializer.data)

    def put(self, request, pk):

        instance = get_object_or_404(ServiceRequest,id=pk)

        self.check_object_permissions(request, instance)

        form_data = request.data

        serializer = ServiceRequestSerializer(instance,data=form_data)

        if serializer.is_valid():

            serializer.save()

            return Response(data=serializer.data)

        else:

            return Response(serializer.errors)

    def delete(self, request, pk):

        instance = get_object_or_404(ServiceRequest,id=pk)

        self.check_object_permissions(request, instance)

        instance.delete()

        return Response({"message": "Service request deleted successfully."})


class ServiceRequestCountView(APIView):

    authentication_classes = [authentication.BasicAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):

        total = ServiceRequest.objects.filter(user=request.user).count()
        
        return Response({"total_services": total})

class HighCriticalServiceRequestView(APIView):

    authentication_classes = [authentication.BasicAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):

        qs = ServiceRequest.objects.filter(user=request.user,priority__in=["High", "Critical"])

        serializer = ServiceRequestSerializer(qs, many=True)

        return Response(data=serializer.data)