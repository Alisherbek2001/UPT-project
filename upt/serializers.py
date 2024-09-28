from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    
    class Meta:
        model = Category
        fields = ['id','title','created_at','updated_at']
    
    def get_title(self, obj):
        return {
            'uz': obj.title_uz,
            'ru': obj.title_ru,
            'en': obj.title_en
        }

class ProjectsSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    category = CategorySerializer(many=False)
    
    class Meta:
        model = Project
        fields = ['id','title','photo','category','link','is_main','created_at','updated_at']
    
    def get_title(self, obj):
        return {
            'uz': obj.title_uz,
            'ru': obj.title_ru,
            'en': obj.title_en
        }
    
    def get_photo_url(self,obj):
        request = self.context.get('request')
        if obj.photo:
            return request.build_absolute_uri(obj.photo.url)
        return None


class FeedbackSerializer(serializers.ModelSerializer):
    text = serializers.SerializerMethodField()
    author = serializers.SerializerMethodField()
    
    class Meta:
        model = Feedback
        fields = ['id','text','author','created_at','updated_at']
        
    def get_text(self, obj):
        return {
            'uz': obj.text_uz,
            'ru': obj.text_ru,
            'en': obj.text_en
        }
        
    def get_author(self, obj):
        return {
            'uz': obj.author_uz,
            'ru': obj.author_ru,
            'en': obj.author_en
        }
        
class MemberSerializer(serializers.ModelSerializer):
    fullname = serializers.SerializerMethodField()
    position = serializers.SerializerMethodField()
    
    class Meta:
        model = Member
        fields = ['id','fullname','photo','position','created_at','updated_at']
        
    def get_fullname(self, obj):
        return {
            'uz': obj.fullname_uz,
            'ru': obj.fullname_ru,
            'en': obj.fullname_en
        }
            
    def get_photo_url(self,obj):
        request = self.context.get('request')
        if obj.photo:
            return request.build_absolute_uri(obj.photo.url)
        return None
    
    def get_position(self, obj):
        return {
            'uz': obj.position_uz,
            'ru': obj.position_ru,
            'en': obj.position_en
        }


class ProjectsPageSerializer(serializers.Serializer):
    projects = ProjectsSerializer(many=True)
    feedback = FeedbackSerializer(many=True)