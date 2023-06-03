# pyscriptnative

```py
import pyscriptnative

app = pyscriptnative.Router()

def html():
    return """
    <!-- HTML here -->
    """

def css():
    return """
    /* CSS here */
    """

def script():
    return """
    # Python here
    """

app.html(html())
app.css(css())
app.script(script())

app.run('localhost', 8080, debug=True)
```