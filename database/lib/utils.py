

def format_full_name(full_name: tuple) -> str:
    """Преобразует full_name в видео tuple (Имя, Фамилия) в формат строки 'Имя|Фамилия'"""
    if isinstance(full_name, tuple):
        return f"{full_name[0]}|{full_name[1]}"
    return full_name