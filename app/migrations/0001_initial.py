# Generated by Django 2.1.1 on 2020-08-02 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospitalid', models.CharField(max_length=25)),
                ('name', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('hospital', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PathTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testid', models.CharField(max_length=25)),
                ('patientid', models.CharField(max_length=25)),
                ('date', models.DateField(null=True)),
                ('year', models.IntegerField()),
                ('month', models.IntegerField()),
                ('sampletype', models.CharField(max_length=50)),
                ('organism', models.CharField(max_length=50)),
                ('hospital', models.CharField(max_length=50)),
                ('collsite', models.CharField(max_length=50)),
                ('amikacin', models.IntegerField(default=-1)),
                ('amoxicillin_clavulanicacid', models.IntegerField(default=-1)),
                ('ampicillin', models.IntegerField(default=-1)),
                ('ampicillin_sulbactum', models.IntegerField(default=-1)),
                ('cefaperazone_sulbactum', models.IntegerField(default=-1)),
                ('cefexime', models.IntegerField(default=-1)),
                ('cefotaxime', models.IntegerField(default=-1)),
                ('cefoxitin', models.IntegerField(default=-1)),
                ('ceftazidime', models.IntegerField(default=-1)),
                ('ceftazidime_clavalunicacid', models.IntegerField(default=-1)),
                ('ceftriaxone', models.IntegerField(default=-1)),
                ('chloramphenicol', models.IntegerField(default=-1)),
                ('ciprofloxacin', models.IntegerField(default=-1)),
                ('colistin', models.IntegerField(default=-1)),
                ('cotrimoxazole', models.IntegerField(default=-1)),
                ('ertapenem', models.IntegerField(default=-1)),
                ('erythromycin', models.IntegerField(default=-1)),
                ('gentamicin_highlevel', models.IntegerField(default=-1)),
                ('imipenem', models.IntegerField(default=-1)),
                ('levofloxacin', models.IntegerField(default=-1)),
                ('linezolid', models.IntegerField(default=-1)),
                ('meropenem', models.IntegerField(default=-1)),
                ('netilmicin', models.IntegerField(default=-1)),
                ('nitrofurantoin', models.IntegerField(default=-1)),
                ('penicillin', models.IntegerField(default=-1)),
                ('piperacillin_tazobactum', models.IntegerField(default=-1)),
                ('rifampicin', models.IntegerField(default=-1)),
                ('teicoplanin', models.IntegerField(default=-1)),
                ('tetracycline', models.IntegerField(default=-1)),
                ('ticarcillin_clavulanicacid', models.IntegerField(default=-1)),
                ('tigecycline', models.IntegerField(default=-1)),
                ('vancomycin', models.IntegerField(default=-1)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patientid', models.CharField(max_length=25)),
                ('testid', models.CharField(max_length=25)),
                ('state', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('hospital', models.CharField(max_length=50)),
                ('symptoms', models.CharField(max_length=50)),
                ('diagnosis', models.CharField(max_length=50)),
                ('test', models.CharField(max_length=50)),
                ('prescription', models.CharField(max_length=50)),
                ('allergy', models.IntegerField(default=0)),
            ],
        ),
    ]
