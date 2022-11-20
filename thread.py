import threading

ranges = [
        [10, 20],
        [1, 5],
        [70, 80],
        [27, 92],
        [0, 16]
        ]  
threads = []

def main():     
    result = [0] * len(ranges)
    for i in range(len(ranges)):
        thread = threading.Thread(target=sum_range, args=(ranges[i][0], ranges[i][1], result, i))
        threads.append(thread)
        thread.start()
    for t in threads:
        t.join()
    print(result)
    print(sum(result))
    
def sum_range(start, end, arr, index):
     arr[index] = int(((end - start + 1) * start) + (((end - start) * (end - start + 1)) / 2))

if __name__ == "__main__":
    main()