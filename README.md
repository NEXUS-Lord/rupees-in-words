# 💰 rupees-in-words

Convert any number to Indian Rupees words — Lakh, Crore, Paise system.

Pure Python. Zero dependencies.

## Example

```python
from converter import convert_to_words

result = convert_to_words(150000)
print(result)  # Rupees One Lakh Fifty Thousand Only
```

## Usage

```python
from converter import convert_to_words

convert_to_words(1000000)    # Rupees Ten Lakhs Only
convert_to_words(10000000)   # Rupees One Crore Only
convert_to_words(1500.50)    # Rupees One Thousand Five Hundred and Fifty Paise Only
```

## Hosted API

Don't want to self-host? Use the ready-made API on RapidAPI:

👉 [RupeesInWords API on RapidAPI](https://rapidapi.com/NEXUSLord/api/rupeesinwords-indian-number-to-words)

- No setup required
- Supports batch conversion (up to 50 numbers)
- Indian comma formatting (1,50,000)
- Multiple currency symbols (Rupees, Rs., ₹, INR)

## License

MIT
