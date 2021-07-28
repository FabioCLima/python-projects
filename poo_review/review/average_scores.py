# Procedural programming

def average(numbers):
    """[Média de números]

    Args:
        numbers ([lista(float)]): [lista de números]

    Returns:
        [float]: [Média da lista de "scores"]
    """
    return sum(numbers) / len(numbers)


scores = [85, 95, 98, 87, 80, 92]
print(f"The final score is {average(scores)}.")
