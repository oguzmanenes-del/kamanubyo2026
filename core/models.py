from django.db import models
from django.utils.text import slugify


class SiteSetting(models.Model):
    site_name = models.CharField(max_length=150, default="Kamanubyo2026")
    site_title = models.CharField(max_length=200, default="Kamanubyo2026 | Kaman Öğrenci Rehberi")
    site_description = models.TextField(
        default="Kaman Uygulamalı Bilimler Yüksekokulu, öğrenci yaşamı, yurt, bölümler ve Kaman hakkında kapsamlı rehber."
    )
    logo = models.ImageField(upload_to="site/", blank=True, null=True)

    def __str__(self):
        return self.site_name


class Page(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    hero_title = models.CharField(max_length=220, blank=True, null=True)
    hero_subtitle = models.TextField(blank=True, null=True)
    content = models.TextField()
    featured_image = models.ImageField(upload_to="pages/", blank=True, null=True)

    meta_title = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.CharField(max_length=320, blank=True, null=True)
    keywords = models.CharField(max_length=255, blank=True, null=True)

    is_homepage = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['title']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class BlogPost(models.Model):
    title = models.CharField("Başlık", max_length=220)
    slug = models.SlugField("SEO Bağlantısı", unique=True, blank=True)
    excerpt = models.TextField("Kısa Açıklama", blank=True, null=True)
    content = models.TextField("İçerik")
    cover_image = models.ImageField("Kapak Görseli", upload_to="blog/", blank=True, null=True)

    meta_title = models.CharField("Meta Başlık", max_length=255, blank=True, null=True)
    meta_description = models.CharField("Meta Açıklama", max_length=320, blank=True, null=True)
    keywords = models.CharField("Anahtar Kelimeler", max_length=255, blank=True, null=True)

    is_published = models.BooleanField("Yayında mı?", default=True)
    created_at = models.DateTimeField("Oluşturulma Tarihi", auto_now_add=True)

    class Meta:
        verbose_name = "Blog Yazısı"
        verbose_name_plural = "Blog Yazıları"
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.question
