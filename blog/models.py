from django.conf import settings
from django.db import models
from django.utils import timezone


# 모델 (객체) 정의
# class : 객체를 정의
# Post : 모델 이름
# models : Post가 장고 모델임을 선언 -> Post가 데이터베이스에 저장되어야 함
class Post(models.Model):
    # models.CharField : 글자 수가 제한된 텍스트를 정의
    # models.TextField : 글자 수가 제한 없는 긴 텍스트를 정의
    # models.DateTimeField : 날짜와 시간 의미
    # models.ForeignKey : 다른 모델에 대한 링크 의미
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # __ = 던더 (더블 언더 스코어)
    def __str__(self):
        return self.title