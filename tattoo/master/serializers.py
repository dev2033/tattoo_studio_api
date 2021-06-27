from rest_framework import serializers

from .models import Master, RecordToMasterModel, MasterSkills


class MasterDetailSerializer(serializers.ModelSerializer):
    """Сериалайзер для вывода мастера"""
    class Meta:
        model = Master
        fields = '__all__'


class MasterListSerializer(serializers.ModelSerializer):
    """Сериалайзер для вывода списка мастеров"""
    class Meta:
        model = Master
        fields = ('name', )
