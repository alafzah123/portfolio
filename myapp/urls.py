from django.urls import path
from .views import ClientListView, ProjectListView, TestimonialListView,EnquiryView,QuotationView,AboutDataView,HomeDataView

urlpatterns = [
    path('clients/', ClientListView.as_view(), name='client-list'),
    path('projects/', ProjectListView.as_view(), name='project-list'),
    path('testimonials/', TestimonialListView.as_view(), name='testimonial-list'),
    path('enquiry/', EnquiryView.as_view(), name='testimonial-list'),
    path('quotation/', QuotationView.as_view(), name='testimonial-list'),
    path('home-data/', HomeDataView.as_view(), name='home-data'),
    path('about-data/', AboutDataView.as_view(), name='about-data'),
]
