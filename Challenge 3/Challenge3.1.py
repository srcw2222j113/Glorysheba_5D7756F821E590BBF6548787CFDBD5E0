def linear_search_product():
    product_list = input("Enter a list of products separated by commas: ").split(',')
    target_product = input("Enter the target product name: ").strip()
    
    indices = []
    
    for i, product in enumerate(product_list):
        if product.strip() == target_product:
            indices.append(i)
    
    return indices

result = linear_search_product()

if result:
    print(f"The target product was found at indices: {result}")
else:
    print("The target product was not found.")
