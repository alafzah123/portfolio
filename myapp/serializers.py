from rest_framework import serializers
from .models import Client, Project, ImageMedia, Testimonial,Enquiry,Quotation

class ClientSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    class Meta:
        model = Client
        fields = ('image_url',)
    def get_image_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return obj.image.url
        return request.build_absolute_uri(obj.image.url)

class ImageMediaSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    class Meta:
        model = ImageMedia
        fields = ('image_url',)
    def get_image_url(self, obj):
        request = self.context.get('request')
        print(request)
        if request is None:
            return obj.image.url
        print(obj.image.url)
        return request.build_absolute_uri(obj.image.url)
class ProjectSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()  # Include related images
    class Meta:
        model = Project
        fields = ('title','images',)
    def get_images(self,instance):
        images = instance.images.all()
        if images:
            return ImageMediaSerializer(images,many=True,context=self.context).data
        return [{'image_url':"https://img.freepik.com/premium-vector/illustration-vector-graphic-cartoon-character-connected_516790-223.jpg?w=740"}]
class TestimonialSerializer(serializers.ModelSerializer):
    profile_image_url = serializers.SerializerMethodField()
    class Meta:
        model = Testimonial
        fields =('name','rating','position','review','profile_image_url',)
    def get_profile_image_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return obj.image.url
        return request.build_absolute_uri(obj.profile_image.url)
    

class EnquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Enquiry
        fields = '__all__'
class QuotationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quotation
        fields = '__all__'