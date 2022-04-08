
points = [[1,1],[-1,1]]

class Solution3(object):
    def isReflected(self, points):
        """
        Найти наибольшую и наименьшую горизонтальную координату всех точек, взять центр магазина в качестве оси симметрии
                 Для каждой точки посмотрите, находится ли осесимметричная точка в точках
                 Обратите внимание, что значение dict является набором
        """
        from collections import defaultdict
        dictionary, max_x, min_x = defaultdict(set), -float('inf'), float('inf')
        for x, y in points:
            max_x = max(max_x, x)
            min_x = min(min_x, x)
            dictionary[x].add(y)

        mid = (min_x + max_x) / 2

        print(mid)
        for x, y in points:
            if y  not in dictionary[2*mid - x]:
                return False
        return True
reflect = Solution3()
print(reflect.isReflected(points))