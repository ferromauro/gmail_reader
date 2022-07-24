import imaplib
import email

class Gmail_reader():

    def __init__(self):    
        self.gmail      = "[YOUR EMAIL]
        self.password   = "[YOUR APP PASSWORD]
        self.server     = "imap.gmail.com"
        self.port       = 993

    def read(self, number=1,  contain_body=False):
        try: 
            mail = imaplib.IMAP4_SSL(self.server)
            mail.login(self.gmail, self.password)
            mail.select('inbox')

            data = mail.search(None, 'ALL')
            mail_ids = data[1]
            id_list = mail_ids[0].split()   
            latest_email_id = int(id_list[-1])

            for i in range(latest_email_id,latest_email_id-number, -1):
                data = mail.fetch(str(i), '(RFC822)' )

                for response_part in data:
                    arr = response_part[0]
                    if isinstance(arr, tuple):
                        msg = email.message_from_string(str(arr[1],'utf-8'))
                        # Subject
                        subject = msg['subject']

                        # Sender
                        sender = msg['from']

                        # Store Body
                        body = ""
                        temp = msg
                        if temp.is_multipart():
                            for part in temp.walk():
                                ctype = part.get_content_type()
                                cdispo = str(part.get('Content-Disposition'))

                                # skip text/plain type
                                if ctype == 'text/plain' and 'attachment' not in cdispo:
                                    body = part.get_payload(decode=True)  # decode
                                    break
                                else:
                                    body = temp.get_payload(decode=True)

                        # Print Sender, Subject, Body
                        print("-"*75)  # To divide the messages
                        print(f"From    : {sender}")
                        print(f"Subject : {subject}")
                        if(contain_body):
                            print(f"Body    : {body.decode()}")
    

        except Exception as e:
            print(e)

        finally:
            mail.close()
            mail.logout()

# Let's test it!!! 
if __name__ == "__main__": 
    reader = Gmail_reader()      
    reader.read(5, True)