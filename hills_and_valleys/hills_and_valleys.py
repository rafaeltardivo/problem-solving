def solution(n):
    """Finds hills and valleys. The rules are:
    - The number is a valley if it is smaller than it's neighbours;
    - The number is a hills if is greater than it's neighbors;
    - If one of the neighbors is an edge, the condition is automatically
    satisfied.

    Args:
        n (list): list of numbers.
    Returns:
        Number of hills and valleys.
    """
    size = len(n)
    hills_and_valleys = 0

    # edge case: empty list
    if not size:
        return 0
    
    # edge case: only one item or all elements are equal
    if size == 1 or n.count(n[0]) == size:
        return 1

    i = 0
    while(i < size):
        previous = None if i == 0 else n[i - 1]
        current = n[i]

        while previous == current and i < size - 1:
            i += 1
            previous = current
            current = n[i]

        nex = None if i == size - 1 else n[i + 1]

        while nex == current and i < size - 2:
            i += 1
            current = nex
            nex = n[i + 1]
        
        if not previous or not nex:
            hills_and_valleys += 1
        elif previous < current > nex or previous > current < nex:
            hills_and_valleys += 1
        i += 1
    return hills_and_valleys

  
if __name__ == '__main__':
    print(solution([1]))                   # 1
    print(solution([1,2]))                 # 2
    print(solution([1,1,1]))               # 1
    print(solution([1,2,1]))               # 3
    print(solution([1,2,6]))               # 2
    print(solution([1,2,3,4,4,3,4,4,5,6])) # 4
    print(solution([-10,2,2,2,2]))         # 2
    print(solution([1,0,0,0,1]))           # 3
    print(solution([0,1,0,1,0]))           # 5
    print(solution([]))                    # 0





