# National Identity Card Parser

A program which can parse through a Sri Lankan Identity Card,
and get various information about the card holder.

---
---

## How does it Work?

---

### Old Version

> Old NICs have 9 digits and a character.
>
>   1. First 2 digits tell the birth year of the card holder.
>   2. Next three digits tell the gender. (Male if less than 500, Else female.)
>   3. Birth month and day can also be discovered through the same three numbers.
>   4. Last character tells whether the holder is a voter or not (V for Voters, X if not).

---

### New Version

> New NICs have 12 digits in total.
>
>   1. First 4 digits tell the birth year of the holder.
>   2. Next three digits tell the gender (Same as the old version).
>   3. Same three numbers would be able to tell the birth month and day.

---
---
