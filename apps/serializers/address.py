from rest_framework import serializers
from apps.models import Address, Currency
from apps.serializers import CurrencySerializer

class AddressSerializer(serializers.ModelSerializer):
    currency_id = serializers.PrimaryKeyRelatedField(queryset=Currency.objects.filter(status='active'))
    user_id = serializers.IntegerField()
    currency = CurrencySerializer(read_only=True)

    def generate_query(self, validated_data, is_used=False):
        return {
            'currency_id': validated_data['currency_id'],
            'user_id': validated_data['user_id'],
            'is_used': is_used
        }

    class Meta:
        model = Address
        fields = (
            'currency_id',
            'user_id',
            'address',
            'label',
            'currency',
        )
        read_only_fields = (
            'address',
            'label'
        )
        extra_kwargs = {
            'currency_id': {'required': True},
            'user_id': {'required': True}
        }

    def create(self, validated_data):
        try:
            query = self.generate_query(validated_data)
            user_address = Address.objects.get(**query)
            if user_address:
                return user_address
        except Address.DoesNotExist:
            query = self.generate_query(validated_data, is_used=False) 
            user_id = query.pop('user_id')
            addresses = Address.objects.filter(
                **query
            )
            if not addresses:
                raise serializers.ValidationError({"detail": "No addresses ready"})
            
            user_address = addresses.first()
            user_address.is_used = True
            user_address.user_id = user_id
            user_address.label = f"{validated_data['currency_id'].symbol} - {user_id}"
            user_address.save()

            return user_address
        
        except Exception as e:
            raise serializers.ValidationError({"detail": "Invalid server"})
