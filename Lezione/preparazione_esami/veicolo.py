class Veicolo:
    def __init__(self, marca: str, modello: str, anno: int) -> None:
        self.marca = marca
        self.modello = modello
        self.anno = anno

    def descrivi_veicolo(self):
        print(f'Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}')
    

class Auto(Veicolo):
    def __init__(self, marca: str, modello: str, anno: int, numero_porte) -> None:
        super().__init__(marca, modello, anno)
        self.numero_porte = numero_porte

    def descrivi_veicolo(self):
        print(f'Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}, Numero di porte: {self.numero_porte}')


class Moto(Veicolo):
    def __init__(self, marca: str, modello: str, anno: int, tipo:str) -> None:
        super().__init__(marca, modello, anno)
        self.tipo: str = tipo

    def descrivi_veicolo(self):
        print(f'Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}, Tipo: {self.tipo}')
        

veicolo = Veicolo("Generic", "Model", 2020)  # Crea un'istanza della classe Veicolo
auto = Auto("Toyota", "Corolla", 2021, 4)  # Crea un'istanza della classe Auto
moto = Moto("Yamaha", "R1", 2022, "sportiva")  # Crea un'istanza della classe Moto

veicolo.descrivi_veicolo()  # Test del metodo descrivi_veicolo per Veicolo
auto.descrivi_veicolo()
moto.descrivi_veicolo()  # Test del metodo descrivi_veicolo per Moto



"""
Marca: Generic, Modello: Model, Anno: 2020
Marca: Generic, Modello: Model, Anno: 2020

Marca: Toyota, Modello: Corolla, Anno: 2021, Numero di porte: 4
Marca: Toyota, Modello: Corolla, Anno: 2021, Numero di porte: 4

Marca: Yamaha, Modello: R1, Anno: 2022, Tipo: sportiva
Marca: Yamaha, Modello: R1, Anno: 2022, Tpo: sportiva
"""