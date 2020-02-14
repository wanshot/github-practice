import hashlib
from django.db import models
from django.conf import settings

from core.models import Attachment


class UserManager(models.Manager):
    """http://lvh.me:8000/s/3eb30c48d1fa4b6ebe2bee48d601a2e7
    """
    def active(self):
        """有効なユーザのみに絞りこむ
        """
        return super(UserManager, self).get_queryset().filter(is_active=True)


class User(models.Model):
    """ユーザー（システムの利用者）
    """
    name = models.CharField(u"名前", max_length=64)
    email = models.CharField(u"メールアドレス", max_length=255, unique=True)
    password = models.CharField(u"パスワード", max_length=255)
    is_active = models.BooleanField(u"有効フラグ", default=True)  # 退会時にFalseにする想定
    objects = UserManager()

    def save(self, *args, **kwargs):
        if not self.id:  # ユーザ登録時にはパスワードをハッシュ化する
            self.password = self.to_hash(self.password)
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return '%s' % self.name

    class Meta:
        db_table = 'user'


class UserAttachment(models.Model):
    attachment = models.ForeignKey(Attachment, verbose_name='ファイル', on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name='ユーザー', on_delete=models.CASCADE)

    class Meta:
        db_table = 'user_attachment'
