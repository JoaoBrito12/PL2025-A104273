import json
import re 

class VendingMachine:
    def __init__(self, json_file):
        self.json_file = json_file
        self.stock = self.load_stock()
        self.saldo = 0.0
        self.moedas = {
            "2E": 2.0, "1E": 1.0, "50C": 0.5, "20C": 0.2,
            "10C": 0.1, "5C": 0.05, "2C": 0.02, "1C": 0.01
        }

    def load_stock(self):
        try:
            with open(self.json_file, "r", encoding="utf-8") as file:
                data = json.load(file)
                return {item["cod"]: item for item in data["stock"]}
        except (FileNotFoundError, json.JSONDecodeError):
            print("Erro ao carregar o stock. Verifique o arquivo JSON.")
            return {}

    def save_stock(self):
        stock_list = list(self.stock.values())  
        with open(self.json_file, "w", encoding="utf-8") as file:
            json.dump({"stock": stock_list}, file, indent=4, ensure_ascii=False)

    def listar(self):
        print("\ncod | nome | quantidade | preço")
        print("---------------------------------")
        for cod, info in self.stock.items():
            print(f"{cod} | {info['nome']} | {info['quant']} | {info['preco']:.2f}€")
        print()

    def inserir_moeda(self, moedas):
        """Inserir moedas validando com regex"""
        moedas_validas = []
        for moeda in moedas:
            moeda = moeda.upper().strip()
            if re.fullmatch(r"[21]E|50C|20C|10C|5C|2C|1C", moeda): 
                moedas_validas.append(moeda)
            else:
                print(f"Moeda inválida ignorada: {moeda}")
        
        for moeda in moedas_validas:
            self.saldo += self.moedas[moeda]

        print(f"Saldo = {self.saldo:.2f}€")

    def selecionar(self, cod):
        """Selecionar produto validando o código com regex"""
        cod = cod.upper().strip()
        if not re.fullmatch(r"[A-Z]\d{2}", cod): 
            print("Erro: Código do produto inválido.")
            return
        
        if cod in self.stock:
            produto = self.stock[cod]
            if self.saldo >= produto["preco"]:
                if produto["quant"] > 0:
                    produto["quant"] -= 1
                    self.saldo -= produto["preco"]
                    print(f"Pode retirar o produto dispensado: \"{produto['nome']}\"")
                    self.save_stock()
                else:
                    print("Produto esgotado")
            else:
                print(f"Saldo insuficiente. Saldo = {self.saldo:.2f}€, Pedido = {produto['preco']:.2f}€")
        else:
            print("Produto não encontrado")

    def sair(self):
        troco = self.calcular_troco()
        if troco:
            print(f"Pode retirar o troco: {troco}")
        print("Até à próxima!")
    
    def calcular_troco(self):
        troco = []
        saldo_cents = int(self.saldo * 100)
        for moeda, valor in sorted(self.moedas.items(), key=lambda x: -x[1]):
            valor_cents = int(valor * 100)
            while saldo_cents >= valor_cents:
                troco.append(moeda)
                saldo_cents -= valor_cents
        self.saldo = 0  
        return ", ".join(troco) if troco else "Sem troco."



if __name__ == "__main__":
    vm = VendingMachine("stock.json")
    print("2024-03-12, Stock carregado, Estado atualizado.")
    print("Bom dia! Estou disponível para atender o seu pedido.")
    
    while True:
        comando = input(">> ").strip().upper()
        
        if comando == "LISTAR":
            vm.listar()
        elif comando.startswith("MOEDA"):
            moedas = comando[6:].replace(" ", "").split(',')
            vm.inserir_moeda(moedas)
        elif comando.startswith("SELECIONAR"):
            args = comando.split()
            if len(args) > 1:
                vm.selecionar(args[1])
            else:
                print("Erro: Código do produto não especificado.")
        elif comando == "SAIR":
            vm.sair()
            break
        else:
            print("Comando não reconhecido.")

