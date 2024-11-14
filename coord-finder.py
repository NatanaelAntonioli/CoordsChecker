

# Os valores devem ser inseridos sem sinal.

#coordinates = [-5.1689538, -52.6662378] # Primeiro teste, em que consideramos coordenadas certamente obtidas com g,m,s
#coordinates = [-30.4227334 , -49.2147833] # Primeiro teste, em que consideramos coordenadas certamente obtidas com g,m
#coordinates = [-21.7080000,-44.9815000] # Coordenada A, em São Thomé das Letras
#coordinates = [-23.9542030,-47.4387690] # Coordenada B, em Tapiraí
#coordinates = [-15.3370333,-52.2526429] # Coordenada C, na Serra do Roncador
 
# O códdigo começa aqui.

decimal_values = [i / 1000 for i in range(60000)] # Lista de valores decimais

abs_coordinates = [abs(coord) for coord in coordinates]
degrees = [int(coord) for coord in abs_coordinates]


found = False

# Teste para g, m, s

with open("trails-gms.txt", "w") as file:

    print("Testando com g, m s:")

    for i in range(2):

        # Obtém valores para testar
        test1 = f"{abs_coordinates[i]:.7f}"
        test2 = test1[:-1] + str(int(test1[-1]) - 1) if test1[-1] != '0' else test1


        # Realiza o teste de força bruta.

        g = degrees[i]
        
        for m in range (59):

            for s in decimal_values:

                candidate = g + m/60 + s/3600

                candidate = str(candidate)
                candidate = candidate[:candidate.index('.') + 8]

                file.write(f"Testando: g = {g}, m = {m}, s = {s:.3f} contra {test1} ou {test2} com candidato {candidate}\n")
                
                if candidate == test1 or candidate == test2:
                    print(f"Encontrado! Podemos obter {abs_coordinates[i]} com g = {g}, m = {m}, s = {s:.3f}")
                    
                    found = True
                    break 

                if found:
                    break

            if found:
                break
        if not found:
            print(f"Nenhuma solução encontrada para {candidate}")
        found = False

# Teste para g, m

found = False

with open("trials-gm.txt", "w") as file:

    print("Testando com g, m:")

    for i in range(2):

        # Obtém valores para testar
        test1 = f"{abs_coordinates[i]:.7f}"
        test2 = test1[:-1] + str(int(test1[-1]) - 1) if test1[-1] != '0' else test1


        # Realiza o teste de força bruta.

        g = degrees[i]
        
        for m in decimal_values:

            candidate = g + m/60

            candidate = str(candidate)
            candidate = candidate[:candidate.index('.') + 8]

            file.write(f"Testando: g = {g}, m = {m:.3f} contra {test1} ou {test2} com candidato {candidate}\n")
                
            if candidate == test1 or candidate == test2:
                print(f"Encontrado! Podemos obter {abs_coordinates[i]} com g = {g}, m = {m:.3f}")
                found = True

            if found:
                break

        if not found:
            print(f"Nenhuma solução encontrada para {abs_coordinates[i]}")

        found = False
