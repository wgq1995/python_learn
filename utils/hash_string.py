# python自带的hash函数会在多次运行时无法保证一致性，通过设置PYTHONHASHSEED解决这个问题
import os
import sys

def ensure_pythonhashseed(seed=0):
    current_seed = os.environ.get("PYTHONHASHSEED")

    seed = str(seed)
    if current_seed is None or current_seed != seed:
        print(f'Setting PYTHONHASHSEED="{seed}"')
        os.environ["PYTHONHASHSEED"] = seed
        # restart the current process
        os.execl(sys.executable, sys.executable, *sys.argv)

ensure_pythonhashseed()
a = 'a'
print(hash(a))
