def get_user_input(text: str, ending_character: str = ":", input_type = str):
    valid_types = [str, float, int]
    if input_type not in valid_types:
        raise ValueError(f"Please give valid input_types, Valid input types are: {str.join(', ', [type.__name__ for type in valid_types])}")
    
    user_input = input(f"{text}{ending_character} ")
    try:
        return input_type(user_input)
    except ValueError:
        raise ValueError(f"Invalid input. Please provide a valid {input_type.__name__} value.")