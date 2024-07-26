def flames(player1, player2):
    # Convert names to lowercase and remove common characters
    common_chars = set(player1.lower()) & set(player2.lower())
    remaining_chars1 = [char for char in player1.lower() if char not in common_chars]
    remaining_chars2 = [char for char in player2.lower() if char not in common_chars]

    # Calculate the count of remaining characters
    count = len(remaining_chars1) + len(remaining_chars2)

    # Define the FLAMES array
    flames_array = ['F', 'L', 'A', 'M', 'E', 'S']

    # Remove letters from FLAMES array using the count
    index = 0
    while len(flames_array) > 1:
        index = (index + count - 1) % len(flames_array)
        flames_array.pop(index)

    # Get the result
    result = flames_array[0]

    # Map the result to a status
    status_map = {
        'F': 'Friends',
        'L': 'Lovers',
        'A': 'Affectionate',
        'M': 'Marriage',
        'E': 'Enemies',
        'S': 'Siblings'
    }
    status = status_map[result]

    return status

def main():
    print("Welcome to the FLAMES game!")
    player1 = input("Enter the first player's name: ")
    player2 = input("Enter the second player's name: ")
    status = flames(player1, player2)
    print(f"Status = {status}")

if __name__ == "__main__":
    main()