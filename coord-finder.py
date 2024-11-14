

# Os valores devem ser inseridos sem sinal.

coordinates = [-15.3370333, -52.2526429]

# O códdigo começa aqui.

decimal_values = [i / 1000 for i in range(60000)] # Lista de valores decimais

abs_coordinates = [abs(coord) for coord in coordinates]
degrees = [int(coord) for coord in abs_coordinates]


found = False

with open("output.txt", "w") as file:

    for i in range(2):

        # Obtém valores para testar
        test1 = str(abs_coordinates[i])
        test2 = test1[:-1] + (test1[-1] if test1[-1] == '9' else str(int(test1[-1]) + 1))


        # Realiza o teste de força bruta.

        g = degrees[i]
        
        for m in range (59):

            for s in decimal_values:

                candidate = g + m/60 + s/3600

                candidate = str(f"{candidate:.7f}")

                file.write(f"Testando: g = {g}, m = {m}, s = {s:.3f} contra {test1} ou {test2} com candidato {candidate}\n")
                
                if candidate == test1 or candidate == test2:
                    print(f"Encontrado! Podemos obter {candidate} com g = {g}, m = {m}, s = {s:.3f}")
                    
                    found = True
                    break 

                if found:
                    break

            if found:
                break
        if not found:
            print(f"Nenhuma solução encontrada para {candidate}")
        found = False


    