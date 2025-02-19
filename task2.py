class DataPreprocessor:
    def __init__(self, method, feuture_count):
        self.method = method
        self.feuture_count = feuture_count

    def __str__(self):
        return f"Prepocessor using {self.method} on {self.feuture_count} feuture"


ADAM = DataPreprocessor('optimization', 100)
print(ADAM)
