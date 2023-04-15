def subtract_arrays(arr1, arr2):
    if len(arr1) != len(arr2):
        raise ValueError('Длины массивов не равны!')

    result = []
    for i in range(len(arr1)):
        result.append(arr1[i] - arr2[i])

    return result


if __name__ == '__main__':
    arr1 = [1, 3, 5, 7, 9]
    arr2 = [2, 4, 6, 8, 10]
    arr3 = [1, 2, 3]

    try:
        result1 = subtract_arrays(arr1, arr2)
        print(result1)  # должен вывести: [-1, -1, -1, -1, -1]

        result2 = subtract_arrays(arr1, arr3)
        print(result2)
    except ValueError as e:
        print(e)  # должен вывести: "Длины массивов не равны!"

