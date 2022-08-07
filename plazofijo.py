class PlazoFijo():
    def __init__(self, num_pf, titular, plazo, importe_inicial, fecha_inicio, importe_retiro, fecha_vencimiento):
        self.num_pf = num_pf
        self.titular = titular
        self.plazo = plazo
        self.importe_inicial = importe_inicial
        self.fecha_inicio = fecha_inicio
        self.importe_retiro = importe_retiro
        self.fecha_vencimiento = fecha_vencimiento

    def __str__(self):
        return("Plazo fijo n° " + str(self.num_pf) + "\n\tTitular: " + str(self.titular) + "\n\tPlazo: " + str(self.plazo) + " dias\n\tImporte inicial: $ " + str(self.importe_inicial) + "\n\tFecha de alta: " + str(self.fecha_inicio) + "\n\tImporte a retirar: $ " + str(self.importe_retiro) + "\n\tFecha vencimiento: " + str(self.fecha_vencimiento))
    