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
	returnlist = range(1,1000)
	for i in returnlist:
		yield func(func) # doesn't really seem to work
		
def zip_with(func, *iterables):
	for i in range(0, len(iterables[0])):
		buffer_list = list()
		for j in range (0, len(iterables)):
			buffer_list.append(iterables[j][i])
		yield func(*buffer_list)

def cache(func, cache_size):
	def cached_func(x):
		cached_list = list()
		result = func(x)
		if result not in cached_list:
			cached_list.append(result)
		else:
			cached_list.pop()
			cached_list.append(result)
		print(result)
	return cached_func
