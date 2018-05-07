from core import models


class Comment(models.BasicObjectModel, models.UGCModel, models.TextModel, models.ObjectRelatedModel, models.Likable):

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.text
