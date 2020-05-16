from telegram.ext import Updater, CommandHandler


def main():
    # Instanciamos el updater
    updater = Updater(token='1267844349:AAHX1Hssg_mhKdM7j2pCwMmT_VHDBB4hA0Y', use_context=True)

    # Añadiendo un manejador al comando  /start
    updater.dispatcher.add_handler(CommandHandler("start", start))

    # Añadiendo un manejador al comando  /repite
    updater.dispatcher.add_handler(CommandHandler("repite", repite))

    # Añadiendo un manejador al comando  /suma
    updater.dispatcher.add_handler(CommandHandler("suma", suma))

    # Empezamos a pedir notificaciones a telegram
    updater.start_polling()

    # Capturamos señales de parada
    updater.idle()

def start(update, context):
    update.message.reply_text("Hola soy un bot y he sido creado por José María Bernal")

def repite(update, context):
    update.message.reply_text(update.message.text)

def suma(update, context):
    resultado = int(context.args[0]) + int(context.args[1])
    resultado = str(resultado)
    update.message.reply_text("El resultado de la suma de es " + resultado)

main()