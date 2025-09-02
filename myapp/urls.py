from django.urls import path
from myapp.views import BlogGeneratorView

urlpatterns = [
    path('generate-blog/', BlogGeneratorView.as_view(), name='generate_blog'),
]
