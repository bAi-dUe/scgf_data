from django.db import models

# Create your models here.


class PoemCompletion(models.Model):
    question = models.CharField(max_length=20, verbose_name="诗歌上句")
    answer = models.CharField(max_length=20, verbose_name="诗歌下句")
    other1 = models.CharField(max_length=20, verbose_name="干扰项1")
    other2 = models.CharField(max_length=20, verbose_name="干扰项2")
    other3 = models.CharField(max_length=20, verbose_name="干扰项3")

    class Meta:
        verbose_name = "诗歌接龙"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.question


class PoemGenerate(models.Model):
    title = models.CharField(max_length=20, verbose_name="标题")
    content = models.CharField(max_length=200, verbose_name="内容")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="生成时间")

    class Meta:
        verbose_name = "诗歌生成"
        verbose_name_plural = verbose_name
