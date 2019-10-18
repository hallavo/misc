
import itertools

def list_sum(l: list) -> int:
    sum = 0
    for num in l:
        sum += num
    return sum


# Example:
# input_list = [1,2,3]
#     recipe = [1,2]
#
# partitions(input_list, recipe) = [
#                               [(1,2), (3,)],
#                               [(1,3), (2,)],
#                               [(2,3), (1,)]
#                           ]
#
def partitions_helper(recipe: list, s1: frozenset) -> list:
    n = recipe.head()
    result = []
    combs = itertools.combinations(s1, n)
    for c in combs:
        s2 = frozenset(c)
        d = s1.difference(s2)
        result.append( (s1, partitions_helper(recipe, s) )
    return result


# this function
#   1. performs some checking on the input arguments
#   2. sets up the necessary variables
#   3. calls partitions_helper
def partitions(recipe: list, l: list) -> list:
    if len(l) != list_sum(recipe):
        raise ArgumentError
    result = []
    s = frozenset(l)
    result.append( partitions_helper(recipe, s) )
    return result


    

def test_list_sum(k: int) -> None:
    l = list( range(k) )
    print("list:     ", l) 
    print("list_sum: ", list_sum(l))
    print("")


for i in range(5):
    test_list_sum(i)

# test cases
#
# f(2, [1,2]) = [
#                   [(1,), (2,)]
#               ]
#
# f(1, [1,2]) = [
#                   [(1,2)]
#               ]
#
#
# f(1, [1,2,3]) = [
#                   [(1,), (2,), (3,)]
#                 ]
#
# f(2, [1,2,3]) = [
#                   [(1,2), (3,)],
#                   [(1,3), (2,)],
#                   [(2,3), (1,)]
#                 ]
