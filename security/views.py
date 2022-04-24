# from rest_framework import generics, permissions
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.authtoken.models import Token
# from .serializers import LoginSerializer, UserSerializer, RegisterSerializer
# from rest_framework.permissions import IsAuthenticated

# class RegisterView(generics.GenericAPIView):
#     serializer_class = RegisterSerializer
    
#     def post(self,request,*args,**kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()
#         return Response({
#             'user': UserSerializer(
#                 user,
#                 context = self.get_serializer_context()
#             ).data
#         })
# class LoginView(generics.GenericAPIView):
#     serializer_class = LoginSerializer
#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data
#         return Response({
#             'user': UserSerializer(
#                 user,
#                 context = self.get_serializer_context()
#             ).data,
#             'token': Token.objects.create(user=user).key
#         })

# class UserView(generics.RetrieveAPIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = UserSerializer

#     def get_object(self):
#         return self.request.user

# class LogoutView(APIView):
#     def get(self, request, format=None):
#         request.user.auth_token.delete()
#         return Response(status=status.HTTP_200_OK)
