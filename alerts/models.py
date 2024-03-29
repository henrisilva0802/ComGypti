from datetime import datetime

from django.db import models
from institutions.models import PublicEntity, ControlCenter


class Report(models.Model):
    title = models.CharField(max_length=12)
    origin_address_problem = models.TextField(max_length=500)
    description = models.TextField(max_length=800)
    control_center_city = models.ForeignKey(ControlCenter, on_delete=models.CASCADE)
    is_human_report = models.BooleanField(default=True)
    is_sensor_report = models.BooleanField(default=False)
    geocode_destin = models.TextField(max_length=500, editable=False)
    geocode_origin = models.TextField(max_length=500, editable=False)
    date = models.TextField(default= datetime.now)
    way_to_report_problem = models.TextField(max_length=1000, editable=False)

    def __str__(self):
        return self.title

    class Meta:
        app_label = 'alerts'


class Notification(models.Model):
    name = models.CharField(max_length=12)
    public_entity = models.ForeignKey(PublicEntity, on_delete=models.CASCADE)
    report = models.OneToOneField(
        Report,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return str(self.id) + ' - ' + self.name

    class Meta:
        app_label = 'alerts'


class Sensor(models.Model):
    name = models.CharField(max_length=12)
    tolerance_to_make_a_alert = models.FloatField(max_length=12)
    coordenate = models.TextField(max_length=25, null=True)

    def __str__(self):
        return str(self.id) + ' - ' + self.name

    class Meta:
        app_label = 'alerts'


class HumiditySensor(Sensor):
    match_alert_with_mosquito_sensor = models.FloatField(default=0)
    match_alert_with_brightness_sensor = models.FloatField(default=0)
    match_alert_with_carbon_dioxide_sensor = models.FloatField(default=0)

    class Meta:
        app_label = 'alerts'


class MosquitoSensor(Sensor):
    frequency_list = ['minute', 'hour', 'day']
    MINUTE = 'M'
    HOUR = 'H'
    DAY = 'D'
    FREQUENCY_LIST_CHOICES = [
        (MINUTE, 'Minute'),
        (HOUR, 'Hour'),
        (DAY, 'Day'),
    ]
    mosquito_sensor_frequency = models.CharField(
        max_length=1,
        choices=FREQUENCY_LIST_CHOICES,
        default=DAY,
    )
    match_alert_with_brightness_sensor = models.FloatField(default=0)
    match_alert_with_humidity_sensor = models.FloatField(default=0)
    match_alert_with_carbon_dioxide_sensor = models.FloatField(default=0)

    class Meta:
        app_label = 'alerts'


class BrightnessSensor(Sensor):
    turn_off_system_night = models.BooleanField(default=False)

    match_alert_with_mosquito_sensor = models.FloatField(default=0)
    match_alert_with_humidity_sensor = models.FloatField(default=0)
    match_alert_with_carbon_dioxide_sensor = models.FloatField(default=0)

    class Meta:
        app_label = 'alerts'


class CarbonDioxideSensor(Sensor):
    coordinate_of_greater_gas_centering = models.CharField(max_length=12)

    match_alert_with_mosquito_sensor = models.FloatField(default=0)
    match_alert_with_humidity_sensor = models.FloatField(default=0)
    match_alert_with_brightness_sensor = models.FloatField(default=0)

    class Meta:
        app_label = 'alerts'