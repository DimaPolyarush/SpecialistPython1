# Посчитайте количество согласных букв в данной строке.

text = ("Посчитайте количество согласных букв в данной строке.")
sgl = "цкнгшщзхъфвпрлджчсмтьб"
text_lower = text.lower()
count_sgl=0
for i in text_lower:
    if i in sgl:
        count_sgl+=1
print(count_sgl)
