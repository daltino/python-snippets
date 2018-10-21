values = [x / (x - y)
          for x in range(100)
          if x > 50
          for y in  range(100)
          if x - y != 0]

values_triangle = [(x, y) for x in range(10) for y in range(x)]

vals = [[y * 3 for y in range(x)] for x in range(10)]

print(values)
print(values_triangle)
print(vals)