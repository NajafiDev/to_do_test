from rest_framework import serializers
from .models import Customer

class CustomerSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    #first_name = serializers.CharField(max_length=255)
    #last_name = serializers.CharField(max_length=255)
    email = serializers.EmailField()
    customer_name = serializers.SerializerMethodField(method_name='full_name')
    
    def full_name(self, customer: Customer):
        return f'{customer.first_name} {customer.last_name}'
    
class TaskSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    description = serializers.CharField()
    created_at = serializers.DateTimeField()
    customer = CustomerSerializer()