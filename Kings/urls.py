from django.contrib import admin
from django.urls import path
from Bakkery import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Homes, name='home'),
    path('AboutUS', views.Abouts, name='about'),  # Use 'about' as the name
    ##path('image_search/', views.image_search, name='image_search'),
    path('Lights1', views.Light, name='Light'),
    path('Cost1', views.Cost1, name='1'),
    path('Cost2', views.Cost2, name='2'),
    path('Cost3', views.Cost3, name='3'),
    path('Cost4', views.Cost4,  name='4'),
    path('Page1', views.Page, name='pag'),
    path('Chandle1', views.Chandle, name='Chandle'),
    path('Lamp1', views.Lamps, name='Lamp'),
    path('Hang1', views.Hang, name='hang'),
    path('Out1', views.Out, name='pag'),
    path('Bed1', views.Bed, name='Beds'),
    path('Almira1', views.Almira, name='Almira'),
    path('Stool1', views.Stool, name='Stool'),
    path('Swing1', views.Swing, name='Swing'),
    path('Chair1', views.Chair, name='Chair'),
    path('Pic1', views.Picture, name='Pic'),
    path('Wall1', views.Wall, name='wall'),
    path('Tasks1', views.Tasks, name='Tasks'),
    path('Table1', views.Table, name='Table'),
    path('Floor1', views.Floor1, name='Floor1'),
    path('Floor2', views.Floor2, name='Floor2'),
    path('Floor3', views.Floor3, name='Floor3'),
    path('Hang', views.Hang1, name='Hang1'),
    path('Hang2', views.Hang2, name='Hang2'),
    path('Hang3', views.Hang3, name='Hang3'),
    path('Out1', views.Out1, name='Out1'),
    path('Out2', views.Out2, name='Out2'),
    path('Out3', views.Out3, name='Out3'),
    path('Contact', views.Contact, name='Con'),
    path('Crouch1', views.Crouch, name='Crouch'),
    path('Blog', views.Blog, name='Blog'),
    path('Login1', views.Login, name='Log'),
    path('Ragister', views.Ragister, name='Ragister'),
        
     
    
            


]

# Correct the following line for serving media files
#if settings.DEBUG:
    #urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 