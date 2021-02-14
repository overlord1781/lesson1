product = {
    'name' : 'Iphone XS',
    'stock' : 5,
    'price' : 65000,
    'discount': 50
}

def discounted(price,discount, max_discount = 80):
    max_discount = abs(float(max_discount))
    price = abs(float(price))
    discount = abs(float(discount))
    if max_discount >=  90:
        raise ValueError('Ошибка по скидке!!!')

    if discount >= max_discount:
        price_with_discount = price
    else:
        price_with_discount = price-price*discount/100

    return price_with_discount

product['price_with_discounted'] = discounted(product['price'],product['discount'])
print(product)
