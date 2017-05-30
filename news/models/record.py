import shortuuid
from models import Article, Tag

class Record():
	tags = []

	sources = {
		'zanoza': 1,
		'kloop': 2,
		'akipress': 3,
		'twentyfour': 4,
		'knews': 5,
	}

	def __init__(self, source, title, url):
		self.url = url
		self.title = title
		self.source_id = self.sources[source]

	def setTags(self, tags):
		self.tags = tags

	def save(self):
		if not self.title or not self.url:
			return False

		article = Article.first_or_new(source_id=self.source_id, url=self.url, title=self.title)
		if hasattr(article, 'id'):
			return False

		tag_ids = []
		for tag_name in self.tags:
			tag = Tag.first_or_create(name=str(tag_name).lower())
			tag_ids.append(tag.id)
		
		while True:
			try:
				article.in_url = shortuuid.uuid()
				article.save()
				break
			except Exception:
				pass

		article.tags().sync(tag_ids)
		return True
