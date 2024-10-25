from django.urls import path
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
import apps.post.views as views
from .views import UserPostView
from .views import PostCreateView, PostListView, PostDetailView, PostUpdateView, PostDeleteView, CommentCreateView, CommentUpdateView, CommentDeleteView, UserPostView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView, movie_list_view, search

app_name = 'post'

# Aplicamos decoradores de permisos a las vistas basadas en clases
post_create_decorator = method_decorator(login_required, name='dispatch')
post_update_delete_decorator = method_decorator(login_required, name='dispatch')

urlpatterns = [
    path('posts/', PostListView.as_view(), name="post_list"),
    path('posts/create/', PostCreateView.as_view(), name="post_create"),
    path('posts/<slug:slug>/', PostDetailView.as_view(), name="post_detail"),
    path('posts/<slug:slug>/update/', PostUpdateView.as_view(), name="post_update"),
    path('posts/<slug:slug>/delete/', PostDeleteView.as_view(), name="post_delete"),
    path('posts/<slug:slug>/comments/create/', CommentCreateView.as_view(), name='comment_create'),
    path('comments/<uuid:pk>/update/', CommentUpdateView.as_view(), name='comment_update'),
    path('comments/<uuid:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
    path('mis-posts/', UserPostView.as_view(), name='user_posts'),
    path('categories/create/', CategoryCreateView.as_view(), name='category_create'),
    path('categories/<uuid:id>/update/', CategoryUpdateView.as_view(), name='category_update'),
    path('categories/<uuid:id>/delete/', CategoryDeleteView.as_view(), name='category_delete'),
    path('movies/', movie_list_view, name='movie_list'),
    path('search/', search, name='search'),
]


"""
post_list: URL para listar los posts.
post_create: URL para crear un nuevo post.
post_detail: URL para ver un post en detalle.
post_update: URL para actualizar un post.
post_delete: URL para eliminar un post.
"""

#TODO: en admin, crear post

"""
Nota: La URL para editar un comentario se define como //. El parámetro pk se utiliza para identificar el
comentario que se desea editar.
La URL comment_update espera el pk del comentario y apunta a la vista CommentUpdateView.
Importante: El parámetro pk es un campo UUID que se utiliza para identificar de forma única un
comentario.
"""
