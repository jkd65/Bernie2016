from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Title
from .forms import TitleForm

# Create your views here.

def splash(request):
	return render(request, 'policies/splash.html', {})

def table_of_contents(request):
	titles = Title.objects.filter(published_date__lte=timezone.now()).order_by('name')
	return render(request, 'policies/table_of_contents.html', {'titles': titles})

def content_detail(request, pk):
	title = get_object_or_404(Title, pk=pk)
	return render(request, 'policies/content_detail.html', {'title': title})

@login_required
def content_edit(request, pk):
	title = get_object_or_404(Title, pk=pk)
	if request.method == "POST":
		form = TitleForm(request.POST, instance=title)
		if form.is_valid():
			title = form.save(commit=False)
			title.author = request.user
			title.published_date = timezone.now()
			title.save()
			return redirect('policies.views.content_detail', pk=title.pk)
	else:
		form = TitleForm(instance=title)
	return render(request, 'policies/content_edit.html', {'form': form})