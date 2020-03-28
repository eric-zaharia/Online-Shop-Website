from django.db import models


class Post(models.Model):
    titlu = models.CharField(max_length=255)
    data_p = models.DateTimeField()
    autor = models.CharField(max_length=31)
    continut = models.CharField(max_length=3000, default='gol')

    def __str__(self):
        return self.titlu


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.deletion.CASCADE, related_name='comments')
    nume_cont = models.CharField(max_length=31, default='no name')
    data_ora = models.DateTimeField()
    continut = models.CharField(max_length=1000, default='gol')




