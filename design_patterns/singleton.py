class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


if __name__ == "__main__":
    # Przykład użycia
    s1 = Singleton()
    s2 = Singleton()
    print(s1 is s2)  # True