from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from django.urls import path

urlpatterns = [
                  path('', views.index, name='home'),
                  path('about/', views.about, name='about'),
                  path('profile/', views.profile, name='profile'),
                  path('earthMoon/', views.earthMoon, name='earthMoon'),
                  path('marsMoon/', views.marsMoon, name='marsMoon'),
                  path('mars_moon1/', views.mars_moon1, name='mars_moon1'),
                  path('mars_moon2/', views.mars_moon2, name='mars_moon2'),
                  path('jupitarMoon/', views.jupitarMoon, name='jupitarMoon'),
                  path('jupitarMoon1/', views.jupitarMoon1, name='jupitarMoon1'),
                  path('jupitarMoon2/', views.jupitarMoon2, name='jupitarMoon2'),
                  path('jupitarMoon3/', views.jupitarMoon3, name='jupitarMoon3'),
                  path('jupitarMoon4/', views.jupitarMoon4, name='jupitarMoon4'),
                  path('jupitarMoon5/', views.jupitarMoon5, name='jupitarMoon5'),
                  path('saturnMoon/', views.saturnMoon, name='saturnMoon'),
                  path('saturnMoon1/', views.saturnMoon1, name='saturnMoon1'),
                  path('saturnMoon2/', views.saturnMoon2, name='saturnMoon2'),
                  path('saturnMoon3/', views.saturnMoon3, name='saturnMoon3'),
                  path('saturnMoon4/', views.saturnMoon4, name='saturnMoon4'),
                  path('saturnMoon5/', views.saturnMoon5, name='saturnMoon5'),
                  path('uranusMoon/', views.uranusMoon, name='uranusMoon'),
                  path('uranusMoon1/', views.uranusMoon1, name='uranusMoon1'),
                  path('uranusMoon2/', views.uranusMoon2, name='uranusMoon2'),
                  path('uranusMoon3/', views.uranusMoon3, name='uranusMoon3'),
                  path('uranusMoon4/', views.uranusMoon4, name='uranusMoon4'),
                  path('uranusMoon5/', views.uranusMoon5, name='uranusMoon5'),
                  path('neptuneMoon/', views.neptuneMoon, name='neptuneMoon'),
                  path('neptuneMoon1/', views.neptuneMoon1, name='neptuneMoon1'),
                  path('neptuneMoon2/', views.neptuneMoon2, name='neptuneMoon2'),
                  path('neptuneMoon3/', views.neptuneMoon3, name='neptuneMoon3'),
                  path('neptuneMoon4/', views.neptuneMoon4, name='neptuneMoon4'),
                  path('neptuneMoon5/', views.neptuneMoon5, name='neptuneMoon5'),

                  path('topics/', views.topics, name='topics'),
                  path('post_form/', views.post_form, name='post_form'),
                  path('library/', views.library, name='library'),
                  path('countdown/', views.countdown, name='countdown'),

                  path('downtopics/<int:file>', views.downtopics, name='downtopics'),
                  path('post_submitted/', views.post_submitted, name='post_submitted'),
                  path('message_submitted/', views.message_submitted, name='message_submitted'),

                  path('events/', views.events, name='events'),
                  path('telescope/', views.telescope, name='telescope'),
                  path('contact/', views.contact, name='contact'),
                  path('blog/', views.blog, name='blog'),

                  path('signup/', views.signup, name='signup'),
                  path('login/', views.loginPage, name='login'),
                  path('logout/', views.logoutUser, name="logout"),
                  path('singlepost/', views.singlepost, name='singlepost'),
                  path('blogs/<int:article_id>/', views.detail, name='detail'),
                  path('nasa/<int:nasaNew_id>/', views.detail1, name='detail1'),
                  path('singlepost1/', views.singlepost, name='singlepost1'),
                  path('nasa/', views.nasa, name='nasa'),
                  path('planets', views.planets, name='planets'),
                  path('mercury/', views.mercury, name='mercury'),
                  path('venus/', views.venus, name='venus'),
                  path('earth/', views.earth, name='earth'),
                  path('mars/', views.mars, name='mars'),
                  path('jupiter', views.jupiter, name='jupiter'),
                  path('saturn', views.saturn, name='saturn'),
                  path('uranus', views.uranus, name='uranus'),
                  path('neptune', views.neptune, name='neptune'),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,
                                                                                           document_root=settings.MEDIA_ROOT)
