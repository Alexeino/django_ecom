from django.shortcuts import render
from rest_framework import views, permissions, response
from accounts.api.serializers import UserSerializer

# Create your views here.
class UserAccountsAV(views.APIView):
    """
    This view is to register general customer account.
    Permission boundary is None. Any new user can create account.

    """

    def post(self,request):
        
        """View to create a customer account.
        This view is supposed to create Non-Staff general customer at all times.
        
        To make role choices uncomment "if role" lines but it may create integrity & security issue.

        Returns:
            _type_: CustomUser | role = "CUSTOMER" always
        """
    
        # if 'role' not in request.data:
        #     request.data['role'] = 'CUST'

        print("Modified data - ",request.data)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data)
        else:
            return response.Response(serializer.errors)