from django.shortcuts import render
from .models import languagecont, example, usage, about, contact


# views


def wiki_list(request):
    pythonobj = languagecont.objects.filter(pk=1)
    cplusplusobj = languagecont.objects.filter(pk=2)
    javaobj = languagecont.objects.filter(pk=3)
    sqlobj = languagecont.objects.filter(pk=4)
    webobj = languagecont.objects.filter(pk=5)
    homeobj = languagecont.objects.filter(pk=6)
    return render(request, 'wiki/index.html', {'python': pythonobj, 'cplusplus': cplusplusobj,
                                               'java': javaobj, 'sql': sqlobj, 'web': webobj, 'home': homeobj})


def wiki_liste(request):
    pythonobj = languagecont.objects.filter(pk=1)
    cplusplusobj = languagecont.objects.filter(pk=2)
    javaobj = languagecont.objects.filter(pk=3)
    sqlobj = languagecont.objects.filter(pk=4)
    webobj = languagecont.objects.filter(pk=5)
    homeobj = languagecont.objects.filter(pk=6)
    exampleobj = example.objects.filter(pk=8)
    usageobj = usage.objects.filter(pk=8)
    return render(request, 'wiki/indexe.html', {'python': pythonobj, 'cplusplus': cplusplusobj,
                                                'java': javaobj, 'sql': sqlobj, 'web': webobj, 'home': homeobj,
                                                'usage': usageobj, 'example': exampleobj})


def wiki_listu(request):
    pythonobj = languagecont.objects.filter(pk=1)
    cplusplusobj = languagecont.objects.filter(pk=2)
    javaobj = languagecont.objects.filter(pk=3)
    sqlobj = languagecont.objects.filter(pk=4)
    webobj = languagecont.objects.filter(pk=5)
    homeobj = languagecont.objects.filter(pk=6)
    exampleobj = example.objects.filter(pk=8)
    usageobj = usage.objects.filter(pk=8)
    htmlobj = languagecont.objects.filter(pk=7)
    programmingobj = languagecont.objects.filter(pk=10)
    return render(request, 'wiki/indexu.html', {'python': pythonobj, 'cplusplus': cplusplusobj,
                                                'java': javaobj, 'sql': sqlobj, 'web': webobj, 'home': homeobj,
                                                'usage': usageobj, 'example': exampleobj, 'html': htmlobj, 'pro': programmingobj})


# python views

def Pythonwiki_list(request):
    pythonobj = languagecont.objects.filter(pk=1)
    cplusplusobj = languagecont.objects.filter(pk=2)
    javaobj = languagecont.objects.filter(pk=3)
    sqlobj = languagecont.objects.filter(pk=4)
    webobj = languagecont.objects.filter(pk=5)
    homeobj = languagecont.objects.filter(pk=6)
    exampleobj = example.objects.filter(pk=1)
    return render(request, 'wiki/Python.html', {'python': pythonobj, 'cplusplus': cplusplusobj,
                                                'java': javaobj, 'sql': sqlobj, 'web': webobj,
                                                'home': homeobj, 'example': exampleobj})


def Pythonwiki_liste(request):
    pythonobj = languagecont.objects.filter(pk=1)
    cplusplusobj = languagecont.objects.filter(pk=2)
    javaobj = languagecont.objects.filter(pk=3)
    sqlobj = languagecont.objects.filter(pk=4)
    webobj = languagecont.objects.filter(pk=5)
    homeobj = languagecont.objects.filter(pk=6)
    exampleobj = example.objects.filter(pk=1)
    return render(request, 'wiki/Pythone.html', {'python': pythonobj, 'cplusplus': cplusplusobj,
                                                 'java': javaobj, 'sql': sqlobj, 'web': webobj,
                                                 'home': homeobj, 'example': exampleobj})


def Pythonwiki_listu(request):
    pythonobj = languagecont.objects.filter(pk=1)
    cplusplusobj = languagecont.objects.filter(pk=2)
    javaobj = languagecont.objects.filter(pk=3)
    sqlobj = languagecont.objects.filter(pk=4)
    webobj = languagecont.objects.filter(pk=5)
    homeobj = languagecont.objects.filter(pk=6)
    exampleobj = example.objects.filter(pk=1)
    usageobj = usage.objects.filter(pk=1)
    return render(request, 'wiki/Pythonu.html', {'python': pythonobj, 'cplusplus': cplusplusobj,
                                                 'java': javaobj, 'sql': sqlobj, 'web': webobj,
                                                 'home': homeobj, 'example': exampleobj, 'usage': usageobj})


# c++ views

def Cpluspluswiki_list(request):
    pythonobj = languagecont.objects.filter(pk=1)
    cplusplusobj = languagecont.objects.filter(pk=2)
    javaobj = languagecont.objects.filter(pk=3)
    sqlobj = languagecont.objects.filter(pk=4)
    webobj = languagecont.objects.filter(pk=5)
    homeobj = languagecont.objects.filter(pk=6)
    exampleobj = example.objects.filter(pk=2)
    return render(request, 'wiki/Cplusplus.html', {'python': pythonobj, 'cplusplus': cplusplusobj,
                                                   'java': javaobj, 'sql': sqlobj, 'web': webobj,
                                                   'home': homeobj, 'example': exampleobj})


def Cpluspluswiki_liste(request):
    pythonobj = languagecont.objects.filter(pk=1)
    cplusplusobj = languagecont.objects.filter(pk=2)
    javaobj = languagecont.objects.filter(pk=3)
    sqlobj = languagecont.objects.filter(pk=4)
    webobj = languagecont.objects.filter(pk=5)
    homeobj = languagecont.objects.filter(pk=6)
    exampleobj = example.objects.filter(pk=2)
    return render(request, 'wiki/Cpluspluse.html', {'python': pythonobj, 'cplusplus': cplusplusobj,
                                                    'java': javaobj, 'sql': sqlobj, 'web': webobj,
                                                    'home': homeobj, 'example': exampleobj})


def Cpluspluswiki_listu(request):
    pythonobj = languagecont.objects.filter(pk=1)
    cplusplusobj = languagecont.objects.filter(pk=2)
    javaobj = languagecont.objects.filter(pk=3)
    sqlobj = languagecont.objects.filter(pk=4)
    webobj = languagecont.objects.filter(pk=5)
    homeobj = languagecont.objects.filter(pk=6)
    exampleobj = example.objects.filter(pk=2)
    usageobj = usage.objects.filter(pk=2)
    return render(request, 'wiki/Cplusplusu.html', {'python': pythonobj, 'cplusplus': cplusplusobj,
                                                    'java': javaobj, 'sql': sqlobj, 'web': webobj,
                                                    'home': homeobj, 'example': exampleobj, 'usage': usageobj})


# java views

def Javawiki_list(request):
    pythonobj = languagecont.objects.filter(pk=1)
    cplusplusobj = languagecont.objects.filter(pk=2)
    javaobj = languagecont.objects.filter(pk=3)
    sqlobj = languagecont.objects.filter(pk=4)
    webobj = languagecont.objects.filter(pk=5)
    homeobj = languagecont.objects.filter(pk=6)
    exampleobj = example.objects.filter(pk=3)
    return render(request, 'wiki/Java.html', {'python': pythonobj, 'cplusplus': cplusplusobj,
                                              'java': javaobj, 'sql': sqlobj, 'web': webobj, 'home':
                                                  homeobj, 'example': exampleobj})


def Javawiki_liste(request):
    pythonobj = languagecont.objects.filter(pk=1)
    cplusplusobj = languagecont.objects.filter(pk=2)
    javaobj = languagecont.objects.filter(pk=3)
    sqlobj = languagecont.objects.filter(pk=4)
    webobj = languagecont.objects.filter(pk=5)
    homeobj = languagecont.objects.filter(pk=6)
    exampleobj = example.objects.filter(pk=3)
    return render(request, 'wiki/Javae.html', {'python': pythonobj, 'cplusplus': cplusplusobj,
                                               'java': javaobj, 'sql': sqlobj, 'web': webobj, 'home':
                                                   homeobj, 'example': exampleobj})


def Javawiki_listu(request):
    pythonobj = languagecont.objects.filter(pk=1)
    cplusplusobj = languagecont.objects.filter(pk=2)
    javaobj = languagecont.objects.filter(pk=3)
    sqlobj = languagecont.objects.filter(pk=4)
    webobj = languagecont.objects.filter(pk=5)
    homeobj = languagecont.objects.filter(pk=6)
    exampleobj = example.objects.filter(pk=3)
    usageobj = usage.objects.filter(pk=3)
    return render(request, 'wiki/Javau.html', {'python': pythonobj, 'cplusplus': cplusplusobj,
                                               'java': javaobj, 'sql': sqlobj, 'web': webobj, 'home':
                                                   homeobj, 'example': exampleobj, 'usage': usageobj})


# sql views


def SQLwiki_list(request):
    pythonobj = languagecont.objects.filter(pk=1)
    cplusplusobj = languagecont.objects.filter(pk=2)
    javaobj = languagecont.objects.filter(pk=3)
    sqlobj = languagecont.objects.filter(pk=4)
    webobj = languagecont.objects.filter(pk=5)
    homeobj = languagecont.objects.filter(pk=6)
    exampleobj = example.objects.filter(pk=4)
    return render(request, 'wiki/SQL.html', {'python': pythonobj, 'cplusplus': cplusplusobj,
                                             'java': javaobj, 'sql': sqlobj, 'web': webobj,
                                             'home': homeobj, 'example': exampleobj})


def SQLwiki_liste(request):
    pythonobj = languagecont.objects.filter(pk=1)
    cplusplusobj = languagecont.objects.filter(pk=2)
    javaobj = languagecont.objects.filter(pk=3)
    sqlobj = languagecont.objects.filter(pk=4)
    webobj = languagecont.objects.filter(pk=5)
    homeobj = languagecont.objects.filter(pk=6)
    exampleobj = example.objects.filter(pk=4)
    return render(request, 'wiki/SQLe.html', {'python': pythonobj, 'cplusplus': cplusplusobj,
                                              'java': javaobj, 'sql': sqlobj, 'web': webobj,
                                              'home': homeobj, 'example': exampleobj})


def SQLwiki_listu(request):
    pythonobj = languagecont.objects.filter(pk=1)
    cplusplusobj = languagecont.objects.filter(pk=2)
    javaobj = languagecont.objects.filter(pk=3)
    sqlobj = languagecont.objects.filter(pk=4)
    webobj = languagecont.objects.filter(pk=5)
    homeobj = languagecont.objects.filter(pk=6)
    exampleobj = example.objects.filter(pk=4)
    usageobj = usage.objects.filter(pk=4)
    return render(request, 'wiki/SQLu.html', {'python': pythonobj, 'cplusplus': cplusplusobj,
                                              'java': javaobj, 'sql': sqlobj, 'web': webobj,
                                              'home': homeobj, 'example': exampleobj, 'usage': usageobj})


# web views

def HTMLwiki_list(request):
    pythonobj = languagecont.objects.filter(pk=1)
    cplusplusobj = languagecont.objects.filter(pk=2)
    javaobj = languagecont.objects.filter(pk=3)
    sqlobj = languagecont.objects.filter(pk=4)
    webobj = languagecont.objects.filter(pk=5)
    homeobj = languagecont.objects.filter(pk=6)
    htmlobj = languagecont.objects.filter(pk=7)
    cssobj = languagecont.objects.filter(pk=8)
    jsobj = languagecont.objects.filter(pk=9)
    exampleobj = example.objects.filter(pk=5)
    return render(request, 'wiki/HTML.html', {'python': pythonobj, 'cplusplus': cplusplusobj,
                                              'java': javaobj, 'sql': sqlobj, 'web': webobj, 'home': homeobj,
                                              'html': htmlobj, 'css': cssobj, 'js': jsobj, 'example': exampleobj})


def HTMLwiki_liste(request):
    pythonobj = languagecont.objects.filter(pk=1)
    cplusplusobj = languagecont.objects.filter(pk=2)
    javaobj = languagecont.objects.filter(pk=3)
    sqlobj = languagecont.objects.filter(pk=4)
    webobj = languagecont.objects.filter(pk=5)
    homeobj = languagecont.objects.filter(pk=6)
    htmlobj = languagecont.objects.filter(pk=7)
    cssobj = languagecont.objects.filter(pk=8)
    jsobj = languagecont.objects.filter(pk=9)
    exampleobj = example.objects.filter(pk=5)
    return render(request, 'wiki/HTMLe.html', {'python': pythonobj, 'cplusplus': cplusplusobj,
                                               'java': javaobj, 'sql': sqlobj, 'web': webobj, 'home': homeobj,
                                               'html': htmlobj, 'css': cssobj, 'js': jsobj, 'example': exampleobj})


def HTMLwiki_listu(request):
    pythonobj = languagecont.objects.filter(pk=1)
    cplusplusobj = languagecont.objects.filter(pk=2)
    javaobj = languagecont.objects.filter(pk=3)
    sqlobj = languagecont.objects.filter(pk=4)
    webobj = languagecont.objects.filter(pk=5)
    homeobj = languagecont.objects.filter(pk=6)
    htmlobj = languagecont.objects.filter(pk=7)
    cssobj = languagecont.objects.filter(pk=8)
    jsobj = languagecont.objects.filter(pk=9)
    exampleobj = example.objects.filter(pk=5)
    usageobj = usage.objects.filter(pk=5)
    return render(request, 'wiki/HTMLu.html', {'python': pythonobj, 'cplusplus': cplusplusobj,
                                               'java': javaobj, 'sql': sqlobj, 'web': webobj, 'home': homeobj,
                                               'html': htmlobj, 'css': cssobj, 'js': jsobj, 'example': exampleobj,
                                               'usage': usageobj})


def CSSwiki_list(request):
    pythonobj = languagecont.objects.filter(pk=1)
    cplusplusobj = languagecont.objects.filter(pk=2)
    javaobj = languagecont.objects.filter(pk=3)
    sqlobj = languagecont.objects.filter(pk=4)
    webobj = languagecont.objects.filter(pk=5)
    homeobj = languagecont.objects.filter(pk=6)
    htmlobj = languagecont.objects.filter(pk=7)
    cssobj = languagecont.objects.filter(pk=8)
    jsobj = languagecont.objects.filter(pk=9)
    exampleobj = example.objects.filter(pk=6)
    return render(request, 'wiki/CSS.html', {'python': pythonobj, 'cplusplus': cplusplusobj,
                                             'java': javaobj, 'sql': sqlobj, 'web': webobj, 'home': homeobj,
                                             'html': htmlobj, 'css': cssobj, 'js': jsobj, 'example': exampleobj})


def CSSwiki_liste(request):
    pythonobj = languagecont.objects.filter(pk=1)
    cplusplusobj = languagecont.objects.filter(pk=2)
    javaobj = languagecont.objects.filter(pk=3)
    sqlobj = languagecont.objects.filter(pk=4)
    webobj = languagecont.objects.filter(pk=5)
    homeobj = languagecont.objects.filter(pk=6)
    htmlobj = languagecont.objects.filter(pk=7)
    cssobj = languagecont.objects.filter(pk=8)
    jsobj = languagecont.objects.filter(pk=9)
    exampleobj = example.objects.filter(pk=6)
    return render(request, 'wiki/CSSe.html', {'python': pythonobj, 'cplusplus': cplusplusobj,
                                              'java': javaobj, 'sql': sqlobj, 'web': webobj, 'home': homeobj,
                                              'html': htmlobj, 'css': cssobj, 'js': jsobj, 'example': exampleobj})


def CSSwiki_listu(request):
    pythonobj = languagecont.objects.filter(pk=1)
    cplusplusobj = languagecont.objects.filter(pk=2)
    javaobj = languagecont.objects.filter(pk=3)
    sqlobj = languagecont.objects.filter(pk=4)
    webobj = languagecont.objects.filter(pk=5)
    homeobj = languagecont.objects.filter(pk=6)
    htmlobj = languagecont.objects.filter(pk=7)
    cssobj = languagecont.objects.filter(pk=8)
    jsobj = languagecont.objects.filter(pk=9)
    exampleobj = example.objects.filter(pk=6)
    usageobj = usage.objects.filter(pk=6)
    return render(request, 'wiki/CSSu.html', {'python': pythonobj, 'cplusplus': cplusplusobj,
                                              'java': javaobj, 'sql': sqlobj, 'web': webobj, 'home': homeobj,
                                              'html': htmlobj, 'css': cssobj, 'js': jsobj, 'example': exampleobj,
                                              'usage': usageobj})


def JSwiki_list(request):
    pythonobj = languagecont.objects.filter(pk=1)
    cplusplusobj = languagecont.objects.filter(pk=2)
    javaobj = languagecont.objects.filter(pk=3)
    sqlobj = languagecont.objects.filter(pk=4)
    webobj = languagecont.objects.filter(pk=5)
    homeobj = languagecont.objects.filter(pk=6)
    htmlobj = languagecont.objects.filter(pk=7)
    cssobj = languagecont.objects.filter(pk=8)
    jsobj = languagecont.objects.filter(pk=9)
    exampleobj = example.objects.filter(pk=7)
    return render(request, 'wiki/JS.html', {'python': pythonobj, 'cplusplus': cplusplusobj,
                                            'java': javaobj, 'sql': sqlobj, 'web': webobj, 'home': homeobj,
                                            'html': htmlobj, 'css': cssobj, 'js': jsobj, 'example': exampleobj})


def JSwiki_liste(request):
    pythonobj = languagecont.objects.filter(pk=1)
    cplusplusobj = languagecont.objects.filter(pk=2)
    javaobj = languagecont.objects.filter(pk=3)
    sqlobj = languagecont.objects.filter(pk=4)
    webobj = languagecont.objects.filter(pk=5)
    homeobj = languagecont.objects.filter(pk=6)
    htmlobj = languagecont.objects.filter(pk=7)
    cssobj = languagecont.objects.filter(pk=8)
    jsobj = languagecont.objects.filter(pk=9)
    exampleobj = example.objects.filter(pk=7)
    return render(request, 'wiki/JSe.html', {'python': pythonobj, 'cplusplus': cplusplusobj,
                                             'java': javaobj, 'sql': sqlobj, 'web': webobj, 'home': homeobj,
                                             'html': htmlobj, 'css': cssobj, 'js': jsobj, 'example': exampleobj})


def JSwiki_listu(request):
    pythonobj = languagecont.objects.filter(pk=1)
    cplusplusobj = languagecont.objects.filter(pk=2)
    javaobj = languagecont.objects.filter(pk=3)
    sqlobj = languagecont.objects.filter(pk=4)
    webobj = languagecont.objects.filter(pk=5)
    homeobj = languagecont.objects.filter(pk=6)
    htmlobj = languagecont.objects.filter(pk=7)
    cssobj = languagecont.objects.filter(pk=8)
    jsobj = languagecont.objects.filter(pk=9)
    exampleobj = example.objects.filter(pk=7)
    usageobj = usage.objects.filter(pk=7)
    return render(request, 'wiki/JSu.html', {'python': pythonobj, 'cplusplus': cplusplusobj,
                                             'java': javaobj, 'sql': sqlobj, 'web': webobj, 'home': homeobj,
                                             'html': htmlobj, 'css': cssobj, 'js': jsobj, 'example': exampleobj,
                                             'usage': usageobj})


def Webwiki_list(request):
    pythonobj = languagecont.objects.filter(pk=1)
    cplusplusobj = languagecont.objects.filter(pk=2)
    javaobj = languagecont.objects.filter(pk=3)
    sqlobj = languagecont.objects.filter(pk=4)
    webobj = languagecont.objects.filter(pk=5)
    homeobj = languagecont.objects.filter(pk=6)
    htmlobj = languagecont.objects.filter(pk=7)
    cssobj = languagecont.objects.filter(pk=8)
    jsobj = languagecont.objects.filter(pk=9)
    return render(request, 'wiki/Web.html', {'python': pythonobj, 'cplusplus': cplusplusobj,
                                             'java': javaobj, 'sql': sqlobj, 'web': webobj, 'home': homeobj,
                                             'html': htmlobj, 'css': cssobj, 'js': jsobj})


def about_list(request):
    pythonobj = languagecont.objects.filter(pk=1)
    cplusplusobj = languagecont.objects.filter(pk=2)
    javaobj = languagecont.objects.filter(pk=3)
    sqlobj = languagecont.objects.filter(pk=4)
    webobj = languagecont.objects.filter(pk=5)
    homeobj = languagecont.objects.filter(pk=6)
    htmlobj = languagecont.objects.filter(pk=7)
    cssobj = languagecont.objects.filter(pk=8)
    jsobj = languagecont.objects.filter(pk=9)
    exampleobj = example.objects.filter(pk=7)
    usageobj = usage.objects.filter(pk=7)
    aboutobj = about.objects.filter(pk=1)
    return render(request, 'wiki/about.html', {'python': pythonobj, 'cplusplus': cplusplusobj,
                                               'java': javaobj, 'sql': sqlobj, 'web': webobj, 'home': homeobj,
                                               'html': htmlobj, 'css': cssobj, 'js': jsobj, 'example': exampleobj,
                                               'usage': usageobj, 'about': aboutobj})


def contact_list(request):
    pythonobj = languagecont.objects.filter(pk=1)
    cplusplusobj = languagecont.objects.filter(pk=2)
    javaobj = languagecont.objects.filter(pk=3)
    sqlobj = languagecont.objects.filter(pk=4)
    webobj = languagecont.objects.filter(pk=5)
    homeobj = languagecont.objects.filter(pk=6)
    htmlobj = languagecont.objects.filter(pk=7)
    cssobj = languagecont.objects.filter(pk=8)
    jsobj = languagecont.objects.filter(pk=9)
    exampleobj = example.objects.filter(pk=7)
    usageobj = usage.objects.filter(pk=7)
    contactobj = contact.objects.filter(pk=1)
    return render(request, 'wiki/contact.html', {'python': pythonobj, 'cplusplus': cplusplusobj,
                                                 'java': javaobj, 'sql': sqlobj, 'web': webobj, 'home': homeobj,
                                                 'html': htmlobj, 'css': cssobj, 'js': jsobj, 'example': exampleobj,
                                                 'usage': usageobj, 'contact': contactobj})


def index_list(request):
    pythonobj = languagecont.objects.filter(pk=1)
    cplusplusobj = languagecont.objects.filter(pk=2)
    javaobj = languagecont.objects.filter(pk=3)
    sqlobj = languagecont.objects.filter(pk=4)
    webobj = languagecont.objects.filter(pk=5)
    homeobj = languagecont.objects.filter(pk=6)
    htmlobj = languagecont.objects.filter(pk=7)
    cssobj = languagecont.objects.filter(pk=8)
    jsobj = languagecont.objects.filter(pk=9)
    exampleobj = example.objects.filter(pk=7)
    usageobj = usage.objects.filter(pk=7)
    return render(request, 'wiki/indexindex.html', {'python': pythonobj, 'cplusplus': cplusplusobj,
                                                    'java': javaobj, 'sql': sqlobj, 'web': webobj, 'home': homeobj,
                                                    'html': htmlobj, 'css': cssobj, 'js': jsobj, 'example': exampleobj,
                                                    'usage': usageobj})
