"""
Indian Number to Words Converter
Supports: Crore, Lakh, Thousand, Hundred, Rupees and Paise system
Range: 0 to 99,99,99,99,999.99
"""

ONES = [
    '', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine',
    'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen',
    'Seventeen', 'Eighteen', 'Nineteen'
]

TENS = [
    '', '', 'Twenty', 'Thirty', 'Forty', 'Fifty',
    'Sixty', 'Seventy', 'Eighty', 'Ninety'
]


def _two_digits_to_words(n: int) -> str:
    """Convert a number 0-99 to words."""
    if n == 0:
        return ''
    elif n < 20:
        return ONES[n]
    else:
        ten = TENS[n // 10]
        one = ONES[n % 10]
        return f"{ten} {one}".strip() if one else ten


def _three_digits_to_words(n: int) -> str:
    """Convert a number 0-999 to words."""
    if n == 0:
        return ''
    hundred = n // 100
    remainder = n % 100
    parts = []
    if hundred:
        parts.append(f"{ONES[hundred]} Hundred")
    if remainder:
        parts.append(_two_digits_to_words(remainder))
    return ' '.join(parts)


def number_to_indian_words(n: int) -> str:
    """
    Convert an integer to Indian number system words.
    Indian system: ones, thousands, lakhs, crores (groups of 2 after thousands)
    """
    if n == 0:
        return 'Zero'

    parts = []

    # Extract groups in Indian number system
    crore = n // 10_000_000
    n %= 10_000_000

    lakh = n // 100_000
    n %= 100_000

    thousand = n // 1_000
    n %= 1_000

    remainder = n

    if crore:
        crore_words = _three_digits_to_words(crore)
        # Handle numbers like 100 Crore, 200 Crore etc.
        parts.append(f"{crore_words} Crore")

    if lakh:
        parts.append(f"{_two_digits_to_words(lakh)} Lakh")

    if thousand:
        parts.append(f"{_two_digits_to_words(thousand)} Thousand")

    if remainder:
        parts.append(_three_digits_to_words(remainder))

    return ' '.join(parts)


def format_indian_number(n: float) -> str:
    """
    Format a number with Indian comma system.
    Example: 1234567 -> '12,34,567'
    Example: 1234567.89 -> '12,34,567.89'
    """
    # Split integer and decimal parts
    int_part = int(n)
    decimal_part = round(n - int_part, 2)

    s = str(int_part)

    # Indian formatting: last 3 digits, then groups of 2
    if len(s) <= 3:
        formatted = s
    else:
        last_three = s[-3:]
        rest = s[:-3]
        # Add commas every 2 digits from right in the 'rest' part
        groups = []
        while len(rest) > 2:
            groups.append(rest[-2:])
            rest = rest[:-2]
        if rest:
            groups.append(rest)
        groups.reverse()
        formatted = ','.join(groups) + ',' + last_three

    if decimal_part > 0:
        paise_str = f"{decimal_part:.2f}"[1:]  # Get ".89" part
        return formatted + paise_str

    return formatted


def convert_to_words(
    number: float,
    currency_symbol: str = "Rupees",
    include_paise: bool = True,
    include_only_suffix: bool = True
) -> str:
    """
    Main conversion function. Converts a float to Indian Rupees words.

    Args:
        number: The amount to convert (e.g., 150000.50)
        currency_symbol: "Rupees", "Rs.", "₹", or "INR"
        include_paise: Whether to include paise for decimal values
        include_only_suffix: Whether to append "Only" at the end

    Returns:
        String like "Rupees One Lakh Fifty Thousand and Fifty Paise Only"
    """
    if number == 0:
        result = f"{currency_symbol} Zero"
        if include_only_suffix:
            result += " Only"
        return result

    # Round to 2 decimal places to avoid float precision issues
    number = round(number, 2)

    rupees = int(number)
    paise = round((number - rupees) * 100)

    # Convert rupees part
    rupees_words = number_to_indian_words(rupees)

    parts = []

    if rupees > 0:
        parts.append(f"{currency_symbol} {rupees_words}")

    # Convert paise part
    if include_paise and paise > 0:
        paise_words = _two_digits_to_words(paise)
        if rupees > 0:
            parts.append(f"and {paise_words} Paise")
        else:
            parts.append(f"{paise_words} Paise")
    elif rupees == 0 and paise == 0:
        parts.append(f"{currency_symbol} Zero")

    result = ' '.join(parts)

    if include_only_suffix:
        result += " Only"

    return result
