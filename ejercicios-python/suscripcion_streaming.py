class SuscripcionStreaming:
    costos_suscripcion = {"Gratis": 0, "Estándar": 5.99, "Premium": 10.99}

    def __init__(self, usuario, tipo_suscripcion, pago_realizado):
        self.usuario = usuario
        self.tipo_suscripcion = tipo_suscripcion
        self.pago_realizado = pago_realizado

    def realizar_pago(self, monto):
        costo = self.costos_suscripcion[self.tipo_suscripcion]

        if monto < costo:
            print("Saldo insuficiente")
        elif monto > costo:
            self.pago_realizado = True
            print(f"Pago realizado, tienes ${monto - costo} de vuelto")
        else:
            self.pago_realizado = True
            print("Pago realizado, no tienes vuelto")

    def cambiar_suscripcion(self, nuevo_tipo):
        tipos = ["Gratis", "Estándar", "Premium"]

        if nuevo_tipo not in tipos:
            print("Suscripcion no disponible")
        else:
            self.tipo_suscripcion = nuevo_tipo
            print(f"Tu nueva suscripción es {nuevo_tipo}")

    def ver_contenido_exclusivo(self):
        if self.tipo_suscripcion == "Premium" and self.pago_realizado == True: 
            print("Hola, este contenido es exclusivo")
        else:
            print("No tienes acceso al contenido, mejora tu tipo de suscripción o paga tu saldo pendiente")

    def mostrar_info_suscripcion(self):
        print(
            f"Hola, {self.usuario}, "
            f"tu tipo de suscripción es: {self.tipo_suscripcion}"
        )


#definir los 3 usuarios
usuario1 = SuscripcionStreaming("matias", "Estándar", False)
usuario2 = SuscripcionStreaming("ithan", "Gratis", False)
usuario3 = SuscripcionStreaming("Rodrigo", "Premium", False)


#usuario 1 intenta ver contenido exclusivo
usuario1.ver_contenido_exclusivo()

#usuario 1 mejora su suscripcion a premium
usuario1.cambiar_suscripcion("Premium")

#usuario 1 paga su saldo pendiente
usuario1.realizar_pago(10.99)


#usuario 2 intenta ver contenido exclusivo
usuario2.ver_contenido_exclusivo()

#usuario 2 mejora su suscripcion a premium
usuario2.cambiar_suscripcion("Premium")

#usuario 2 paga 2 veces
usuario2.realizar_pago(10.99)
usuario2.realizar_pago(10.99)


#usuario 3 intenta pagar menos que su saldo y ver contenido exclusivo
usuario3.realizar_pago(3)
usuario3.ver_contenido_exclusivo()

