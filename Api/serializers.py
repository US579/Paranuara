from rest_framework import serializers
from .models import Company, People


VEGATABLE = ['cucumber', 'beetroot', 'carrot', 'celery']


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('index', 'company')


class People2dbSerializer(serializers.ModelSerializer):
    index = serializers.IntegerField(min_value=0, required=True)
    name = serializers.CharField(
        max_length=50, allow_blank=True, required=False)
    _id = serializers.CharField(
        max_length=50, allow_blank=True, required=False)
    guid = serializers.CharField(
        max_length=128, allow_blank=True, required=False)
    has_died = serializers.BooleanField(default=False, required=False)
    balance = serializers.DecimalField(
        max_digits=16, decimal_places=2, required=False)
    picture = serializers.CharField(
        max_length=128, allow_blank=True, required=False)
    age = serializers.IntegerField(min_value=0, required=False)
    eyeColor = serializers.CharField(
        max_length=16, allow_blank=True, required=False)
    gender = serializers.CharField(
        max_length=8, allow_blank=True, required=False)
    email = serializers.EmailField(
        max_length=64, allow_blank=True, required=False)
    phone = serializers.CharField(
        max_length=32, allow_blank=True, required=False)
    tags = serializers.CharField(
        max_length=512, allow_blank=True, required=False)
    address = serializers.CharField(
        max_length=512, allow_blank=True, required=False)
    about = serializers.CharField(allow_blank=True, required=False)
    registered = serializers.DateTimeField(
        format="%Y-%m-%dT%H:%M:%S", required=False, read_only=True)
    greeting = serializers.CharField(allow_blank=True, required=False)
    company_id = serializers.IntegerField(required=False)
    fruits = serializers.CharField(allow_blank=True, required=False)
    vegetables = serializers.CharField(allow_blank=True, required=False)
    friends = serializers.CharField(allow_blank=True, required=False)

    class Meta:
        model = People
        fields = '__all__'

    def create(self, validated_data):
        index = validated_data['company_id'] - 1
        validated_data['company_id'] = Company.objects.get(index=index)
        People.objects.update_or_create(
            index=validated_data['index'], defaults=validated_data)


class EmployeesHelpSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = ('name', 'age', 'address', 'phone')


class EmployeesSerializer(serializers.ModelSerializer):
    employees = EmployeesHelpSerializer(many=True, read_only=True)

    class Meta:
        model = Company
        fields = ('index', 'company', 'employees', )


class SameFriendsSerializer(serializers.BaseSerializer):
    def to_representation(self, obj):
        return {
            'people1': EmployeesHelpSerializer(obj['people1']).data,
            'people2': EmployeesHelpSerializer(obj['people2']).data,
            'same_friends': EmployeesHelpSerializer(obj['same_friends'], many=True).data,
        }


class FoodHelpSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='name')
    class Meta:
        model = People
        fields = ('username', 'age',)


class FriutVegetableSerializer(serializers.ModelSerializer):
     def to_representation(self, obj):
         res = FoodHelpSerializer(obj['name']).data
         res['fruits'] = obj['fruits']
         res['vegatables'] = obj['vegatables']
         return res
