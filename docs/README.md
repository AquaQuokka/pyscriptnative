# pyscriptnative

pyscriptnative is a Python package that allows you to use the power of [PyScript](https://pyscript.net) to use Python in HTML, natively with Flask.

## Examples

Here is a simple outline of how to use `pyscriptnative`:

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


### What if I need external modules?

You can use the `pyscriptnative.Router().require()` and/or `pyscriptnative.Router().requires()` methods to use some external modules. However, due to pyscriptnative being a wrapper around [PyScript](https://pyscript.net), it doesn't support all modules as [PyScript](https://pyscript.net) is built on [Pyodide](https://pyodide.org/en/stable/), which does not support things like sockets, etc.

#### What is the difference between `require()` and `requires()`?

The difference between `require()` and `requires()` is that `require()` adds to the requirements, while `requires()` overrides the requirements.