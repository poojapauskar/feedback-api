from rest_framework import serializers
from set_feedback.models import Set_feedback

class Set_feedbackSerializer(serializers.ModelSerializer):

    class Meta:
        model = Set_feedback
        fields = ('pk','value')
        #write_only_fields = ('firstame', 'lastname')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        
        objects=Set_feedback.objects.create(value=validated_data.get('value'))
        return objects


   