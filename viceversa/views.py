from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def reverse(request):
    user_text = request.GET['message']
    reversed_text = user_text[::-1]
    len_words = (len(user_text.strip().split(" ")))
    result_len_words = f'{len_words} word' if len_words == 1 else f'{len_words} words'
    return render(request, 'reverse.html', {'message': user_text, 'reversedtext': reversed_text,
                                            'lenwords': result_len_words})
