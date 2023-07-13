class Student:
    def __init__(self, first_name, last_name, age):
        """
        Args:
            first_name(str)
            last_name(str)
            age(int)
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def to_json(self, attr=None):
        """
        Agrs:
            self(list) for the first instance
            self(str)
            self(int)
            self(bool)
        """
        self.attr = attr
        if isinstance(self.attr, list):
            return [to_json(item) for item in self.attr]
        elif isinstance(self.attr, dict):
            return {to_json(key): to_json(value) for key, value in self.attr.items()}
        elif isinstance(self.attr, str) or isinstance(self.attr, int) or isinstance(self.attr, bool):
            return self.attr
        else:
            return {var: to_json(getattr(self.attr, var))\
                    for var in dir(self.attr) if not var.startswith('__')}
