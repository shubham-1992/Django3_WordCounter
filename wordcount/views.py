from django.http import HttpResponse
from django.shortcuts import render
import operator


def home(request):
    return render(request, 'home.html', {'abc': "How's the Josh"})


def test(request):
    return HttpResponse("<h1>Great Test</h1>")


def about(request):
    return render(request, 'about.html', {'Me': 'SuperMaan'})


def count(request):
    fulltext = request.GET['fulltext']
    print(fulltext)
    wordlist = fulltext.split()
    worddictionary = {}

    for each in wordlist:
        if each not in worddictionary:
            worddictionary[each] = 1
        else:
            worddictionary[each] += 1

    words_sorted = sorted(worddictionary.items(),
                          key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltexting': fulltext, 'num_words': len(wordlist), 'total_worddictionary': worddictionary, 'list_worddictionary': words_sorted})
