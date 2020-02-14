import hashlib
from django.db import models
from django.conf import settings

from core.models import Attachment


class UserManager(models.Manager):
    """
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


    @classmethod
    def login(cls, request, user, is_persist):
        """ログイン
        """
        request.session[settings.USER_SESSION_KEY] = user.id

        # セッション設定
        if is_persist:
            request.session.set_expiry(settings.SESSION_COOKIE_AGE)
        else:
            request.session.set_expiry(0)

    @classmethod
    def logout(cls, session):
        """ログアウト
        """
        session.flush()
        session[settings.USER_SESSION_KEY] = None

    @classmethod
    def create_user(cls, name, email, raw_password):
        """ユーザの作成
        """
        return cls.objects.create(
            name=name,
            email=email,
            password=raw_password,
        )

    @classmethod
    def to_hash(cls, raw_password):
        """パスワードをハッシュ化して返す
        """
        return hashlib.sha256(
            'Polypterus{}endlicheri'.format(raw_password).encode('utf-8')
        ).hexdigest()

    @classmethod
    def get_user(cls, email, raw_password):
        """引数をもとに対象ユーザを取得する、なければNoneを返す
        """
        ret = None
        try:
            ret = cls.objects.get(email=email,
                                  password=cls.to_hash(raw_password))
        except cls.DoesNotExist:
            pass
        return ret

    def save(self, *args, **kwargs):
        if not self.id:  # ユーザ登録時にはパスワードをハッシュ化する
            # ハッシュアルゴリズムについて
            # http://lvh.me:8000/s/708f4e5ed87742169c0ce7a6f00adce2
            self.password = self.to_hash(self.password)
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return '%s' % self.name

    class Meta:
        db_table = 'user'


class UserAttachment(models.Model):
    """http://lvh.me:8000/s/3eb30c48d1fa4b6ebe2bee48d601a2e7
    """
    attachment = models.ForeignKey(Attachment, verbose_name='ファイル', on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name='ユーザー', on_delete=models.CASCADE)

    class Meta:
        db_table = 'user_attachment'
