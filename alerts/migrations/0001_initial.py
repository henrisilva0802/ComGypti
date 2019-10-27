# Generated by Django 2.2.5 on 2019-10-26 04:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('institutions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=12)),
                ('tolerance_to_make_a_alert', models.FloatField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='BrightnessSensor',
            fields=[
                ('sensor_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='alerts.Sensor')),
                ('turn_off_system_night', models.BooleanField(default=False)),
                ('match_alert_with_mosquito_sensor', models.FloatField(default=0)),
                ('match_alert_with_humidity_sensor', models.FloatField(default=0)),
                ('match_alert_with_carbon_dioxide_sensor', models.FloatField(default=0)),
            ],
            bases=('alerts.sensor',),
        ),
        migrations.CreateModel(
            name='CarbonDioxideSensor',
            fields=[
                ('sensor_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='alerts.Sensor')),
                ('coordinate_of_greater_gas_centering', models.CharField(max_length=12)),
                ('match_alert_with_mosquito_sensor', models.FloatField(default=0)),
                ('match_alert_with_humidity_sensor', models.FloatField(default=0)),
                ('match_alert_with_brightness_sensor', models.FloatField(default=0)),
            ],
            bases=('alerts.sensor',),
        ),
        migrations.CreateModel(
            name='HumiditySensor',
            fields=[
                ('sensor_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='alerts.Sensor')),
                ('match_alert_with_mosquito_sensor', models.FloatField(default=0)),
                ('match_alert_with_brightness_sensor', models.FloatField(default=0)),
                ('match_alert_with_carbon_dioxide_sensor', models.FloatField(default=0)),
            ],
            bases=('alerts.sensor',),
        ),
        migrations.CreateModel(
            name='MosquitoSensor',
            fields=[
                ('sensor_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='alerts.Sensor')),
                ('mosquito_sensor_frequency', models.CharField(choices=[('M', 'Minute'), ('H', 'Hour'), ('D', 'Day')], default='D', max_length=1)),
                ('match_alert_with_brightness_sensor', models.FloatField(default=0)),
                ('match_alert_with_humidity_sensor', models.FloatField(default=0)),
                ('match_alert_with_carbon_dioxide_sensor', models.FloatField(default=0)),
            ],
            bases=('alerts.sensor',),
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=12)),
                ('description', models.TextField(max_length=800)),
                ('control_center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institutions.ControlCenter')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=12)),
                ('public_entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institutions.PublicEntity')),
            ],
        ),
    ]
