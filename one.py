def func():
	print("FUNC() in one.py")

print("TOP LEVEL IN one.py")

if __name__ == '__main__':
	print('ony.py is being run directly')
else:
	print('one.py has been imported')