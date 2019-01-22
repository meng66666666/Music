from django.db import models


class Wheel(models.Model):
    img_name = models.CharField(max_length=100)
    img_url = models.URLField(max_length=200)

    class Meta:
        db_table = 'wheel'


class User(models.Model):
    username = models.CharField(max_length=50, verbose_name='用户名')
    password = models.CharField(max_length=100, verbose_name='密码')
    phone_num = models.CharField(max_length=15, verbose_name='电话号码')

    def __str__(self):
        return self.username


class Singer(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=False, default=4292)
    singer_name = models.CharField(max_length=50)
    singer_img = models.URLField(max_length=200)
    album_img = models.URLField(max_length=200)
    singer_info = models.TextField()
    singer_fans = models.CharField(max_length=20)
    singer_albums = models.CharField(max_length=200)

    class Meta:
        db_table = 'singer'


class Label(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=False, default=0)
    label_name = models.CharField(max_length=10)

    class Meta:
        db_table = 'label'


class Songs(models.Model):
    song_id = models.CharField(max_length=20)
    song_name = models.CharField(max_length=50)
    song_img = models.URLField(max_length=200)
    song_lyrics = models.TextField()
    song_album = models.CharField(max_length=50)  # 所属专辑
    song_time = models.TimeField()  # 歌曲时长
    song_url = models.CharField(max_length=150)
    play_num = models.IntegerField()
    download_num = models.IntegerField()
    is_free = models.BooleanField()  # 是否免费
    label = models.ForeignKey(Label, on_delete=models.CASCADE)
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE)

    class Meta:
        db_table = 'songs'


class Comment(models.Model):
    comment_date = models.DateField()
    comment_text = models.TextField()
    praise = models.IntegerField()
    songs = models.ForeignKey(Songs, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'comment'


class Collections(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    songs = models.ForeignKey(Songs, on_delete=models.CASCADE)

    class Meta:
        db_table = 'collections'
