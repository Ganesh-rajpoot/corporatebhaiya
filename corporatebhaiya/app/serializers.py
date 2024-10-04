from rest_framework import serializers
from .models import UserProfile, Course, CourseCategory, Booking
from django.contrib.auth.models import User

# Serializer for User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

# Serializer for UserProfile
class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = ['user', 'role', 'bio', 'availability', 'courses']

# Serializer for CourseCategory
class CourseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseCategory
        fields = ['id', 'name', 'description']

# Serializer for Course
class CourseSerializer(serializers.ModelSerializer):
    category = CourseCategorySerializer()

    class Meta:
        model = Course
        fields = ['id', 'name', 'description', 'category']

# Serializer for Booking
class BookingSerializer(serializers.ModelSerializer):
    student = UserProfileSerializer()
    mentor = UserProfileSerializer()
    course = CourseSerializer()

    class Meta:
        model = Booking
        fields = ['id', 'student', 'mentor', 'course', 'date_time']
