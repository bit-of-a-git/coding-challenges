def delete_nth(order, max_e):
    result = []
    for item in order:
        if result.count(item) < max_e:
            result.append(item)
    return result
