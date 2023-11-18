import crud

crud.createSala(19)
crud.createSala(14)
crud.createSala(16)
crud.createSala(12)
crud.createSala(13)

crud.createEnfermeiro("1980/05/02", "Ana", "@gmail.com")
crud.createEnfermeiro("1989/09/30", "Lucas", "lucas@example.org")
crud.createEnfermeiro("2000/02/12", "Julia", "julia@hotmail.com")
crud.createEnfermeiro("1978/11/07", "Pedro", "pedro@yahoo.com")
crud.createEnfermeiro("1985/03/21", "Mariana", "mariana@gmail.com")
crud.createEnfermeiro("1992/08/15", "Carlos", "carlos@example.com")

crud.createInstrumentador("1995/06/18", "Isabel", "isabel@example.com")
crud.createInstrumentador("1983/04/09", "Rafael", "rafael@gmail.com")
crud.createInstrumentador("1976/12/25", "Fernanda", "fernanda@yahoo.com")
crud.createInstrumentador("2002/10/08", "Gabriel", "gabriel@hotmail.com")
crud.createInstrumentador("1990/03/14", "Camila", "camila@example.org")

crud.createAnestesista("1987/07/23", "Eduardo", "eduardo@example.com")
crud.createAnestesista("2001/07/06", "Larissa", "larissa@example.org")
crud.createAnestesista("1974/09/02", "Vanessa", "vanessa@gmail.com")
crud.createAnestesista("2005/01/30", "Diego", "diego@yahoo.com")


crud.createCirurgiao("1982/11/11", "Patricia", "patricia@hotmail.com")
crud.createCirurgiao("1998/08/04", "Gustavo", "gustavo@example.org")
crud.createCirurgiao("1979/05/27", "Amanda", "amanda@example.com")
crud.createCirurgiao("2003/02/19", "Rodrigo", "rodrigo@gmail.com")
crud.createCirurgiao("1993/10/12", "Carolina", "carolina@yahoo.com")

crud.createEspecializacao("Transplante de órgãos")
crud.createEspecializacao("Olhos")
crud.createEspecializacao("Redução de peso")
crud.createEspecializacao("Intestino")

crud.createTipo_Cirurgia("Transplante de Coração","120000",1)
crud.createTipo_Cirurgia("Remoção de Catarata","4000",2)
crud.createTipo_Cirurgia("bariátrica","30000",3)
crud.createTipo_Cirurgia("Transplante Renal","4000",1)
crud.createTipo_Cirurgia("Hérnia Inguinal","3000",4)

crud.createPerfilDeAcesso("1234","master",1)

crud.createEspecializacao_Cirurgiao(1,1)
crud.createEspecializacao_Cirurgiao(1,2)
crud.createEspecializacao_Cirurgiao(2,1)
crud.createEspecializacao_Cirurgiao(2,1)
crud.createEspecializacao_Cirurgiao(3,3)
crud.createEspecializacao_Cirurgiao(4,4)