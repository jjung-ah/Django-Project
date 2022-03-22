from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import User
from .forms import UserForm, ContentForm
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    # return HttpResponse("Hello Django !")
    """
    web 목록 출력
    """
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지

    # 조회
    user_list = User.objects.order_by('-create_date')

    # 페이징처리
    paginator = Paginator(user_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'user_list': page_obj}
    # context = {'user_list': user_list}
    return render(request, 'web/user_list.html', context)

def detail(request, user_id):
    """
    web 내용 출력
    """
    # user = User.objects.get(id=user_id)
    user = get_object_or_404(User, pk=user_id)
    context = {'user': user}
    return render(request, 'web/user_detail.html', context)

def content_create(request, user_id):
    """
    web 요청사항
    """
    # user = get_object_or_404(User, pk=user_id)
    # user.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    # return redirect('web:detail', user_id=user.id)
    user = get_object_or_404(User, pk=user_id)
    if request.method == "POST":
        form = ContentForm(request.POST)
        if form.is_valid():
            content = form.save(commit=False)
            content.create_date = timezone.now()
            content.question = user
            content.save()
            return redirect('web:detail', user_id=user.id)
    else:
        form = ContentForm()
    context = {'user': user, 'form': form}
    return render(request, 'web/user_detail.html', context)


def user_create(request):
    """
    web User등록
    """
    # form = UserForm()
    # return render(request, 'web/user_form.html', {'form': form})
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.create_date = timezone.now()
            user.save()
            return redirect('web:index')
    else:
        form = UserForm()
    context = {'form': form}
    return render(request, 'web/user_form.html', context)