import os

print(f"Current Working Directory is: {os.getcwd()}")
print(os.path.exists('../data'))


print(f"test_dir existing: {os.path.exists('test_dir')}")
if not os.path.exists('test_dir'):
    os.mkdir("test_dir")
    
print(f"test_dir existing: {os.path.exists('test_dir')}")

print(os.listdir('.'))
