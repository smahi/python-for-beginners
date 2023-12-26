# To create a directory
import os


if not os.path.exists('test_dir'):
    os.mkdir('test_dir')


# list directory content
print(os.listdir('.'))
print(os.listdir('/home/smahi/Music'))