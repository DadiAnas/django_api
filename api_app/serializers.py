from .models import Article, Customer
from rest_framework import serializers


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['title', 'author', 'email']


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'  # ['first_name', 'last_name', 'email', 'gender', 'company', 'city', 'title']

# class ArticleSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=100)
#     author = serializers.CharField(max_length=100)
#     email = serializers.EmailField(max_length=100)
#     date = serializers.DateTimeField()
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.author = validated_data.get('author', instance.author)
#         instance.email = validated_data.get('email', instance.email)
#         instance.date = validated_data.get('date', instance.date)
#         instance.save()
#         return instance
#
#     def create(self, validated_data):
#         return Article.objects.create(validated_data)


# class CustomerSerializer(serializers.Serializer):
#     id = serializers.IntegerField(allow_null=False)
#     first_name = serializers.CharField(max_length=100)
#     last_name = serializers.CharField(max_length=100)
#     email = serializers.EmailField(max_length=100)
#     gender = serializers.CharField(max_length=50)
#     company = serializers.CharField(max_length=100)
#     city = serializers.CharField(max_length=100)
#     title = serializers.CharField(max_length=100)
#
#     def create(self, validated_data):
#         return Customer.objects.create(validated_data)
#
#     def update(self, instance, validated_data):
#         instance.id = validated_data.get('id', instance.id)
#         instance.first_name = validated_data.get('first_name', instance.first_name)
#         instance.last_name = validated_data.get('last_name', instance.last_name)
#         instance.email = validated_data.get('email', instance.email)
#         instance.gender = validated_data.get('gender', instance.gender)
#         instance.company = validated_data.get('company', instance.company)
#         instance.city = validated_data.get('city', instance.city)
#         instance.title = validated_data.get('title', instance.title)
#         instance.save()
#         return instance
