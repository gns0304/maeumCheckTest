from imagekit.models import ProcessedImageField 
from imagekit.processors import ResizeToFit
from django.db.models import Count
from django.db import models

# Create your models here.
class List(models.Model):
    title= models.CharField(max_length=200) #TITLE 

    people = models.IntegerField() #사람수 근데 count 이용해서 모델추가될때마다 늘어나도록 짜고 싶은데 방법을 모르겠음 

    QRcode = models.URLField() #QRcode 링크

    QRimage = ProcessedImageField( #이미지객체를 담고있음 image.url 을 통해 이미지 경로에 접근함
        upload_to ='postings/resize/%Y%m%d',
        processors =[ResizeToFit(width=50, upscale=False)], #이미지처리 진행하는 인자
        format ='JPEG'
    )
    created_at = models.DateTimeField(auto_now_add=True) #생성일
    visited_at = models.DateTimeField(auto_now =True) #방문기록
    out_at = models.DateTimeField(auto_now =True) #나가는기록

    def __str__(self):
        return self.title

    

