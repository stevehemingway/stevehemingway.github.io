from sender import Mail, Message

sender_email = 'steve@acksam.com'

mail = Mail("mail.gandi.net", port=587, username="steve@acksam.com", password="yesterday consensus",
            use_tls=True, use_ssl=False, debug_level=None)

mail.fromaddr = ("Steve H", sender_email)

msg = Message("demo subject", fromaddr=sender_email,
              to="steve.hemingway@gmail.com")

msg.body = "this is the body"

mail.send(msg)

print("message sent!")
      
