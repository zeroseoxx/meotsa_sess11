from rest_framework import serializers
from .models import Comment
from movies.models import Movie,Actor

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['name', 'character', 'image_url']

class CommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'username', 'content', 'created_at']

#영화 세부 정보 조회 시 코멘트도 함께 
class MovieDetailSerializer(serializers.ModelSerializer): 
    comments = CommentSerializer(many=True, read_only=True)
    actors = ActorSerializer(many=True,read_only=True)



    class Meta:
        model = Movie
        fields = [
            'audience_score', 'critic_score', 'netizen_score',  # 평점
            'genre', 'showtime', 'rating', 'release_date', 'plot',  # 영화 정보
            'actors',  # 인물정보
            'comments',  # 한줄평
            'title_kor', 'title_eng', 'poster_url', 'director_name'  # 필요 시 추가
        ]


