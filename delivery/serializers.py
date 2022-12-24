<<<<<<< HEAD
from rest_framework import serializers
from delivery.models import neww_order_info

class order_Serializer(serializers.ModelSerializer):
    class Meta:
        model = neww_order_info
        fields = ['id','payment_status']

=======
from rest_framework import serializers
from delivery.models import neww_order_info

class order_Serializer(serializers.ModelSerializer):
    class Meta:
        model = neww_order_info
        fields = ['id','payment_status']

>>>>>>> 3d89e68835facbecfce5429c0e3d265323376159
