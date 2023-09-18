from django.db import models
from utils import gen_id
from django.db.models.signals import post_save
from django.dispatch import receiver

def json():
    return {}

class Teacher(models.Model):
    tid = models.IntegerField(default=gen_id, editable=False, verbose_name="O'qituvchi ID si")
    first_name = models.CharField(max_length=200, verbose_name="Ism")
    last_name = models.CharField(max_length=200, verbose_name="Familiya")
    middle_name = models.CharField(max_length=200, verbose_name="Sharif")

    def __str__(self):
        return self.first_name + " " + self.last_name
    

class School(models.Model):
    sid = models.IntegerField(default=gen_id, verbose_name="Maktab ID si")
    rector = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, verbose_name="Direktor")
    name = models.CharField(max_length=200, verbose_name="Nomi")

    def __str__(self):
        return self.name

class Class(models.Model):
    cid = models.IntegerField(default=gen_id, verbose_name="Sinf ID si", editable=False)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, verbose_name="Raxbar")
    school = models.ForeignKey(School, on_delete=models.CASCADE, verbose_name="Maktab")
    name = models.CharField(max_length=200, verbose_name="Nomi")

    def __str__(self):
        return self.name

class Pupil(models.Model):
    pid = models.IntegerField(default=gen_id, verbose_name="O'quvchi ID si", editable=False)
    klass = models.ForeignKey(Class, on_delete=models.CASCADE, verbose_name="Sinf")
    first_name = models.CharField(max_length=200, verbose_name="Ism")
    last_name = models.CharField(max_length=200, verbose_name="Familiya")
    middle_name = models.CharField(max_length=200, verbose_name="Sharifi")
    phone_number = models.CharField(max_length=20, verbose_name='Telefon raqami', null=True, blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Subject(models.Model):
    sbid = models.IntegerField(default=gen_id, verbose_name="Fan ID si")
    name = models.CharField(max_length=200, verbose_name="Nomi")
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, verbose_name="O'qituvchi")
    klass = models.ForeignKey(Class, on_delete=models.CASCADE, verbose_name="Sinf")

    def __str__(self):
        return self.name


class Grade(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    grades = models.JSONField(default=json)
    dates = models.JSONField(default=json)

@receiver(post_save, sender=Subject)
def update_stock(sender, instance, **kwargs):
    grade = Grade.objects.filter(subject__sbid=instance.sbid).first()
    if grade:
        pass
    else:
        pupils = Pupil.objects.filter(klass=instance.klass)
        d = {}
        for i in pupils:
            d[f"{i.pid}"] = {}
        Grade.objects.create(
            subject=instance,
            grades=d,
            dates={"dates": []}
        )

@receiver(post_save, sender=Pupil)
def update_stock(sender, instance, **kwargs):
    grades = Grade.objects.filter(subject__klass=instance.klass)
    if grades:
        for grade in grades:
            grade.grades[instance.pid] = {}
            grade.save()
    else:
        pass