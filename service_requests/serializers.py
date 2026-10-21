from django.contrib.auth.models import User

from rest_framework import serializers

from service_requests.models import ServiceRequest


class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = User

        fields = ["username","first_name","last_name","email","password"]

class ServiceRequestSerializer(serializers.ModelSerializer):

    class Meta:

        model = ServiceRequest

        fields = "__all__"

        read_only_fields = [
            "id",
            "created_date",
            "user"
        ]

    def validate_vehicle_number(self, validated_data):

        vehicle_number = validated_data.upper().replace(" ", "")

        if len(vehicle_number) < 5 or len(vehicle_number) > 10:

            raise serializers.ValidationError(
                "Vehicle number must be between 5 and 10 characters."
            )

        if not vehicle_number[:2].isalpha():

            raise serializers.ValidationError(
                "Vehicle number must start with two letters."
            )

        if not vehicle_number[2:4].isdigit():

            raise serializers.ValidationError(
                "Vehicle number must contain two digits after the first two letters."
            )

        if not vehicle_number[4:].isalnum():

            raise serializers.ValidationError(
                "Vehicle number must contain only letters and numbers."
            )

        if not vehicle_number[-1].isdigit():

            raise serializers.ValidationError(
                "Vehicle number must end with a digit."
            )

        return vehicle_number

    def validate_problem_description(self, validated_data):

        if not validated_data.strip():

            raise serializers.ValidationError(
                "Problem description cannot be empty."
            )

        return validated_data.strip()