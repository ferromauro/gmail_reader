# Gmail_reader

Gmail_reader is a Python script to read email from Gmail account.

## Settings
In order to login to your gmail account you need to set some values in the __init__().

```python
def __init__(self):    
    self.gmail      = [YOUR EMAIL]
    self.password   = [YOUR APP PASSWORD]
    self.server     = "imap.gmail.com"
    self.port       = 993
```
**Note:** You have to create an 'app password', please follow this instructions: [Google Help App Password](https://support.google.com/accounts/answer/185833?hl=en)

## Usage

```python
from gmail_reader import Gmail_reader

# Create a reader instance
G = Gmail_reader()
# returns only last email without body
G.read_()

# returns last 5 email without body
G.read(5)

# returns last 5 emails with body
G.read(5,True)
```


## License
[MIT](https://choosealicense.com/licenses/mit/)