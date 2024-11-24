from django.shortcuts import render, redirect, get_object_or_404
from .models import Word
from .forms import WordForm

# 단어 추가 뷰
def add_word(request):
    if request.method == 'POST':
        form = WordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('word_list')
    else:
        form = WordForm()
    return render(request, 'words/add_word.html', {'form': form})

# 단어 삭제 뷰
def delete_word(request, word_id):
    word = get_object_or_404(Word, id=word_id)
    if request.method == 'POST':
        word.delete()
        return redirect('word_list')
    return render(request, 'words/delete_word.html', {'word': word})

# 단어 목록 보기
def word_list(request):
    words = Word.objects.all()
    return render(request, 'words/word_list.html', {'words': words})
