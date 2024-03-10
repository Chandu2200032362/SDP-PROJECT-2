from django.db import models

class YourModel(models.Model):

    user_id = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    confirm_password = models.CharField(max_length=255)
    college = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    # survey_app/models.py
    from django.db import models

    class SurveyResponse(models.Model):
        question_text = models.TextField()
        answer = models.TextField()

        def __str__(self):
            return f'{self.question_text}: {self.answer}'

