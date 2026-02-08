# Online Sales Analysis

Ovaj projekat je Python aplikacija za upravljanje prodajom u online prodavnici.  
Koristi OOP koncepte i GitHub za verzionisanje i timsku saradnju.

## Klase i funkcionalnosti

### Product
- Atributi: name, price, quantity
- Metodi:
  - `display_info()` - prikazuje informacije o proizvodu
  - `update_quantity(amount)` - mijenja količinu proizvoda

### ProductManager
- Atribut: lista proizvoda
- Metodi:
  - `add_product(product)` - dodaje proizvod
  - `display_products()` - prikazuje sve proizvode
  - `total_inventory_value()` - izračunava ukupnu vrijednost inventara
  - `remove_product(name)` - uklanja proizvod po imenu

### Cart
- Atribut: lista proizvoda u korpi
- Metodi:
  - `add_to_cart(product)` - dodaje proizvod u korpu
  - `display_cart()` - prikazuje sadržaj korpe
  - `total_cart_value()` - izračunava ukupnu vrijednost korpe

## Sigurnost podataka
- `config.json` je ignorisan u Git-u  
- Snimci ekrana se takođe ignorišu

## Autor
- Mirsada Gudic
