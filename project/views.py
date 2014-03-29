from django.shortcuts import render
from apps.articles.models import Article, Category

def home(request):
	sw_articles = Article.objects.filter(category__slug='surf-wire').order_by('-pub_date')[:3]
	g_articles = Article.objects.filter(category__slug='gear').order_by('-pub_date')[:3]
	wt_articles = Article.objects.filter(category__slug='world-tour').order_by('-pub_date')[:3]

	return render(request, 'home.html', {
		'sw_articles': sw_articles,
		'g_articles': g_articles,
		'wt_articles': wt_articles,
	})


def category(request, category_slug):
	articles = Article.objects.filter(category__slug=category_slug).order_by('-pub_date')
	category = Category.objects.get(slug=category_slug)

	return render(request, 'category.html', {
		'articles': articles,
		'category': category,
	})


def article(request, category_slug, article_id):
	article = Article.objects.get(id=article_id)

	return render(request, 'article.html', {
		'article': article,
	})