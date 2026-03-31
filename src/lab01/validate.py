def validate_name(self, value, field_name):
        if not isinstance(value, str):
            raise TypeError(f"{field_name} должен быть строкой")
        if not value.strip():
            raise ValueError(f"{field_name} не может быть пустым")
        
def validate_year(self, value, field_name, min_year=0, max_year=None, allow_none=False):
    if allow_none and value is None:
        return
    if not isinstance(value, int):
        raise TypeError(f"{field_name} должен быть целым числом")
    if value < min_year:
        raise ValueError(f"{field_name} не может быть < {min_year}")
    if max_year and value > max_year:
        raise ValueError(f"{field_name} не может быть > {max_year}")
    
def validate_country(self, value):
    if not isinstance(value, str):
        raise TypeError("тип должен быть str")

def validate_genre(self, value):
    if not isinstance(value, str):
        raise TypeError("тип должен быть str")

def validate_count_books(self, value):
    if not isinstance(value, int):
        raise TypeError("кол-во должно быть целым числом")
    if value < 0:
        raise ValueError("кол-во не может быть < 0")
