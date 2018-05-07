from core import models


class Like(models.BasicObjectModel, models.UGCModel, models.ObjectRelatedModel):

    class Meta:
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'
