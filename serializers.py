from rest_framework import serializers
from snippets.models import Snippets, LANGUAGE_CHOICES, STYLE_CHOICES

class SnippetSerializers(serializers.Serializer):
    id= serializers.IntegerField(read_only= True)
    title= serializers.CharField(required= False, allow_blank=True, max_length=100)
    code= serializers.CharField(style={'base_template', 'textareat.html'})
    lineous= serializers.BooleanField(required=False)
    language= serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style= serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    def create(self, validated_data):
      return Snippets.objects.create(**validated_data)

    def update(self,instance, validated_data):
       instance.title = validated_data.get('title', instance.title)
       instance.code= validated_data('code', instance.code)
       instance.lineous= validated_data('lineous', instance.lineous)
       instance.language= validated_data('language', instance.language)
       instance.style= validated_data('style', instance.style)
       instance.save
       return instance
