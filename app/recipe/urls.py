"""
URL mapping for the recipe app.
"""

from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter

from recipe import views


router = DefaultRouter()
router.register('recipes', views.RecipeViewSet) # otomatik olarak urller olusturuldu bunun sayesinde
router.register('tags', views.TagViewSet)
router.register('ingredients', views.IngredientViewSet)

app_name='recipe'

urlpatterns = [
    path('', include(router.urls)),
]

