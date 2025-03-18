from django.contrib import admin
from .models import Post

# 관리자 페이지에서 Post 모델을 확인할 수 있도록 등록
admin.site.register(Post)
