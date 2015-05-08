from rest_framework import serializers
from .models import Desk

class DeskSerializer(serializers.ModelSerializer):
    owner_id = serializers.SerializerMethodField()
    location_id = serializers.SerializerMethodField()
    desk_price = serializers.SerializerMethodField()
    city = serializers.SerializerMethodField()
    company = serializers.SerializerMethodField()

    def get_owner_id(self, obj):
        if obj.owner is not None:
            return obj.owner.id
        return None

    def get_location_id(self, obj):
        return obj.location.id

    def get_company(self, obj):
        return obj.location.company.name

    def get_desk_price(self, obj):
        return obj.location.price

    def get_city(self, obj):
        return obj.location.city

    class Meta:
        model = Desk
        fields = ('id', 'city', 'company', 'desk_price', 'owner_id', 'rent_start_date', 'rent_end_date', 'location_id')