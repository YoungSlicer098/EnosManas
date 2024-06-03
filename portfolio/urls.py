from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.deLeonAboutMe, name='aboutme'),
    path('check500/', views.check500, name='check500'),
    path('handler400/', views.handler400Viewable, name='handler400'),
    path('handler401/', views.handler401Viewable, name='handler401'),
    path('handler402/', views.handler402Viewable, name='handler402'),
    path('handler403/', views.handler403Viewable, name='handler403'),
    path('handler408/', views.handler408Viewable, name='handler408'),
]

handler400 = 'portfolio.views.handler400'
handler401 = 'portfolio.views.handler401'
handler402 = 'portfolio.views.handler402'
handler403 = 'portfolio.views.handler403'
handler404 = 'portfolio.views.handler404'
handler408 = 'portfolio.views.handler408'
handler500 = 'portfolio.views.handler500'