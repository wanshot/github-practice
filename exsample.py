from django.db import models


class User(models.Model):
    """ ユーザー

    https://tracery.jp/s/abe2c3758be247dbb483f5e71b338134
    """

    class Meta:
        verbose_name = "ユーザー"
        db_table = "user"


class Term(models.Model):
    """ 用語

    https://tracery.jp/s/305038611d2b4e07a63e3be5a6aac216
    """

    class Meta:
        verbose_name = "用語"
        db_table = "term"
