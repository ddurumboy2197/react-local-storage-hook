import json

def useLocalStorage(key, initialValue):
    def save(value):
        with open(f'{key}.json', 'w') as f:
            json.dump(value, f)

    def load():
        try:
            with open(f'{key}.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return initialValue

    value = load()
    save(value)

    def update(newValue):
        nonlocal value
        value = newValue
        save(value)

    return value, update
