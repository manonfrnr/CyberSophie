# Generated by Django 3.0.5 on 2020-04-05 13:41

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enonce', models.CharField(max_length=300)),
                ('isLibre', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Reponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valeur', models.CharField(max_length=1000)),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date de la réponse')),
                ('ip', models.CharField(max_length=30)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Question')),
            ],
        ),
        migrations.CreateModel(
            name='Choix',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valeur', models.CharField(max_length=100)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Question')),
            ],
            options={
                'verbose_name_plural': 'Choix',
            },
        ),
    ]
