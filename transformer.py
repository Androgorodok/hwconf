from lark import Transformer


class ConfigTransformer(Transformer):
    def __init__(self):
        self.constants = {}
        self.result = {}

    def number(self, items):
        return int(items[0])

    def string(self, items):
        # Убираем @" и " с начала и конца
        return str(items[0])[2:-1]

    def array(self, items):
        # Фильтруем None значения
        return [item for item in items if item is not None]

    def const_ref(self, items):
        name = str(items[0])
        if name not in self.constants:
            raise ValueError(f"Неизвестная константа: {name}")
        return self.constants[name]

    def statement(self, items):
        name, value = items
        name_str = str(name)
        self.constants[name_str] = value
        self.result[name_str] = value

    def start(self, items):
        return self.result