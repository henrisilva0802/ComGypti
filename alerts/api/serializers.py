from rest_framework.serializers import ModelSerializer

from alerts.models import Report, Sensor, Notification


class ReportSerializer(ModelSerializer):
    class Meta:
        model = Report
        fields = ('id', 'name', 'description',)


class SensorSerializer(ModelSerializer):
    class Meta:
        model = Sensor
        fields = ('id', 'type')


class NotificationSerializer(ModelSerializer):
    class Meta:
        model = Notification
        fields = ('id','name')