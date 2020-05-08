N = int(input())
hours = (N % 86400) // 3600
minutes = (((N % 86400) % 3600) // 60)
seconds = (((N % 86400) % 3600) % 60)
print(hours, ':', minutes // 10, minutes % 10, ':', seconds // 10,
      seconds % 10, sep='')
