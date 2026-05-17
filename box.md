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

# utils.py

def truncate_text(text, max_length):
    if len(text) > max_length:
        return text[:max_length - 3] + "..."
    return text

def format_line(text, width, side_char="|"):
    usable_width = width - 2
    processed_text = truncate_text(text, usable_width)
    return f"{side_char}{processed_text.center(usable_width)}{side_char}"

def draw_scroll(text_list, width):
    border = "=" * width
    print(border)
    for line in text_list:
        print(format_line(line, width))
    print(border)

def draw_scroll(text, width):
    side_char = "|"
    top_bot_char = "="

    top_bot_line = top_bot_char * width
    print(top_bot_line)
    for line in text: 
        print(side_char + line.center(width-2) +side_char)

    print(top_bot_line)
    
draw_scroll(["Welcome", "to", "Boot.dev"], 15)

print(len("experiece"))