from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import UserProfile
from .serializers import UserProfileSerializer


class UserProfileView(ViewSet):
    queryset = UserProfile.objects.all()
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        queryset = UserProfile.objects.all()
        serializer = UserProfileSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = UserProfile.objects.all()
        user = get_object_or_404(queryset, user_id=pk)
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)
