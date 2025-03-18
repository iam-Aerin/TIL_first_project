from django.shortcuts import render
from .models import Post
import random
import os
from datetime import datetime
from django.conf import settings

# ✅ 랜덤 능력 3개 선택 함수
def get_random_abilities():
    abilities = [
        "천재적인 창의력", "무한한 인내심", "순발력 최고", "천상의 미각", "운동 신경 만렙",
        "무한 체력", "명석한 두뇌", "강철 멘탈", "리더십", "친화력 갑"
    ]
    return random.sample(abilities, 3)  # ✅ 반드시 3개만 반환

# ✅ 내부 폴더에서만 랜덤 이미지 가져오기
def get_random_images():
    image_folder = os.path.join(settings.MEDIA_ROOT, 'images')
    if not os.path.exists(image_folder):  # 폴더가 없으면 생성
        os.makedirs(image_folder)

    # ✅ 내부 폴더에서 이미지 가져오기 (.jpg, .jpeg, .png 포함)
    local_images = [
        f"{settings.MEDIA_URL}images/{img}" for img in os.listdir(image_folder)
        if img.lower().endswith(('.jpg', '.jpeg', '.png'))
    ]

    # ✅ 내부 이미지가 3개 이상이면 랜덤으로 선택, 부족하면 남는 개수만큼만 출력
    final_images = random.sample(local_images, min(3, len(local_images)))  # 내부 이미지 최대 3개 선택

    return final_images  # ✅ 내부 이미지만 반환

# ✅ 사용자 입력을 받아 랜덤 결과를 반환하는 View 함수
def user_view(request):
    name = ""
    abilities = []  # ✅ 능력 리스트 초기화
    images = []
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # ✅ 현재 시간 포함

    if request.method == "POST":
        name = request.POST.get("name")  # ✅ 사용자가 입력한 이름 받기
        abilities = get_random_abilities()  # ✅ 랜덤한 3개 능력 선택
        images = get_random_images()  # ✅ 내부 랜덤 이미지만 선택

    return render(request, "user.html", {
        "name": name, 
        "abilities": abilities,  # ✅ 능력 전달 확인
        "images": images,  # ✅ 내부 랜덤 이미지만 전달
        "current_time": current_time,  # ✅ 현재 시간 전달
    })


# 게시물 목록을 가져오는 뷰
def post_list(request):
    posts = Post.objects.all().order_by('-created_at')  # 최신 게시물부터 정렬
    return render(request, 'post_list.html', {'posts': posts})
