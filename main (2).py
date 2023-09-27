def linearSearchProduct (ProductList, TargetProduct):
  indices = []
  for index,Product in enumerate(ProductList): 
    if Product == TargetProduct:
     indices.append(index)

  return indices


# Example usage:
Products =["shoes", "boot", "loafer", "shoes", "sandal","shoes"]
Target = "shoes"
Result = linearSearchProduct(Products, Target)
print(Result)