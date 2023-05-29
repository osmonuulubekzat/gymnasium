from django.urls import path, include
from .views import *
urlpatterns = [
    path("", Forms, name="form"),
    path("make_pdf_page", Make_Pdf_Page, name="make_pdf_page"),
]
