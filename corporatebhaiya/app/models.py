from django.db import models
from django.contrib.auth.models import User

# CourseCategory Model
class CourseCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

# Course Model
class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE, related_name='courses')

    def __str__(self):
        return self.name

# UserProfile Model (Extends the User model for Mentor/Student roles)
class UserProfile(models.Model):
    ROLE_CHOICES = (
        ('mentor', 'Mentor'),
        ('student', 'Student'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    bio = models.TextField(blank=True, null=True)
    courses = models.ManyToManyField(Course, blank=True)  # Only used for mentors
    availability = models.JSONField(blank=True, null=True)  # Availability for mentorship (e.g. JSON data)

    def __str__(self):
        return f"{self.user.username} - {self.role}"

# Booking Model for booking mentor sessions
class Booking(models.Model):
    student = models.ForeignKey(UserProfile, related_name='bookings', on_delete=models.CASCADE)
    mentor = models.ForeignKey(UserProfile, related_name='mentorships', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_time = models.DateTimeField()

    def __str__(self):
        return f'{self.student.user.username} booked {self.mentor.user.username} for {self.course.name} on {self.date_time}'
