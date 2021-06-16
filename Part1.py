def solve():
  print("solving part 1")
  with open("moduleWeights.txt", "r") as f:
    weightsText = f.read()
    module_int = weightsText.split("\n")
    
    total_fuel = 0
    for module in module_int:
      total_fuel += int((int(module)/3) - 2 )
    print(total_fuel)
pass
