import requests
from time import sleep
from news.models.models import Article


def get_facebook_shares(url):
    shares = 0
    try:
        r = requests.get('https://graph.facebook.com/?id={0}'.format(url))
        shares = int(r.json()['share']['share_count'])
    except Exception:
        pass

    return shares


articles = Article.where_raw('created_at >= NOW() - INTERVAL 1 HOUR').order_by('created_at', 'desc').get()

for article in articles:
    article.facebook_shared = get_facebook_shares(article.url)
    print(article.url + ' ' + str(article.facebook_shared))
    article.save()
    sleep(3)
