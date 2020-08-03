# -*- encoding: utf-8 -*-


from django.db import models
from django.contrib.auth.models import User
from app.variables import *


class PathTest(models.Model):
    testid = models.CharField(max_length=25)
    patientid = models.CharField(max_length=25)
    date = models.DateField(null=True)
    year = models.IntegerField()
    month = models.IntegerField()
    sampletype = models.CharField(max_length=50)
    organism = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    hospital = models.CharField(max_length=50)
    collsite = models.CharField(max_length=50)
    # AM Fields, add all
    amikacin = models.IntegerField(default=-1)
    amoxicillin_clavulanicacid = models.IntegerField(default=-1)
    ampicillin = models.IntegerField(default=-1)
    ampicillin_sulbactum = models.IntegerField(default=-1)
    cefaperazone_sulbactum = models.IntegerField(default=-1)
    cefexime = models.IntegerField(default=-1)
    cefotaxime = models.IntegerField(default=-1)
    cefoxitin = models.IntegerField(default=-1)
    ceftazidime = models.IntegerField(default=-1)
    ceftazidime_clavalunicacid = models.IntegerField(default=-1)
    ceftriaxone = models.IntegerField(default=-1)
    chloramphenicol = models.IntegerField(default=-1)
    ciprofloxacin = models.IntegerField(default=-1)
    colistin = models.IntegerField(default=-1)
    cotrimoxazole = models.IntegerField(default=-1)
    ertapenem = models.IntegerField(default=-1)
    erythromycin = models.IntegerField(default=-1)
    gentamicin_highlevel = models.IntegerField(default=-1)
    imipenem = models.IntegerField(default=-1)
    levofloxacin = models.IntegerField(default=-1)
    linezolid = models.IntegerField(default=-1)
    meropenem = models.IntegerField(default=-1)
    netilmicin = models.IntegerField(default=-1)
    nitrofurantoin = models.IntegerField(default=-1)
    penicillin = models.IntegerField(default=-1)
    piperacillin_tazobactum = models.IntegerField(default=-1)
    rifampicin = models.IntegerField(default=-1)
    teicoplanin = models.IntegerField(default=-1)
    tetracycline = models.IntegerField(default=-1)
    ticarcillin_clavulanicacid = models.IntegerField(default=-1)
    tigecycline = models.IntegerField(default=-1)
    vancomycin = models.IntegerField(default=-1)


class Patient(models.Model):
    patientid = models.CharField(max_length=25)
    testid = models.CharField(max_length=25)
    state = models.CharField(max_length=50,default="")
    district = models.CharField(max_length=50,default="")
    hospital = models.CharField(max_length=50,default="")
    symptoms = models.CharField(max_length=50,default="")
    diagnosis = models.CharField(max_length=50,default="")
    test = models.CharField(max_length=50,default="")
    prescription = models.CharField(max_length=50,default="")
    allergy = models.IntegerField(default=0)


class Hospital(models.Model):
    hospitalid = models.CharField(max_length=25)
    name = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    hospital = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
