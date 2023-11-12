import crud
#METODO DO GRÁFICO - VOU APAGAR DEPOIS QUE ESTIVER FUNCIONANDO NA MAIN


#def tetse():
#    Agendadas = 0
#    Canceladas = 0
#    Concluidas = 0
#    todosIds = crud.obter_IDs_TodasCirurgias()
#    #print(len(todosIds)-1)
#    #print(todosIds)
#    for idCirurgia in todosIds:
#            print(idCirurgia)
#            print(crud.read("CIRURGIA", "*", idCirurgia))
#            retornoStatus = crud.read("CIRURGIA", "STATUS", idCirurgia)
#            match retornoStatus[0][0]:
#                case 1:
#                    Agendadas += 1
#                case 2: 
#                    Concluidas +=1
#                case 3: 
#                    Canceladas +=1
#        
#print(tetse())

#crud.createEspecializacao("Cérrebro")
#crud.createSala(23)
#crud.createPerfilDeAcesso("1","a",1)
#crud.createEnfermeiro("1980/05/02", "Ana", "@gmail.com")
#crud.createEnfermeiro("1975/01/02", "Valentina", "val@gmail.com")
#crud.createInstrumentador("1980/09/02", "Maike", "@gmail.com")
#crud.createAnestesista("1980/01/05", "Durval", "@gmail.com")
#crud.createCirurgiao("1989/03/13", "Ricardo", "r@gmail.com")
#crud.createTipo_Cirurgia("Aorta", "5000", 1)
#crud.createEspecializacao_Cirurgiao(1,1)
#crud.createRecepcionista("1985/04/10", "Mario", "mario@gmail.com", 1)
#crud.createPaciente("Claudio", "1976/03/02","Av. Brasil 198", "12345678912", "cl@gmail.com", 1)
#crud.createCirurgia("2023/02/03 06:03:03", "2023/02/03 12:03:03", 1,1,1,1,1,1,1)
#crud.createTelefone(19,"985919213", 3, 1)
#crud.createCirurgia_Enfermeiro(1,1)
#crud.delete("cirurgia", 1)

#crud.deletaCirurgia(5)

crud.createCirurgia("2023/02/03 06:03:03", "2023/02/03 12:03:03", 1,1,1,1,1,1,1)
