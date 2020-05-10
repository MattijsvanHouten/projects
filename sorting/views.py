from django.shortcuts import render
from . import sorting as sort
from timeit import default_timer as timer

rand = sort.randomizer()
sort = sort.sort()

def index(request):
    nums = rand.randomize(0, 10000, 10000)

    start = timer()
    sorted_nums = sort.merge_sort(nums)
    end = timer()

    timeElapsed = end - start

    context = {
        'time': timeElapsed
    }

    return render(request, 'sorting_index.html', context)