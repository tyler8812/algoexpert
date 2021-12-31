def arrayOfProducts(array):
    # O(n) time O(n) space
    products = [1 for _ in array]
    right_products = [1 for _ in array]
    left_products = [1 for _ in array]

    currentProduct = 1
    for i in range(len(array)):
        left_products[i] *= currentProduct
        currentProduct *= array[i]
    currentProduct = 1
    for i in reversed(range(len(array))):
        right_products[i] *= currentProduct
        currentProduct *= array[i]

    print(left_products)
    print(right_products)
    for i in range(len(right_products)):
        products[i] = right_products[i] * left_products[i]

    return products
