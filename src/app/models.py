
from django.db import models
from django.utils.translation import ugettext as _

# Create your models here.
class Orang(models.Model):
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, blank=True, null=True,
        related_name="children",
    )
    JENIS_KELAMIN = [
        ('Laki - Laki', 'Laki - Laki'),
        ('Perempuan', 'Perempuan'),
    ]
    nama = models.CharField(_("Nama"), max_length=100)
    jenis_kelamin = models.CharField(_("Jenis Kelamin"), choices=JENIS_KELAMIN, max_length=50)


    class Meta:
        verbose_name = 'Orang'
        verbose_name_plural ='Orang'

    def __str__(self) -> str:
        return self.nama

    def get_parents(self):
        parents = list(Orang.objects.filter(pk=self.id))
        p = self.parent
        return self._extracted_from_get_parent_id_4(p, parents)


    def _extracted_from_get_parent_id_4(self, p, parents):
        while p:
            parents.append(p)
            p = p.parent
        parents.reverse()
        return parents

    def get_all_children(self, include_self=True):
        r = []
        if include_self:
            r.append(self)
        for c in Orang.objects.filter(parent=self):
            _r = c.get_all_children(include_self=True)
            if len(_r) > 0:
                r.extend(_r)
        return r