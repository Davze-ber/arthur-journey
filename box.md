import textwrap

def draw_box(width, text):
    inner_width = width - 4  # "X " + " X"

    print("X" * width)

    lines = textwrap.wrap(text, inner_width)

    for line in lines:
        padding = inner_width - len(line)
        print("X " + line + " " * padding + " X")

    print("X" * width)


text = "This is a long sentence that should wrap nicely inside the box."

draw_box(20, text)