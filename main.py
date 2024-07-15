from module import module
import time
start_time = time.time()

result=module.num(1000000000)

end_time = time.time()
elapsed_time = end_time - start_time

print(f"result {result} {elapsed_time:.2f} seconds")