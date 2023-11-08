from django.db import models
from django.utils.translation import gettext as _


class Category(models.Model):
    name = models.SlugField(_("name"))
    parent = models.ForeignKey('self', verbose_name=_("parent"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categories")

class Post(models.Model):
    title = models.CharField(_("title"), max_length=100)
    content = models.TextField(_("content"))
    category = models.ForeignKey(
        Category, 
        verbose_name=_("category"), 
        on_delete=models.CASCADE, 
        related_name='posts'
        )
    image = models.ImageField(_("image"), upload_to='posts/')
    publisher = models.ForeignKey(
        "accounts.User", 
        verbose_name=_("publisher"), 
        on_delete=models.CASCADE,
        related_name='posts'
        )
    
    class Statuse(models.TextChoices):
        PUBLISH = "PUBLISH", _("Publish")
        UNPUBLISH = "UNPUBLISH", _("Unpublish")
        DRAFT = "DRAFT", _("Draft")

    status = models.CharField(
        max_length=9,
        choices=Statuse.choices,
        default=Statuse.DRAFT,
    )

    create_at = models.DateTimeField(_("Create at"), auto_now=False, auto_now_add=True)
    update_at = models.DateTimeField(_("Update at"), auto_now=True, auto_now_add=False)


class ShortLink(models.Model):
    shorten = models.CharField(_("shorten link"), max_length=30)
    url = models.TextField(_("original url"))
    

    class Meta:
        verbose_name = _("ShortLink")
        verbose_name_plural = _("ShortLinks")

    def __str__(self):
        return self.shorten

    # def get_absolute_url(self):
    #     return reverse("ShortLink_detail", kwargs={"pk": self.pk})

