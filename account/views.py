
from django.http import Http404

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny

from .models import User
from .serializers import UserSerializer
from .permissions import CustomPermission


class UserView(APIView):
    def get_permissions(self):
        if self.request.method == 'POST':
            permission_classes = (AllowAny, )
        else:
            permission_classes = (IsAdminUser, )

        return [permission() for permission in permission_classes]

    def get(self, request):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            # TODO: "serializer.validated['profile']" returns an instance of
            # InMemoryUploadedFile which raises an I/0 error when passed to Response
            # (i.e it is not JSON serializable )
            # This why we remove it and add the file's name manually.
            profile = serializer.validated_data.pop('profile')

            data = serializer.validated_data
            data['profile'] = profile.name
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):

    permission_classes = (CustomPermission, )

    def get_object(self, pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404
        self.check_object_permissions(self.request, user)
        return user

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def delete(self, request, pk):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
