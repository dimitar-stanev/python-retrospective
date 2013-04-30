from collections import deque

def groupby(func, seq):
	returndictionary = {}
	for item in seq:
		result = func(item)
		if result in returndictionary.keys():
			returndictionary.setdefault(result, []).append(item)
		else:
			returndictionary.update({result:[item]})
	return returndictionary

def iterate(func):
    def compose(func1, func2):
        return lambda arg: func1(func2(arg))

    current_func = lambda arg: arg

    while True:
        yield current_func
        current_func = compose(func, current_func)
		
def zip_with(func, *iterables):
    return (func(*ntuple) for ntuple in zip(*iterables))

def cache(func, cache_size):
    cache = deque(maxlen=cache_size)

    def func_cached(*args):
        for cached_args, cached_value in cache:
            if cached_args == args:
                return cached_value

        result = func(*args)
        cache.append((args, result))
        return result

    return func_cached