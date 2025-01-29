from django.db import models

class React(models.Model):
    v1 = models.FloatField()
    v2 = models.FloatField(max_length=10)
    v3 = models.FloatField()
    v4 = models.FloatField()
    v5 = models.FloatField()
    v6 = models.FloatField()
    v7 = models.FloatField()
    v8 = models.FloatField()

    class Meta:
        db_table = 'predictor_react' 
