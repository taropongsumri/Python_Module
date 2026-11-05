import random
import typing

players = [
    "bob", "charlie", "alice", "dylan"
]

actions = [
    "run", "eat", "swim", "grab", "sleep", "move", "climb", "use", "release",
]

def consume_event(events: list[tuple[str, str]],) -> typing.Generator[tuple[str, str], None, None]:
    while len(events) > 0:
        index = random.randint(0, len(events) - 1)
        yield events.pop(index)

def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    while True:
        name = random.choice(players)
        action = random.choice(actions)
        yield (name, action)

def main() -> None:
    print("=== Game Data Stream Processor ===")
    gen = gen_event()

    for i in range(1000):
        name, action = next(gen)
        print(f"Event {i}: Player {name} did action {action}")

    events = []
    for _ in range(10):
        events.append(next(gen))

    print(f"Built list of 10 events: {events}")

    for event in consume_event(events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events}")


if __name__ == "__main__":
    main()