# Gmail_reader

Gmail_reader is a Python script to read email from Gmail account.

## Settings
In order to login to your gmail account you need to set some values.
You have to create an 'app password', please follow this instructions: [Google Help App Password](https://support.google.com/accounts/answer/185833?hl=en)
```python
FROM_EMAIL  = [YOUR EMAIL]
FROM_PWD    = [YOUR APP PASSWORD]
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT   = 993
```


## Usage

```python
import gmail_reader

# returns only last email without body
read_email()

# returns last 5 email without body
read_email(5)

# returns last 5 emails with body
read_email(5,True)
```


## License
[MIT](https://choosealicense.com/licenses/mit/)