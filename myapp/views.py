import traceback
from rest_framework import generics
from .models import Client, Project, Testimonial
from .serializers import ClientSerializer, ProjectSerializer,  TestimonialSerializer
from .serializers import EnquirySerializer, QuotationSerializer
from django.core.mail import send_mail
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

class ClientListView(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({
            'request': self.request
        })
        return context

class ProjectListView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({
            'request': self.request
        })
        return context

class TestimonialListView(generics.ListAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({
            'request': self.request
        })
        return context

class HomeDataView(APIView):
    def get(self, request, *args, **kwargs):
        projects = ProjectSerializer(Project.objects.all(), many=True, context={'request': request}).data
        testimonials = TestimonialSerializer(Testimonial.objects.all(), many=True, context={'request': request}).data
        return Response({
            'projects': projects,
            'testimonials': testimonials
        })

class AboutDataView(APIView):
    def get(self, request, *args, **kwargs):
        testimonials = TestimonialSerializer(Testimonial.objects.all(), many=True, context={'request': request}).data
        clients = ClientSerializer(Client.objects.all(), many=True, context={'request': request}).data
        return Response({
            'testimonials': testimonials,
            'clients': clients
        })


class EnquiryView(APIView):
    def post(self, request):
        try:
            serializer = EnquirySerializer(data=request.data)
            logo_image = request.build_absolute_uri('/media/logo.png')
            print(logo_image)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                name = serializer.validated_data['name']
                email = serializer.validated_data['email']
                subject = serializer.validated_data['subject']
                message = serializer.validated_data['message']
                from_email = settings.DEFAULT_FROM_EMAIL
                to_email = email

                html_message = render_to_string(
                    'emails/enquiry_email.html',
                    {
                        'logo_url':logo_image,
                        'title':"Enquiry",
                        'subtitle':"enquiry",
                        'name': name,
                        'email': email,
                        'subject': subject,
                        'message': message,
                    }
                )

                # Construct email content
                email = EmailMessage(subject, html_message, from_email, [to_email])
                email.content_subtype = 'html'
                
                try:
                    email.send()
                    return Response({"message": "Enquiry email sent successfully!"}, status=status.HTTP_200_OK)
                except Exception as e:
                    # Log the exception or handle it as needed
                    return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            traceback.print_exc()
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class QuotationView(APIView):
    def post(self, request):
        try:
            serializer = QuotationSerializer(data=request.data)
            logo_image = request.build_absolute_uri('/media/logo.png')
            print(logo_image)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                name = serializer.validated_data['name']
                email = serializer.validated_data['email']
                number = serializer.validated_data['phone']
                message = serializer.validated_data['message']

                subject = 'New Quotation Submission'
                from_email = settings.DEFAULT_FROM_EMAIL
                to_email = email

                html_message = render_to_string(
                    'emails/quotation.html',
                    {
                        'logo_url':logo_image,
                        'title':"Quotation",
                        'subtitle':"quotation",
                        'name': name,
                        'email': email,
                        'subject': number,
                        'message': message,
                    }
                )

                email = EmailMessage(subject, html_message, from_email, [to_email])
                email.content_subtype = 'html'
                
                try:
                    email.send()
                    return Response({"message": "Contact email sent successfully!"}, status=status.HTTP_200_OK)
                except Exception as e:
                    # Log the exception or handle it as needed
                    return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)



