from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_POST, require_http_methods, require_GET
from .models import Review, Comment
from .forms import ReviewForm, CommentForm
from django.http import HttpRequest
from django.contrib.auth import get_user_model

# Create your views here.

# C
@require_http_methods(['GET', 'POST'])
# httprequest만 request로 받겠다라는 선언
def create_review(request:HttpRequest):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save()
                return redirect('community:review_detail', review.pk)
        
        else:
            form = ReviewForm()
        
        context = {
            'form':form,
        }
        return render(request, 'community/create.html', context)
    else:
        return redirect('accounts:login')
# R
@require_safe
def index(request):
    reviews = Review.objects.order_by('-pk')
    context = {
        'reviews':reviews,
    }
    return render(request, 'community/index.html', context)

@require_safe
def review_detail(request:HttpRequest, detail_pk):
    review = get_object_or_404(Review, pk=detail_pk)
    comment_form = CommentForm()
    comments = review.comment_set.all()
    context = {
        'review':review,
        'comment_form':comment_form,
        'comments':comments
    }
    return render(request, 'community/detail.html', context)


@require_POST
def comment_create(request, detail_pk):
    review = get_object_or_404(Review, pk=detail_pk)
    user = get_object_or_404(get_user_model(), pk=request.user.pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.review = review
        comment.user = user
        comment.save()
        return redirect('community:review_detail', detail_pk)
    else:
        return redirect('community:review_detail', detail_pk)


        
