from django.urls import path

from . import views

urlpatterns = [

    # main

    path('', views.wiki_list, name='index'),
    path('Usage/', views.wiki_listu, name='usage'),
    path('Examples/', views.wiki_liste, name='examples'),
    path('About/', views.about_list, name='about'),
    path('Contact/', views.contact_list, name='contact'),
    path('Index', views.index_list, name='indexindex'),


    # programming


    path('Python/', views.Pythonwiki_list, name='Python'),
    path('Python/examples', views.Pythonwiki_liste, name='Pythonexamples'),
    path('Python/usage', views.Pythonwiki_listu, name='Pythonusage'),
    path('C++/', views.Cpluspluswiki_list, name='C++'),
    path('C++/examples', views.Cpluspluswiki_liste, name='C++examples'),
    path('c++/usage', views.Cpluspluswiki_listu, name='C++usage'),
    path('Java/', views.Javawiki_list, name='Java'),
    path('Java/examples', views.Javawiki_liste, name='Javaexamples'),
    path('Java/usage', views.Javawiki_listu, name='Javausage'),
    path('SQL/', views.SQLwiki_list, name='SQL'),
    path('SQL/examples', views.SQLwiki_liste, name='SQLexamples'),
    path('SQL/usage', views.SQLwiki_listu, name='SQLusage'),

    # web

    path('Web/', views.Webwiki_list, name='Web'),
    path('HTML/', views.HTMLwiki_list, name='Html'),
    path('HTML/examples', views.HTMLwiki_liste, name='Htmlexamples'),
    path('HTML/usage', views.HTMLwiki_listu, name='Htmlusage'),
    path('CSS/', views.CSSwiki_list, name='Css'),
    path('CSS/examples', views.CSSwiki_liste, name='Cssexamples'),
    path('CSS/usage', views.CSSwiki_listu, name='Cssusage'),
    path('JS/', views.JSwiki_list, name='Js'),
    path('JS/examples', views.JSwiki_liste, name='Jsexamples'),
    path('JS/usage', views.JSwiki_listu, name='Jsusage'),
]
