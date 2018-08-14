from django.db import models
from django.utils import timezone
from django.utils.dateformat import DateFormat,TimeFormat

class Vache(models.Model):
    # 태그 넘버
    numero_tag = models.CharField(max_length=30, primary_key=True)
    # 개체 정보 저장 일시
    date_stocker = models.DateTimeField(blank=True,null=True,default=timezone.now)
    SEXE = (
        ('F','Femelle'),
        ('M','Mâle'),
    )
    sexe = models.CharField(max_length=1,choices=SEXE,null=True)
    #수태 여부
    gestation = models.BooleanField(default=True)

    def stocker(self):
        self.date_stocker=timezone.now()
        self.save()

    def __str__(self):
        return self.numero_tag

class Senseur(models.Model):
    vache=models.ForeignKey(Vache,on_delete=models.CASCADE)
    temperature = models.DecimalField(decimal_places=2,max_digits=4,default=0)
    mouvement = models.DecimalField(decimal_places=2,max_digits=4,default=0)
    # 데이터 저장 일시
    date_stocker = models.DateTimeField(blank=True,null=True,default=timezone.now)

    def __str__(self):
        return self.vache.numero_tag

    def enregistrer(self):
        self.date_stocker=timezone.now()
        self.save()

# 공지사항 Post
class Post(models.Model):
    auteur = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    titre = models.CharField(max_length=200)
    texte = models.TextField()
    date_publication = models.DateTimeField(blank=True,null=True,default=timezone.now)

    def publier(self):
        self.date_publication = timezone.now()
        self.save()

    def __str__(self):
        return self.titre



