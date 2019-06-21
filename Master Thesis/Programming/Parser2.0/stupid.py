result = 'Result.txt'
with open('Result2.txt', 'w') as filehandle:
    for listitem in result:
        filehandle.write('%s\n' % listitem)
