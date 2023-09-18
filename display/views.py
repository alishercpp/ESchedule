from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.http import urlencode

def reverse_querystring(view, urlconf=None, args=None, kwargs=None, current_app=None, query_kwargs=None):
    '''Custom reverse to handle query strings.
    Usage:
        reverse('app.views.my_view', kwargs={'pk': 123}, query_kwargs={'search': 'Bob'})
    '''
    base_url = reverse(view, urlconf=urlconf, args=args, kwargs=kwargs, current_app=current_app)
    if query_kwargs:
        return '{}?{}'.format(base_url, urlencode(query_kwargs))
    return base_url


def home(request):
    error = None
    if request.method == 'POST':
        pid = request.POST.get('pid')
        try:
            pupil = Pupil.objects.get(pid=pid)
            return HttpResponseRedirect(reverse_querystring('class', kwargs={'cid': pupil.klass.cid}, query_kwargs={'pid': pupil.pid}))
        except:
            error = "O'quvchi topilmadi!"
    return render(request, 'home.html', {
        'schools': School.objects.all(),
        "error": error
    })

def school(request, sid):
    school = School.objects.get(sid=sid)
    if school:
        return render(request, 'school.html', {
            'school': school,
            'classes': Class.objects.filter(school=school)
        })
    else:
        return render(request, '404.html')
    
def klass(request, cid):
    klass = Class.objects.get(cid=cid)
    pid = request.GET.get('pid')
    if klass:
        return render(request, 'class.html', {
            'class': klass,
            'subjects': Subject.objects.filter(klass=klass),
            "ppid": pid
        })
    else:
        return render(request, '404.html')

def subject(request, sbid):
    pid = None
    from datetime import datetime
    subject = Subject.objects.get(sbid=sbid)
    if subject:
        if request.GET.get('pid'):
            pid = request.GET.get("pid")
        return render(request, 'subject.html', {
            'subject': subject,
            'grade': Grade.objects.filter(subject=subject).first(),
            "pid": pid,
            "pupils": Pupil.objects.filter(klass=subject.klass),
            "now": f"{datetime.now().day}/{datetime.now().month}/{datetime.now().year}"
        })
    else:
        return render(request, '404.html')
    
def save(request, sbid):
    if request.method == 'POST':
        print(request.POST)
        id = request.POST.get("id")
        grade = request.POST.get("grade")
        date = request.POST.get("date").replace(' ', '')
        b = Grade.objects.filter(subject__sbid=sbid).first()
        if b:
            b.grades[id][date] = grade
            b.save()
            try:
                if date not in b.dates.get("dates"):
                    b.dates.get("dates").append(date)
                    b.save()
            except Exception as e:
                print(e)
        import json
        print(json.dumps(str(b.grades), indent=True))
        return HttpResponseRedirect(reverse('subject', args=[sbid]))
    return HttpResponseRedirect(reverse('subject', args=[sbid]))
