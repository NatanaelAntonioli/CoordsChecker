

coordinates = []

coordinates.append([-5.1689538, -52.6662378]) # Teste 1, em que consideramos coordenadas certamente obtidas com g,m,s
coordinates.append([-30.4227334 , -49.2147833]) # Teste 2, em que consideramos coordenadas certamente obtidas com g,m
coordinates.append([-21.7080000,-44.9815000]) # Teste 3, Coordenada A, em São Thomé das Letras
coordinates.append([-23.9542030,-47.4387690]) # Teste 4, Coordenada B, em Tapiraí
coordinates.append([-15.3370333,-52.2526429]) # Teste 5, Coordenada C, na Serra do Roncador
 
# O códdigo começa aqui.

def guess_numbers(list, index):

    print(f"-------------- Testando para o caso {index + 1} -------------------")

    decimal_values = [i / 1000 for i in range(60000)] # Lista de valores decimais

    abs_coordinates = [abs(coord) for coord in list[index]]
    degrees = [int(coord) for coord in abs_coordinates]

    print(abs_coordinates)


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

                    #file.write(f"Testando: g = {g}, m = {m}, s = {s:.3f} contra {test1} ou {test2} com candidato {candidate}\n")
                    
                    if candidate == test1 or candidate == test2:
                        print(f"Encontrado! Podemos obter {abs_coordinates[i]:.7f} com g = {g}, m = {m}, s = {s:.3f}")
                        
                        found = True
                        break 

                    if found:
                        break

                if found:
                    break
            if not found:
                print(f"Nenhuma solução encontrada para {abs_coordinates[i]:.7f} ")
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

                #file.write(f"Testando: g = {g}, m = {m:.3f} contra {test1} ou {test2} com candidato {candidate}\n")
                    
                if candidate == test1 or candidate == test2:
                    print(f"Encontrado! Podemos obter {abs_coordinates[i]:.7f} com g = {g}, m = {m:.3f}")
                    found = True

                if found:
                    break

            if not found:
                print(f"Nenhuma solução encontrada para {abs_coordinates[i]:.7f}")

            found = False

for i in range(5):
    guess_numbers(coordinates,i)