from django.urls import path
from app_1.views import *


urlpatterns = [
    path('index/', Index.as_view()),
    path(r'upload-doc/', UploadDoc.as_view()),
    path(r'', Login.as_view()),
    path(r'logout/', Logout.as_view()),
    path('registration/', Registration.as_view()),
]