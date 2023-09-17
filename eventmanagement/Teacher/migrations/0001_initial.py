# Generated by Django 4.2.5 on 2023-09-17 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attends',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(default=0)),
                ('dateRegistered', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('RoomID', models.BigAutoField(primary_key=True, serialize=False)),
                ('RoomName', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=20)),
                ('first_name', models.CharField(max_length=20)),
                ('middle_name', models.CharField(blank=True, max_length=20, null=True)),
                ('last_name', models.CharField(max_length=20)),
                ('type', models.CharField(choices=[('S', 'Student'), ('T', 'Teacher')], max_length=1)),
                ('age', models.IntegerField()),
                ('specialization', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specialization', models.CharField(max_length=20)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher_specialize', to='Teacher.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('EventID', models.AutoField(primary_key=True, serialize=False)),
                ('EventTitle', models.CharField(max_length=50)),
                ('DateofEvent', models.DateTimeField()),
                ('MaxParticipants', models.IntegerField()),
                ('geek', models.ManyToManyField(through='Teacher.Attends', to='Student.student')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Teacher.room')),
                ('teachers', models.ManyToManyField(to='Teacher.teacher')),
            ],
        ),
        migrations.AddField(
            model_name='attends',
            name='eventid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Teacher.event'),
        ),
        migrations.AddField(
            model_name='attends',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Student.student'),
        ),
    ]
