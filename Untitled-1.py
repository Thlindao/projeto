email_sender/
 send_emails.py
 recipients.csv
 README.md

import smtplib
import ssl
import csv
from email.message import EmailMessage

# --- CONFIGURAÇÕES ---
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465  # Porta para SSL
SENDER_EMAIL = "seu_email@gmail.com"
SENDER_PASSWORD = "sua_senha_de_app"  # Use senha de app, não a senha normal!

ASSUNTO = "Olá! 🚀 Este é um e-mail automático"
MENSAGEM_BASE = """\
Olá {nome},

Esta é uma mensagem automática enviada pelo script Python!

Tenha um ótimo dia 😊
"""

ANEXO = None  # Exemplo: "documento.pdf" (ou deixe None se não quiser anexos)
CSV_ARQUIVO = "recipients.csv"  # arquivo com colunas: nome,email


# --- FUNÇÃO PRINCIPAL ---
def enviar_emails():
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, context=context) as server:
        server.login(SENDER_EMAIL, SENDER_PASSWORD)

        with open(CSV_ARQUIVO, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                nome = row["nome"]
                email = row["email"]

                msg = EmailMessage()
                msg["From"] = SENDER_EMAIL
                msg["To"] = email
                msg["Subject"] = ASSUNTO
                msg.set_content(MENSAGEM_BASE.format(nome=nome))

                if ANEXO:
                    with open(ANEXO, "rb") as f:
                        msg.add_attachment(
                            f.read(),
                            maintype="application",
                            subtype="octet-stream",
                            filename=ANEXO,
                        )

                server.send_message(msg)
                print(f"✅ E-mail enviado para {nome} <{email}>")

    print("\nTodos os e-mails foram enviados com sucesso!")


if __name__ == "__main__":
    enviar_emails()
