

def compare_version(v1,v2):

	if float(v1) > float(v2):
		return f'Version {v1} is greater than Version {v2}'

	elif float(v1) < float(v2):
		return f'Version {v1} is lesser than Version {v2}'

	else:
		return f'Version {v1} is equal than Version {v2}'


