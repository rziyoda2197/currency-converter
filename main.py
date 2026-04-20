class ValyutaKonvertori:
    def __init__(self):
        self.valyutalar = {
            "USD": 1,
            "EUR": 0.88,
            "GBP": 0.76,
            "RUB": 74.45,
            "JPY": 109.55,
            "CNY": 6.48
        }

    def konvert(self, valyuta1, summa, valyuta2):
        if valyuta1 not in self.valyutalar or valyuta2 not in self.valyutalar:
            return "Ishlatiladigan valyutalar: USD, EUR, GBP, RUB, JPY, CNY"
        return summa * self.valyutalar[valyuta2] / self.valyutalar[valyuta1]


def main():
    konvertor = ValyutaKonvertori()
    valyuta1 = input("Birinchi valyutani kiriting (USD, EUR, GBP, RUB, JPY, CNY): ")
    summa = float(input("Summani kiriting: "))
    valyuta2 = input("Ikkinchi valyutani kiriting (USD, EUR, GBP, RUB, JPY, CNY): ")
    print(konvertor.konvert(valyuta1, summa, valyuta2))


if __name__ == "__main__":
    main()
