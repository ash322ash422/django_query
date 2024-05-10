from rest_framework import serializers
from webapp.models import Query
from webapp.my_utils import dbg


class QuerySerializer(serializers.ModelSerializer):
    qry_name = serializers.CharField(max_length=100)

    def validate_qry_name(self, value): ##override. Invoked on CREATE,UPDATE
        dbg("inside QuerySerializer.validate_qry_name")
        if len(value) < 2:
           raise serializers.ValidationError("qry_name is too short")

        return value

    def create(self, validated_data):#override. Invoked on CREATE
        """
        Create and return a new `Query` instance, given the validated data.
        """
        dbg("inside QuerySerializer.create")
        return Query.objects.create(**validated_data)
    
    
    def update(self, instance, validated_data):
        dbg("inside QuerySerializer.update")
        dbg("validated_data=",validated_data)
        
        #for attr, value in validated_data.items():
        #   setattr(instance, attr, value)
        
        instance.save()
        
        # if instance.status == OrderStatus.COMPLETED:
        #     po_status_completed_signal.send(
        #         sender=instance.__class__, instance=instance
        #     )
        
        return instance
   
    class Meta:
        model = Query
        fields = ['qry_name','qry','create_by','create_on','last_accessed']
             