from django.shortcuts import render
from rest_framework.generics import ListAPIView,RetrieveAPIView,RetrieveUpdateAPIView,ListCreateAPIView,UpdateAPIView,DestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.db.models import Q
from .models import Customer,Activity,User
from .serializers import CustomerSerializer,ActivitySerializer,UserSerializer,ProfileSerializer

from django.db.models import Case,When,Value,IntegerField
from django.utils import timezone

class DashbordAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self,request):
        
        print("USER:", request.user)
        print("AUTH:", request.auth)

        data={
            "total":Customer.objects.filter(user=self.request.user).count(),
            "new":Customer.objects.filter(status="new",user=self.request.user).count(),
            "in_progress":Customer.objects.filter(status="in_progress",user=self.request.user).count(),
            "closed":Customer.objects.filter(status="closed",user=self.request.user).count(), 
            
        }
    
        return Response(data)



class CustomerListAPI(ListCreateAPIView):
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]
    
    
    def perform_create(self, serializer):
        serializer.save(
        user=self.request.user
    )
    
    def get_queryset(self):
        query_set = Customer.objects.filter(user=self.request.user)
        
        
        search = self.request.GET.get("search")
        
        if search:
            query_set = query_set.filter(Q(name__icontains=search) | Q(company__icontains=search))


        status = self.request.GET.get("status")
        
        if status:
            query_set = query_set.filter(status=status)
            
        
        sort = self.request.GET.get("sort")
        if sort == "updated_desc":
            query_set = query_set.order_by("-updated_at")
        elif sort == "updated_asc":
            query_set = query_set.order_by("updated_at")
        elif sort == "name_asc":
            query_set = query_set.order_by("name")
        elif sort == "overdue":
            # query_set = query_set.order_by("next_action_date")
            today = timezone.now().date()
            query_set = query_set.annotate(
                overdue_priority=Case(
                    When(
                        next_action_date__lt=today,
                        then=Value(0)
                    ),
                    When(
                        next_action_date__isnull=True,
                        then=Value(2)
                    ),
                    default=Value(1),
                    output_field=IntegerField(),
                )
                
            ).order_by("overdue_priority","next_action_date")
        return query_set.order_by('-created_at')
        
        
class CustomerDetailAPI(RetrieveAPIView):
    
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        
        return Customer.objects.filter(user=self.request.user)

class CustomerUpdateAPI(UpdateAPIView):
    
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
            
        return Customer.objects.filter(user=self.request.user)
    
    
class CustomerDeleteAPI(DestroyAPIView):
    
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
                
            return Customer.objects.filter(user=self.request.user)
    
    
class ActivityListAPI(ListAPIView):
    
    permission_classes = [IsAuthenticated]
    serializer_class = ActivitySerializer
    
    def get_queryset(self):
        return  Activity.objects.filter(customer__user = self.request.user)


class ActivityListCreateAPI(ListCreateAPIView):
    
    permission_classes = [IsAuthenticated]
    serializer_class = ActivitySerializer
    
    
    def perform_create(self, serializer):

        customer = Customer.objects.get(id=self.kwargs["pk"],user=self.request.user)
        
        serializer.save(
            customer = customer
        )
    
    def get_queryset(self):
    
        customer_id = self.kwargs["pk"]
        
        activity = Activity.objects.filter(customer_id=customer_id).order_by("-created_at")
        
        return activity.filter(customer__user = self.request.user)
        

class ActivityDetailAPI(RetrieveAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    
    lookup_url_kwarg = "activity_id"

class ActivityUpdateAPI(UpdateAPIView):
    
    queryset=Activity.objects.all()
    serializer_class=ActivitySerializer
    
    lookup_url_kwarg = "activity_id"

class ActivityDeleteAPI(DestroyAPIView):
    
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    lookup_url_kwarg = "activity_id"
    

class UserAPI(RetrieveAPIView):
    serializer_class = UserSerializer
    # permission_classes = [IsAuthenticated]
    
    def get_object(self):
        return self.request.user
    

class ProfileAPI(RetrieveUpdateAPIView):

    serializer_class=ProfileSerializer
    permission_classes = [IsAuthenticated]
    
    def get_object(self):
        return self.request.user.profile
    

# Create your views here.
