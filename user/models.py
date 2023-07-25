
from random import choices
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from user.managers import UserManager

class User(AbstractBaseUser):

    objects = UserManager()
    
    username = None
    first_name = None
    last_name = None
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['nickname', 'mbti']

    STATUS_NORMAL = 1
    STATUS_ABNORMAL = 2
    STATUS_DROPOUT = 999
    STATUS_CHOICES = [
        (STATUS_NORMAL, 'Normal status'),
        (STATUS_ABNORMAL, 'Something wrong'),
        (STATUS_DROPOUT, 'Dropped out user'),
    ]

    DOMAIN_LOCAL = 'LO'
    DOMAIN_KAKAO = 'KA'
    DOMAIN_GOOGLE = "GG"
    DOMAIN_CHOICES = [
        (DOMAIN_LOCAL, 'Local service account'),
        (DOMAIN_KAKAO, 'Kakao account'),
        (DOMAIN_GOOGLE, 'Google account'),
    ]

    username = models.CharField(unique=True, max_length=100, null=False, blank=False)
    nickname = models.CharField(max_length=100, null=True, blank=True)
    mbti = models.ForeignKey('type16.mbti', on_delete=models.DO_NOTHING, null=True, blank=True)
    domain = models.CharField(max_length=2, default=DOMAIN_LOCAL, choices=DOMAIN_CHOICES)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    status = models.IntegerField(default=1, choices=STATUS_CHOICES)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(null=True,blank=True)

    class Meta:
        db_table = "t_user"

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        self.full_clean()
        super(User, self).save(*args, **kwargs)

    
    def has_perm(self, perm, obj=None):
        if self.is_superuser or self.is_staff:
            return True
        return False

    def has_module_perms(self, app_label):
        if self.is_superuser or self.is_staff:
            return True
        return False
