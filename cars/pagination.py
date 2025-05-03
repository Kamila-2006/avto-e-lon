from rest_framework.pagination import PageNumberPagination


class MakePagination(PageNumberPagination):
    page_size = 10


class ModelPagination(PageNumberPagination):
    page_size = 10


class BodyTypePagination(PageNumberPagination):
    page_size = 10


class FeaturePagination(PageNumberPagination):
    page_size = 10


class CarPagination(PageNumberPagination):
    page_size = 10