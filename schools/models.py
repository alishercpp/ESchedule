from django.db import models
from teachers.models import Teacher
from utils.generatos import generate
from django.db.models.signals import post_save
from django.dispatch import receiver

REGIONS = (
    ("Andijon", "Andijon"),
    ("Buxoro", "Buxoro"),
    ("Fargona", "Fargona"),
    ("Jizzax", "Jizzax"),
    ("Namangan", "Namangan"),
    ("Navoiy", "Navoiy"),
    ("Qashqadaryo", "Qashqadaryo"),
    ("Qoraqalpogiston", "Qoraqalpogiston"),
    ("Samarqand", "Samarqand"),
    ("Sirdaryo", "Sirdaryo"),
    ("Surxondaryo", "Surxondaryo"),
    ("Toshkent", "Toshkent"),
    ("Toshkent shahri", "Toshkent shahri"),
    ("Xorazm", "Xorazm")
)


class School(models.Model):
    sid         = models.CharField(max_length=20, default=generate, editable=False)
    director    = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    name        = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True, default="")
    region      = models.CharField(max_length=30, choices=REGIONS)
    town        = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
    def direktor(self):
        return {
            "id": self.director.pk,
            "username": self.director.username,
            "first_name": self.director.first_name,
            "last_name": self.director.last_name,
            "middle_name": self.director.middle_name
        }

    def classes(self):
        classes = Class.objects.filter(school=self)
        res = {}
        c = 1
        for klass in classes:
            res[c] = {
                "name": klass.name,
                "url": f"http://127.0.0.1:8000/classes/{klass.pk}/",
                "teacher": {
                    "id": klass.teacher.pk,
                    "username": klass.teacher.username,
                    "first_name": klass.teacher.first_name,
                    "last_name": klass.teacher.last_name,
                    "middle_name": klass.teacher.middle_name
                }
            }
            c += 1
        return res
    
    class Meta:
        verbose_name_plural = "Maktablar"
    

class Class(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    school  = models.ForeignKey(School, on_delete=models.CASCADE)
    name    = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
    def schedule(self):
        s = Schedule.objects.get(klass=self)
        if s:
            return s.schedule()
        return None
    
    def subjects(self):
        subjects = Subject.objects.filter(klass=self)
        res = {}
        c = 1
        for subject in subjects:
            res[c] = {
                "id": subject.pk,
                "name": subject.name,
                "teacher": {
                    "id": subject.teacher.pk,
                    "username": subject.teacher.username,
                    "first_name": subject.teacher.first_name,
                    "last_name": subject.teacher.last_name,
                    "middle_name": subject.teacher.middle_name
                },
                "url": f"http://127.0.0.1:8000/subjects/{subject.pk}/"
            }
            c += 1
        return dict(res)
    
    def students(self):
        students = Student.objects.filter(klass=self)
        c = 1
        res = {}
        for student in students:
            res[c] = {
                'pid': student.pid,
                'first_name': student.first_name,
                'last_name': student.last_name,
                'middle_name': student.middle_name,
            }
            c += 1
        return res

    
    class Meta:
        verbose_name_plural = "Sinflar"

class Student(models.Model):
    pid         = models.CharField(max_length=20, default=generate)
    first_name  = models.CharField(max_length=200)
    last_name   = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200)
    klass       = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return self.last_name + " " + self.first_name + " " + self.middle_name
    
    class Meta:
        verbose_name_plural = "O'quvchilar"
        ordering = ["last_name"]

class Subject(models.Model):
    name    = models.CharField(max_length=200)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    klass   = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Fanlar"
        ordering = ["name"]

    def grades(self):
        res = {}
        dates = Date.objects.filter(subject=self)
        c = 1
        for date in dates:
            grades = date.grades.all()
            res[f"{date.date.day}/{date.date.month}/{date.date.year}"] = []
            print(date.date)
            for grade in grades:
                res[f"{date.date.day}/{date.date.month}/{date.date.year}"].append({
                    "student": {
                        "id": grade.student.pk,
                        "pid": grade.student.pid,
                        "first_name": grade.student.first_name,
                        "last_name": grade.student.last_name,
                        "middle_name": grade.student.middle_name,
                    },
                    "number": grade.number,
                    "string": grade.string,
                })
            c += 1
        return res


class Grade(models.Model):
    number  = models.CharField(max_length=10)
    string  = models.CharField(max_length=20)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date    = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.student.last_name + " " + self.student.first_name + " " + self.number + " " + self.subject.name + " " + str(self.date)
    
    class Meta:
        verbose_name_plural = "Baholar"
        ordering = ["student__last_name"]


class Date(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    date    = models.DateField()
    grades  = models.ManyToManyField(Grade, related_name="grades")

    def __str__(self):
        return self.subject.name + " " + str(self.date)
    
    

class Schedule(models.Model):
    klass     = models.ForeignKey(Class, on_delete=models.CASCADE)
    monday    = models.ManyToManyField(Subject, related_name="monday_subjects")
    tuesday   = models.ManyToManyField(Subject, related_name="tuesday_subject")
    wednesday = models.ManyToManyField(Subject, related_name="wednesday_subjects")
    thursday  = models.ManyToManyField(Subject, related_name="thursday_subjects")
    friday    = models.ManyToManyField(Subject, related_name="friday_subjects")
    saturday  = models.ManyToManyField(Subject, related_name="saturday_subjects")
    sunday    = models.ManyToManyField(Subject, related_name="sunday_subjects")

    def __str__(self):
        return self.klass.name
    
    def schedule(self):
        res = {}
        res['monday'] = []
        for i in self.monday.all():
            res['monday'].append(i.name)
        res['tuesday'] = []
        for i in self.tuesday.all():
            res['tuesday'].append(i.name)
        res['wednesday'] = []
        for i in self.wednesday.all():
            res['wednesday'].append(i.name)
        res['thursday'] = []
        for i in self.thursday.all():
            res['thursday'].append(i.name)
        res['friday'] = []
        for i in self.friday.all():
            res['friday'].append(i.name)
        res['saturday'] = []
        for i in self.saturday.all():
            res['saturday'].append(i.name)
        return res
    
    class Meta:
        verbose_name_plural = "Dars jadvallari"

@receiver(post_save, sender=Grade)
def fun1(sender, instance, **kwargs):
    from datetime import datetime
    now = datetime.now().date()
    date = Date.objects.filter(subject=instance.subject, date=instance.date)
    if date:
        date = date.first()
        date.grades.add(instance)
    else:
        date = Date.objects.create(
            subject=instance.subject,
            date=now
        )
        date.grades.add(instance)
        date.save()
