from rest_framework import serializers  # Asegúrate de importar desde 'rest_framework'
from .models import Post  # Importa tu modelo Post correctamente

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = ['is_removed', 'created', 'modified']
