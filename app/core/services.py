

class CalculoImposto:

    def calculo_imposto_faturado(self, ProdutoEntity, NotaFiscalEntity):
        valor = ProdutoEntity.valor
        qnt = NotaFiscalEntity.qnt
        imposto = (((valor*qnt)*0.15)*2.34/100)
        return imposto
