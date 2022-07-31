from .entitys import ProdutoEntity, CategoriaEntity, NotafiscalEntity

class CalculoImposto:

    def calculo_imposto_faturado(self, produto_entity, nota_fiscal_entity):
        valor = produto_entity.valor
        qnt = nota_fiscal_entity.qnt
        imposto = (((valor*qnt)*0.15)*2.34/100)
        return imposto


class MontaCalculoImposto:
    def carrega_dados(self,data):
        nota = NotafiscalEntity(
            id=None,
            numero = data.get('numero'),
            qnt=data.get('qnt'), 
            produto=data.get('produto'))
        print(nota)