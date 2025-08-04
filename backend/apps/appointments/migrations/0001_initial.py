# Generated manually for initial schema
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('repairs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100)),
                ('customer_email', models.EmailField(max_length=254)),
                ('scheduled_for', models.DateTimeField()),
                ('notes', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                (
                    'repair_price',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='appointments',
                        to='repairs.repairprice',
                    ),
                ),
            ],
            options={'ordering': ['scheduled_for']},
        ),
    ]
