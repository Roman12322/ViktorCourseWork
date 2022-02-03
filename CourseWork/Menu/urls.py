from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.registration),
    path('form', views.form),
    path('Results', views.results),
    path('registration', views.registration),
    path('SignUp', views.SignUp),
    path('calculate', views.calculate),
    path('checkResults', views.checkResults),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
