from django.db import models

# Create your models here.
from user.models import User


class Board(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=2000)
    hit = models.IntegerField(default=0)
    regdate = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # CASCADE : user 삭제되면 board 삭제 됨
    # SET_NULL : user 삭제되어도 board 삭제 안됨 (NULL 처리)

    def __str__(self):
        return "Board(%s, %s, %d, %s, %d)" % (self.title, self.content, self.hit, str(self.regdate), self.user.id)