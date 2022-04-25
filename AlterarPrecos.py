# Created By Julio Melo
import pathlib

def main():
    local = pathlib.Path(__file__).parent.absolute()
    localc = str(local)
    file = "\data.js"
    filexy = localc + file
    mucarela = 0
    calabresa = 0
    portuguesa = 0
    frango = 0
    frangocatupiri = 0
    frangomussarela = 0
    atum = 0
    napolitana = 0
    americana = 0
    camarao = 0
    pepperoni = 0
    quatroqueijos = 0   
    x = (input("Deseja definir o preço de cada pizza? DIGITE: [sim] ou [nao]: "))
    if (x == "sim"):
        print("\nLembre-se os valores são definidos por cada MEIO de pizza.")
        print("\nExemplo: Muçarela = 15 , Se 1 pizza inteira de muçarela valor total será: 30")
        print("Será necessario definir o valor de todas as metades para a atualização.\n")
        mucarela = int(input("Muçarela = "))
        calabresa = int(input("Calabresa = "))
        portuguesa = int(input("Portuguesa = "))
        frango = int(input("Frango = "))
        frangocatupiri = int(input("Frango C/ Catupiri = "))
        frangomussarela = int(input("Frango C/ Mussarela = "))
        atum = int(input("Atum = "))
        napolitana = int(input("Napolitana = "))
        americana = int(input("Americana = "))
        camarao = int(input("Camarao = "))
        pepperoni = int(input("Pepperoni = "))
        quatroqueijos = int(input("Quatro Queijos = "))
        z = input("Valores Definidos, Deseja salvar a alteração? [sim] ou [nao]")
        if (z == 'sim'):
            with open(filexy, "w") as arq:
                arq.truncate()
            closeline = ";\n"
            arquivo = open(filexy, "a+")
            arquivo.write("var mucarela = {}{}".format(mucarela,closeline))
            arquivo.write("var calabresa = {}{}".format(calabresa,closeline))
            arquivo.write("var portuguesa = {}{}".format(portuguesa,closeline))
            arquivo.write("var frango = {}{}".format(frango,closeline))
            arquivo.write("var frangocatupiri = {}{}".format(frangocatupiri,closeline))
            arquivo.write("var frangomussarela = {}{}".format(frangomussarela,closeline))
            arquivo.write("var atum = {}{}".format(atum,closeline))
            arquivo.write("var napolitana = {}{}".format(napolitana,closeline))
            arquivo.write("var americana = {}{}".format(americana,closeline))
            arquivo.write("var camarao = {}{}".format(camarao,closeline))
            arquivo.write("var pepperoni = {}{}".format(pepperoni,closeline))
            arquivo.write("var quatroqueijos = {}{}".format(quatroqueijos,closeline))

            print("Arquivo atualizado.")
    else:
        print("Ops, algum erro aconteceu.")
        pass

main()
