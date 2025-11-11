#!/usr/bin/env python3
import socketserver
import email.parser

class SMTPHandler(socketserver.StreamRequestHandler):
    def handle(self):
        print(f'\n📧 Nuova connessione da {self.client_address}')
        self.wfile.write(b'220 localhost SMTP\r\n')
        
        while True:
            line = self.rfile.readline()
            if not line:
                break
            
            line = line.decode('utf-8').strip()
            print(f'< {line}')
            
            if line.upper().startswith('HELO') or line.upper().startswith('EHLO'):
                self.wfile.write(b'250 localhost\r\n')
            elif line.upper().startswith('MAIL FROM:'):
                self.mail_from = line[10:].strip()
                self.wfile.write(b'250 OK\r\n')
            elif line.upper().startswith('RCPT TO:'):
                self.rcpt_to = line[8:].strip()
                self.wfile.write(b'250 OK\r\n')
            elif line.upper() == 'DATA':
                self.wfile.write(b'354 Start mail input\r\n')
                data = []
                while True:
                    data_line = self.rfile.readline()
                    if data_line == b'.\r\n':
                        break
                    data.append(data_line)
                
                print('\n' + '='*60)
                print('📧 EMAIL RICEVUTA')
                print('='*60)
                print(f'Da: {self.mail_from}')
                print(f'A: {self.rcpt_to}')
                print(f'\nMessaggio:')
                print(b''.join(data).decode('utf-8'))
                print('='*60 + '\n')
                
                self.wfile.write(b'250 OK\r\n')
            elif line.upper() == 'QUIT':
                self.wfile.write(b'221 Bye\r\n')
                break
            else:
                self.wfile.write(b'250 OK\r\n')

print('🚀 Server SMTP avviato su localhost:1025 (Python 3.12+)')
print('Premi Ctrl+C per fermare il server\n')

with socketserver.TCPServer(('localhost', 1025), SMTPHandler) as server:
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\n\n👋 Server fermato')
        sys.exit(0)
