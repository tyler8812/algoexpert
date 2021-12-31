def arrayOfProducts(array):
    # O(n) time O(n) space
    products = [1 for _ in array]

    currentProduct = 1
    for i in range(len(array)):
        products[i] *= currentProduct
        currentProduct *= array[i]
    currentProduct = 1
    for i in reversed(range(len(array))):
        products[i] *= currentProduct
        currentProduct *= array[i]

    return products
