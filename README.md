# Python Wrapper for AbeBooks.com REST API

## Usage

Search book prices by ISBN:

```python
from abebooks import AbeBooks

ab = AbeBooks()
results = ab.getPriceByISBN(9780062941503)
if results['success']:
    best_new = results['pricingInfoForBestNew']
    best_used = results['pricingInfoForBestUsed']

# Best New Price
print(best_new['bestPriceInPurchaseCurrencyWithCurrencySymbol'])
# Best Used Price
print(best_used['bestPriceInPurchaseCurrencyWithCurrencySymbol'])
```
