def get_statistics(input_list):
    if len(input_list) == 0:
        return {
            "mean": 0,
            "median": 0,
            "mode": 0,
            "sample_variance": 0,
            "sample_standard_deviation": 0,
            "mean_confidence_interval": [0, 0],
        }
    elif len(input_list) == 1:
        return {
            "mean": input_list[0],
            "median": input_list[0],
            "mode": input_list[0],
            "sample_variance": 0,
            "sample_standard_deviation": 0,
            "mean_confidence_interval": [0, 0],
        }
    n = len(input_list)
    input_list = sorted(input_list)
    s = sum(input_list)
    mean = s / n
    if n % 2 == 1:
        median = input_list[n // 2]
    else:
        median = (input_list[n // 2] + input_list[n // 2 - 1]) / 2
    count_dict = {}
    mode = -1
    mode_count = 0
    for num in input_list:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
        if count_dict[num] > mode_count:
            mode_count = count_dict[num]
            mode = num
    sample_variance = sum([(num - mean) ** 2 for num in input_list]) /(n - 1)
    sample_standard_deviation = sample_variance ** 0.5
    mean_std_err = sample_standard_deviation / n ** 0.5
    mean_confidence_interval = [mean - 1.96 * mean_std_err, mean + 1.96 * mean_std_err]
    return {
        "mean": mean,
        "median": median,
        "mode": mode,
        "sample_variance": sample_variance,
        "sample_standard_deviation": sample_standard_deviation,
        "mean_confidence_interval": mean_confidence_interval,
    }

