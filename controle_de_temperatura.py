celsius_list = []

while True:
    entrada = input("Digite a temperatura em Celsius (ou 'sair'): ").lower()
    if entrada == "sair":
        break
    celsius_list.append(float(entrada))

if celsius_list:
    # Conversão usando List Comprehension
    fahrenheit_list = [(c * 1.8 + 32) for c in celsius_list]
    
    media_c = sum(celsius_list) / len(celsius_list)
    media_f = sum(fahrenheit_list) / len(fahrenheit_list)
    
    print(f"\nMédia em Celsius: {media_c:.2f}°C")
    print(f"Média em Fahrenheit: {media_f:.2f}°F")
else:
    print("Nenhuma temperatura inserida.")