paises = {
    "Brasil": "Brasília",
    "Argentina": "Buenos Aires",
    "França": "Paris",
    "Estados Unidos": "Washington, D.C.",
    "Japão": "Tóquio",
    "Alemanha": "Berlim",
    "Itália": "Roma",
    "Canadá": "Ottawa",
    "Reino Unido": "Londres",
    "México": "Cidade do México"
}

pais = input("Digite o nome do país: ")
capital = paises.get(pais, "País não encontrado")
print("Capital:", capital)