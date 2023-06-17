from collections import defaultdict

n, m = map(int, input().strip().split())

pizza_combs = defaultdict(set)

for _ in range (m):
    ing1, ing2 = sorted(map(int, input().strip().split()))
    pizza_combs[ing1].add(ing2)

def pizza_combiner(num, pizza_combs,  tracker = []):
    if num == 0:
        return 1
    pizzas = 0
    valid = True
    for ing in pizza_combs[num]:
        if ing in tracker:
            valid = False
    pizzas += pizza_combiner(num-1, pizza_combs, tracker)
    if valid:
        pizzas += pizza_combiner(num-1, pizza_combs, tracker+[num])
    return pizzas
    
print(pizza_combiner(n, pizza_combs))
