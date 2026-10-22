"""
Day 16 - 2026-10-22
Tool: Number to Words Converter
What it does: Turns a number like 1250 into words - 'one thousand two
hundred fifty' - the way amounts are written out on cheques, invoices
and receipts, so the written amount can be checked against the digits.
Who it helps: Anyone writing a cheque, preparing an invoice, filling
in a bank form, or learning English number words.
"""

ONES = ["zero", "one", "two", "three", "four", "five", "six", "seven",
        "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen",
        "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
TENS = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy",
        "eighty", "ninety"]


def under_thousand(n):
    """Words for a number from 0 to 999."""
    parts = []
    if n >= 100:
        parts.append(ONES[n // 100] + " hundred")
        n %= 100
    if n >= 20:
        parts.append(TENS[n // 10])
        if n % 10:
            parts.append(ONES[n % 10])
    elif n > 0 or not parts:
        parts.append(ONES[n])
    return " ".join(parts)


def number_to_words(n):
    """Words for a whole number from 0 to 999,999,999."""
    if not isinstance(n, int) or isinstance(n, bool):
        raise ValueError("Please give a whole number.")
    if n < 0:
        raise ValueError("Negative numbers are not supported.")
    if n > 999_999_999:
        raise ValueError("Number is too big (max 999,999,999).")
    if n == 0:
        return "zero"
    parts = []
    millions, rest = divmod(n, 1_000_000)
    thousands, rest = divmod(rest, 1_000)
    if millions:
        parts.append(under_thousand(millions) + " million")
    if thousands:
        parts.append(under_thousand(thousands) + " thousand")
    if rest:
        parts.append(under_thousand(rest))
    return " ".join(parts)


def taka_in_words(amount):
    """'Taka <words> only' - the line written on a cheque."""
    return "Taka " + number_to_words(amount) + " only"


if __name__ == "__main__":
    # Example 1: a small shop bill
    print(350, "->", number_to_words(350))
    # Example 2: a cheque amount
    print(taka_in_words(1250))
    # Example 3: a bigger amount, like a phone price
    print(taka_in_words(18500))
    print(999999, "->", number_to_words(999999))
