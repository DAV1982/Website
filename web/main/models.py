from django.db import models


class Task(models.Model):
    title = models.CharField("Название", max_length=50)
    task = models.TextField("Описание")
    level = models.CharField("Уровень", max_length=50)

    def __str__(self):
        return self.title

        class Meta:
            varbose_name = "Задача"
            varbose_name_plural = "Задачи"


