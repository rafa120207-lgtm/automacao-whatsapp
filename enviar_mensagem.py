import pywhatkit as kit
import time

# ============================================
# BOT DE ENVIO AUTOMÁTICO DE MENSAGENS
# Desenvolvido por: Rafael Gonçalves
# Descrição: Envia mensagem automática via WhatsApp
# ============================================

def enviar_mensagem_whatsapp(numero, mensagem, hora, minuto):
    """
    Envia uma mensagem automática pelo WhatsApp.
    
    numero: número com código do país (ex: +5511999999999)
    mensagem: texto a ser enviado
    hora: hora do envio (formato 24h)
    minuto: minuto do envio
    """
    try:
        print(f"Agendando mensagem para {numero} às {hora}:{minuto:02d}...")
        kit.sendwhatmsg(numero, mensagem, hora, minuto, wait_time=20)
        print("Mensagem enviada com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar mensagem: {e}")


# ============================================
# EXEMPLO DE USO
# ============================================

numero_destino = "+5511965736438"  # Troca pelo número real
mensagem = "Olá! Essa é uma mensagem automática enviada via Python. 🤖"

# Pega o horário atual e agenda para 2 minutos à frente
from datetime import datetime, timedelta
agora = datetime.now() + timedelta(minutes=2)

enviar_mensagem_whatsapp(
    numero=numero_destino,
    mensagem=mensagem,
    hora=agora.hour,
    minuto=agora.minute
)