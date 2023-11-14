# Generated by Django 4.0.6 on 2023-03-08 09:12

import app.models
from django.db import migrations, models
import django.db.models.deletion
import django_jsonform.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='科室名称')),
                ('registration_fee', models.FloatField(default=0, verbose_name='挂号费')),
            ],
            options={
                'verbose_name': '科室管理',
                'verbose_name_plural': '科室管理',
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_number', models.CharField(default=app.models.make_doctor_random_number, max_length=6, unique=True, verbose_name='工号')),
                ('username', models.CharField(max_length=50, unique=True, verbose_name='医生用户名')),
                ('id_card', models.CharField(max_length=50, unique=True, verbose_name='身份证号')),
                ('phone', models.CharField(max_length=11, verbose_name='手机号')),
                ('password', models.CharField(help_text='存储的为密文，每次保存的时候密码会自动更新', max_length=250, verbose_name='密码')),
                ('sex', models.IntegerField(choices=[(1, '男'), (2, '女')], default=1, verbose_name='性别')),
                ('age', models.IntegerField(verbose_name='年龄')),
                ('limit', models.IntegerField(default=10, verbose_name='挂号限额')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.department', verbose_name='科室')),
            ],
            options={
                'verbose_name': '医生管理',
                'verbose_name_plural': '医生管理',
            },
            bases=(models.Model, app.models.AbsUser),
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='药品名称')),
                ('price', models.FloatField(verbose_name='药品价格')),
                ('unit', models.CharField(max_length=10, verbose_name='药品单位')),
                ('stock', models.IntegerField(verbose_name='药品库存')),
            ],
            options={
                'verbose_name': '药品管理',
                'verbose_name_plural': '药品管理',
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medical_insurance_number', models.CharField(default=app.models.make_patient_random_number, max_length=6, unique=True, verbose_name='医保号')),
                ('username', models.CharField(max_length=50, unique=True, verbose_name='患者用户名')),
                ('id_card', models.CharField(max_length=50, unique=True, verbose_name='身份证号')),
                ('phone', models.CharField(max_length=11, verbose_name='手机号')),
                ('password', models.CharField(help_text='存储的为密文，每次保存的时候密码会自动更新', max_length=250, verbose_name='密码')),
                ('sex', models.IntegerField(choices=[(1, '男'), (2, '女')], default=1, verbose_name='性别')),
                ('age', models.IntegerField(verbose_name='年龄')),
            ],
            options={
                'verbose_name': '患者管理',
                'verbose_name_plural': '患者管理',
            },
            bases=(models.Model, app.models.AbsUser),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_description', models.TextField(max_length=250, verbose_name='患者自述情况')),
                ('readme', models.TextField(max_length=250, verbose_name='医嘱')),
                ('medicine_list', django_jsonform.models.fields.JSONField(blank=True, null=True, verbose_name='药品列表')),
                ('total_cost', models.FloatField(default=0, verbose_name='总费用')),
                ('status', models.BooleanField(default=False, verbose_name='诊断结束')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='预约时间')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.department', verbose_name='科室')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.doctor', verbose_name='医生')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.patient', verbose_name='患者')),
            ],
            options={
                'verbose_name': '预约管理',
                'verbose_name_plural': '预约管理',
            },
        ),
    ]