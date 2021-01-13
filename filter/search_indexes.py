from haystack import indexes
from .models import Filter


class FilterIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.NgramField(document=True, use_template=True, template_name='filter/filter_text.txt')
    is_dhaka = indexes.BooleanField(model_attr='is_dhaka')
    is_khulna = indexes.BooleanField(model_attr='is_khulna')
    is_male = indexes.BooleanField(model_attr='is_male')
    is_female = indexes.BooleanField(model_attr='is_female')
    pub_date = indexes.DateTimeField(model_attr='pub_date')

    def get_model(self):
        return Filter

    def index_queryset(self, using=None):
        # filter(pub_date__lte=datetime.now()
        return self.get_model().objects.all()
