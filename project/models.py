from django.db import models
# データベース定義
# http://lvh.me:8000/s/ff7971f45f784ae58701874de7437429


class UserProfile(models.Model):
    """ ユーザープロフィール

    http://lvh.me:8000/s/d95025ad5a714450bcf7e4b61ab87068

    ユーザープロフィールモデル
    """

    user = models.CharField(verbose_name="ユーザー", max_length=255)
    bio = models.TextField(verbose_name="ビオ", default="空文字")
    phone = models.IntegerField(verbose_name="電話番号")
    city = models.CharField(verbose_name="都道府県", max_length=255)
    # カラムのパーマリンク
    # http://lvh.me:8000/s/4beb6dee460f425c9b67ae6d026d8167
    country = models.CharField(verbose_name="国", max_length=255)

    class Meta:
        verbose_name = "ユーザープロフィール"
        db_table = "user_profile"
