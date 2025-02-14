# Generated by Django 4.1.7 on 2023-02-22 16:05

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, db_column='title_db_column', db_index=True, db_tablespace='title_db_tablespace', default='', error_messages=False, help_text='<small class="text-muted">CharField [0, 300]</small><hr><br>', max_length=300, null=True, validators=[django.core.validators.MinLengthValidator(0), django.core.validators.MaxLengthValidator(300)], verbose_name='Заголовок')),
                ('description', models.TextField(blank=True, db_column='description_db_column', db_index=True, db_tablespace='description_db_tablespace', default='', error_messages=False, help_text='<small class="text-muted">TextField [0, 3000]</small><hr><br>', max_length=3000, null=True, validators=[django.core.validators.MinLengthValidator(0), django.core.validators.MaxLengthValidator(3000)], verbose_name='Описание')),
                ('is_completed', models.BooleanField(blank=True, db_column='is_completed_db_column', db_index=True, db_tablespace='is_completed_db_tablespace', default=False, error_messages=False, help_text='<small class="text-muted">BooleanField</small><hr><br>', verbose_name='Статус выполнения')),
                ('created', models.DateTimeField(blank=True, db_column='created_db_column', db_index=True, db_tablespace='created_db_tablespace', default=django.utils.timezone.now, error_messages=False, help_text='<small class="text-muted">DateTimeField</small><hr><br>', null=True, verbose_name='Дата и время создания')),
                ('updated', models.DateTimeField(blank=True, db_column='updated_db_column', db_index=True, db_tablespace='updated_db_tablespace', default=django.utils.timezone.now, error_messages=False, help_text='<small class="text-muted">DateTimeField</small><hr><br>', null=True, verbose_name='Дата и время обновления')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Task',
                'verbose_name_plural': 'Tasks',
                'db_table': 'task_task_list_model_table',
                'ordering': ('-updated',),
            },
        ),
    ]
