import _thread


urls = []


def add_list(value, val):
    print("oi")


try:
    _thread.start_new_thread(add_list, (1, 1))
    _thread.start_new_thread(add_list, (2, 2))
except Exception as e:
    print("error")

print(urls)