from rest_framework.pagination import PageNumberPagination
class QuizPagePagination(PageNumberPagination):
    page_size_query_param = 'page_size'

    MAX_PAGINATE_BY: 100
