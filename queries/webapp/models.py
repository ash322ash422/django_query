from django.db import models
from  django.utils import timezone

# Create your models here.
class Query(models.Model ):
    """We do not have to explicitly create Primary Keys b/c auto. does this
    id =models.AutoField(primary_key=True)
    """
    id =models.AutoField(primary_key=True)
    qry_name = models.CharField(max_length = 100, unique = True)
    qry = models.TextField(help_text = 'Enter query here')
    create_by = models.CharField(max_length = 20)
    create_on = models.DateField(verbose_name = "Created 0n", blank=True,
                        null=True, default = timezone.now )
    last_accessed = models.DateTimeField( verbose_name= "Last accessed",
                        help_text = "Last time this query was accessed",
                        blank=True, null=True, default = timezone.now )
    num_visit = models.PositiveIntegerField(verbose_name="Num of visits to this qry", default=1)
    
    def __str__(self):
        return "{} by {}".format(self.qry_name, self.create_by,)
    
    class Meta:
        db_table = 'tb_queries'
        verbose_name = 'Query'
        verbose_name_plural = 'Queries'
        ordering = ['qry_name'] #or use ['-title']

#end class 