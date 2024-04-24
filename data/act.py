import scraiping
import time

for i in range(128, 1000):
    if i == 1:
        scraiping.page("")
    else:
        scraiping.page("?page=" + str(i))

    print(i)
    time.sleep(5)
