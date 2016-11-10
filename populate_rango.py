import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Tango_with_django_3.settings')

import django
django.setup()

from rango.models import Category, Page


def populate():
    python_pages = [
        {'title': 'Official Python Tutorial',
         'url': 'http://docs.python.org/2/tutorial',
         'views': 100},

        {'title': 'How to Think like a Computer Scientist',
         'url': 'http://www.greenteapress.com/thinkpython',
         'views': 200},

        {'title': 'Learn Python in 10 Minutes',
         'url': 'http://www.koroithankis.net/tutorials/python/',
         'views': 300}
    ]

    django_pages = [
        {'title': 'Official Django Tutorial',
         'url': 'https://docs.djangoproject.com/en/1.9/intro/tutorial01/',
         'views': 150},

        {'title': 'Django Rocks',
         'url': 'http://www.djangorocks.com',
         'views': 250},

        {'title': 'How to Tango with Django',
         'url': 'http://www.tangowithdjango.com/',
         'views': 350}
    ]

    other_pages = [
        {'title': 'Bottle',
         'url': 'http://bottlepy.org/docs/dev/',
         'views': 400},

        {'title': 'Flask',
         'url': 'http://flask,pocoo.org',
         'views': 500}
    ]

    chinese_pages = [
        {'title': 'python中文社区',
         'url': 'http://www.pythontab.com/',
         'views': 600}
    ]

    cats = {'Python': {'pages': python_pages, 'views': 128, 'likes': 64},
            'Django': {'pages': django_pages, 'views': 64, 'likes': 32},
            'Other Frameworks': {'pages': other_pages, 'views': 32, 'likes': 16},
            '中文测试': {'pages': chinese_pages, 'views': 222, 'likes': 666}}

    for cat, cat_data in cats.items():
        c = add_cat(cat, cat_data['views'], cat_data['likes'])
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'], p['views'])

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(p)))


def add_cat(name, views, likes):
    c = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c


def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.views = views
    p.save()
    return p


if __name__ == '__main__':
    print('Staring Rango population script...')
    populate()