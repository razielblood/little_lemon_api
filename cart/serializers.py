from rest_framework import serializers
from cart.models import Cart
from rest_framework.validators import UniqueTogetherValidator
from django.contrib.auth.models import User
from menu.serializers import MenuItemSerializer


class CartSerializer(serializers.ModelSerializer):
    menuitem = MenuItemSerializer(read_only=True)
    menuitem_id = serializers.IntegerField(write_only=True)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), default=serializers.CurrentUserDefault())
    price = serializers.DecimalField(max_digits=6, decimal_places=2, read_only=True)
    validators = [UniqueTogetherValidator(queryset=Cart.objects.all(), fields=["user", "menuitem_id"])]

    class Meta:
        model = Cart
        fields = ["id", "user", "menuitem", "menuitem_id", "quantity", "unit_price", "price"]

    def create(self, validated_data):
        validated_data["price"] = validated_data.get("unit_price") * validated_data.get("quantity")

        cart_item = Cart.objects.create(**validated_data)

        return cart_item

    def update(self, instance, validated_data):
        cart_item = Cart.objects.get(user=validated_data.get("user"), menuitem_id=validated_data.get("menuitem_id"))
        cart_item.price = validated_data.get("unit_price") * validated_data.get("quantity")
        cart_item.quantity = validated_data.get("quantity")
        cart_item.unit_price = validated_data.get("unit_price")
        cart_item.save()
        return cart_item


class DestroyCartSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), default=serializers.CurrentUserDefault())

    def destroy(self, validated_data):
        Cart.objects.filter(user=validated_data.get("user")).delete()
