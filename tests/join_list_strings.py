#join_list_strings.py  

from typing import List

def join(xs: List[int], delimiter: str) -> str:    
    """Produce a string where subsequent itens are separated by delimiter."""
    
    generate_string : str = ""
    for item in xs:
        if generate_string == "": # Don'tput delimiter before the first item
            generate_string = str(item)
        else:  
            generate_string += delimiter + str(item)
    return generate_string

