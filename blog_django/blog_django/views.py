# blog_django/blog_django/views.py
from django.views.generic import ListView
from django.shortcuts import render
from apps.post.models import Post, Category
from apps.post.forms  import PostFilterForm
from django.db.models import Count
from django.contrib.auth.decorators import login_required

class IndexView(ListView):
    template_name = 'index.html'

    model =  Post
    context_object_name= 'posts'
    paginate_by = 9 # Definimos la paginación de 10 posts por página

    def category_view(request):
        categories = Category.objects.all()  # Obtener todas las categorías
        return render(request, 'index.html', {'categories': categories})
    
    def get_queryset(self):
        queryset = Post.objects.all().annotate(comments_count=Count('comments'))
        # Anotamos la cantidad de comentarios en cada post
        
        search_query = self.request.GET.get('search_query', '')
        order_by = self.request.GET.get('order_by', '-creation_date')
        category_filter = self.request.GET.get('category_filter', '')

        # Filtramos por título o autor si se proporciona una búsqueda
        if search_query:
            queryset = queryset.filter(title__icontains=search_query) |queryset.filter(author__username__icontains=search_query)

        if category_filter:
            queryset = queryset.filter(category__slug__icontains=category_filter)

        return queryset.order_by(order_by)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = PostFilterForm(self.request.GET) # Pasamos el formulario de filtro al contexto
        posts_with_images = []
        for post in context['posts']:
            first_image = post.images.filter(active=True).first()
            posts_with_images.append({
                'post': post,
                'first_image': first_image
            })
        context['posts_with_images'] = posts_with_images
        context['categories'] = Category.objects.all()
        
        # Manejamos la paginación
        if context.get('is_paginated', False):
            query_params = self.request.GET.copy()
            query_params.pop('page', None)
            
            pagination = {}
            page_obj = context['page_obj']
            paginator = context['paginator']
            
            # Usamos number para obtener el número de la página actual
            if page_obj.number > 1:
                pagination['first_page'] = f'?{query_params.urlencode()}&page={paginator.page_range[0]}'
            
            # Usamos has_previous para saber si hay una página anterior
            if page_obj.has_previous():
                pagination['previous_page'] = f'?{query_params.urlencode()}&page={page_obj.number - 1}'
                
            # Usamos has_next para saber si hay una página siguiente
            if page_obj.has_next():
                pagination['next_page'] = f'?{query_params.urlencode()}&page={page_obj.number + 1}'
                
            # Usamos num_pages para obtener el número total de páginas
            if page_obj.number < paginator.num_pages:
                pagination['last_page'] = f'?{query_params.urlencode()}&page={paginator.num_pages}'
                
            context['pagination'] = pagination
            
        return context


    # Es importante que el argumento exception esté presente
    # para que Django lo pueda identificar como un manejador de errores

def not_found_view(request, exception):
    return render(request, 'errors/error_not_found.html', status=404)
        
def internal_error_view(request):
    return render(request, 'errors/error_internal.html', status=500)
        
def forbidden_view(request, exception):
    return render(request, 'errors/error_forbidden.html', status=403)

def search(request):
    query = request.GET.get('q')
    results = Post.objects.filter(title__icontains=query)  # Busca posts cuyo título contenga la query
    return render(request, 'search_results.html', {'results': results, 'query': query})


@login_required
def user_profile(request):
    return render(request, 'user/user_profile.html', {'user': request.user})
#Nota: Cada vista está asociada a un template de error correspondiente y devuelve el código de estado HTTP adecuado.


#TODO definir estilos de errores 
"""
Manejo de Errores Personalizados
Veamos cómo manejar los errores 404(Not Found - Recurso no encontrado), 500(Server Error - Error interno del servidor) y 403(Forbidden - Acceso denegado) con templates personalizados.
"""
