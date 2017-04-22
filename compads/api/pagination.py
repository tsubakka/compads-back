from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination,
    )


class DefaultLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 10

class DefaultPageNumberPagination(PageNumberPagination):
    page_size = 10

class ClientTypeLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 10


class ClientTypePageNumberPagination(PageNumberPagination):
    page_size = 20
