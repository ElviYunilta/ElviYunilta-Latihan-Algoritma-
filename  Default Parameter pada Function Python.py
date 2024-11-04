# Default Parameter pada Function Python


def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

# Memanggil fungsi dengan kedua argumen
greet("Alice", "Hi")  # Output: Hi, Alice!

# Memanggil fungsi hanya dengan argumen name
greet("Bob")  # Output: Hello, Bob!