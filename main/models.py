from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
import os
import shutil
from pathlib import Path
from django.conf import settings
from django.db.models.signals import post_delete
from django.dispatch import receiver


class UserProfile(models.Model):
	ROLE_TEACHER = 'teacher'
	ROLE_PRINCIPAL = 'principal'
	ROLE_CHOICES = [
		(ROLE_TEACHER, 'Teacher'),
		(ROLE_PRINCIPAL, 'Principal'),
	]

	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
	role = models.CharField(max_length=20, choices=ROLE_CHOICES)
	full_name = models.CharField(max_length=150)

	def __str__(self):
		return f"{self.full_name} ({self.get_role_display()})"


class VideoSubmission(models.Model):
	STATUS_PENDING = 'pending'
	STATUS_PROCESSING = 'processing'
	STATUS_COMPLETED = 'completed'
	STATUS_FAILED = 'failed'
	STATUS_CHOICES = [
		(STATUS_PENDING, 'Pending'),
		(STATUS_PROCESSING, 'Processing'),
		(STATUS_COMPLETED, 'Completed'),
		(STATUS_FAILED, 'Failed'),
	]

	SUBJECT_ENGLISH = 'english'
	SUBJECT_BAHASA = 'bahasa_indonesia'
	SUBJECT_SCIENCE = 'science'
	SUBJECT_MATH = 'math'
	SUBJECT_CHOICES = [
		(SUBJECT_ENGLISH, 'English'),
		(SUBJECT_BAHASA, 'Bahasa Indonesia'),
		(SUBJECT_SCIENCE, 'Science'),
		(SUBJECT_MATH, 'Math'),
	]

	teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='video_submissions')
	subject = models.CharField(max_length=50, choices=SUBJECT_CHOICES)
	class_name = models.CharField(max_length=100)
	submission_date = models.DateField(default=timezone.now, help_text="Learning date")
	day = models.CharField(max_length=20, editable=False, default='Monday')  # Auto-generated from date
	start_time = models.TimeField()
	end_time = models.TimeField()
	notes = models.TextField(blank=True)
	original_video = models.FileField(upload_to='videos/raw/')
	preprocessed_dir = models.CharField(max_length=255, blank=True)
	status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_PENDING)
	total_faces = models.PositiveIntegerField(default=0)
	model_score = models.FloatField(default=0.0)
	predicted_label = models.CharField(max_length=100, blank=True)
	ground_truth_label = models.CharField(max_length=100, blank=True)
	ground_truth_breakdown = models.TextField(default='{}')
	is_correct = models.BooleanField(null=True, blank=True)
	# Expression breakdown: JSON format {'Happy': 15, 'Sad': 8, ...}
	expression_breakdown = models.TextField(default='{}')
	process_log = models.TextField(blank=True)
	processed_at = models.DateTimeField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	modified_at = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['-created_at']

	def save(self, *args, **kwargs):
		"""Auto-generate day name from submission_date"""
		if self.submission_date:
			day_names = {
				0: 'Monday',      # Monday
				1: 'Tuesday',     # Tuesday
				2: 'Wednesday',   # Wednesday
				3: 'Thursday',    # Thursday
				4: 'Friday',      # Friday
				5: 'Saturday',    # Saturday
				6: 'Sunday'       # Sunday
			}
			self.day = day_names.get(self.submission_date.weekday(), 'Monday')
		super().save(*args, **kwargs)

	def __str__(self):
		return f"{self.subject} - {self.class_name} ({self.get_status_display()})"

@receiver(post_delete, sender=VideoSubmission)
def delete_media_files(sender, instance, **kwargs):
    """
    Automatically delete video file and preprocessed folder when record is deleted.
    This includes deletion via Dashboard and Admin Panel.
    """
    # 1. Delete original video file
    if instance.original_video:
        if os.path.isfile(instance.original_video.path):
            try:
                os.remove(instance.original_video.path)
            except Exception as e:
                print(f"Failed to delete video file: {e}")

    # 2. Delete preprocessed folder (face crops)
    if instance.preprocessed_dir:
        preproc_path = Path(instance.preprocessed_dir)
        if preproc_path.exists() and preproc_path.is_dir():
            try:
                shutil.rmtree(preproc_path)
            except Exception as e:
                print(f"Failed to delete preprocessed folder: {e}")