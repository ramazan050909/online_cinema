from django.db import models
from django.contrib.auth import get_user_model
from movies.models import Movie

User = get_user_model()

class AbstractModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    class Meta:
        abstract = True


class Comment(AbstractModel):
    text = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'Comment {self.id} from {self.user.username}'
    
    class Meta:
        default_related_name = 'comments'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
    
class RatingChoices(models.IntegerChoices):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5


class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rate = models.PositiveIntegerField(choices=RatingChoices.choices)

    def __str__(self) -> str:
        return str(self.rate)
    
    class Meta:
        default_related_name = 'ratings'

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги фильмов'
    

class Favorite(AbstractModel):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)


    class Meta:
        default_related_name = 'favorites'

    class Meta:
        verbose_name = 'Избранные'
        verbose_name_plural = 'Избранные'

class Like(AbstractModel):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)


    class Meta:
        default_related_name = 'like'

    class Meta:
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'