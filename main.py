from morse_code import morse
import time

# equal to 'string.punctuation'
SPECIAL_CHARS = "~:'+[\\@^{%(-\"*|,&<`}._=]!>;?#$)/"


def remove_special_chars(text: str) -> str:
    """
    Removes special (punctuation) characters from any string and returns it. strip() for every word within a paragraph.

    :param text: Takes text as string only
    :return: Natural language text without punctuation
    """
    text_as_list = text.split()
    formatted_text = []

    for word in text_as_list:
        word = word.strip(SPECIAL_CHARS)
        formatted_text.append(word)

    formatted_text = " ".join(formatted_text)
    return formatted_text


def text_to_morse(f_text: str):
    """
    Converts plaintext to 'morse code'. Requires predefined 'morse code' dictionary with ASCII letters and morse chars.

    :param f_text: Formatted text without punctuation characters.
    :return: Prints a string of 'morse code' characters to terminal.
    """
    morse_text = " ".join([morse[char] for char in f_text])
    print(f"\nMorse code: \n{morse_text}")


def stop_converter():
    global convertor_is_on
    convertor_is_on = False


# Program presentation
print("Text to Morse\n")
time.sleep(1.5)
print("Enter 'EXIT' at any time to quit the program.")
time.sleep(1)

convertor_is_on = True
while convertor_is_on:
    # Take user input
    user_text = input("\nEnter plaintext to convert: ").upper()
    # Terminate loop if user decides to quit
    if user_text == "EXIT":
        convertor_is_on = False
    else:
        # 'text_to_morse' takes the return value of 'remove_special_chars'
        text_to_morse(remove_special_chars(user_text))
