age = int(input('yoshni kirit: '))

if age < 0:
    print('bunday yosh yoq')

elif age <= 3:
    print('bola hali yosh')

elif age <= 6:
    print('bola bogcha yoshida')

elif age <= 18:
    print('bola maktabda oqiydi')

elif age <= 60:
    print('ishlaydi')

elif age <= 110:
    print('pensioner')

else:
    print('bunday yosh yoq')
