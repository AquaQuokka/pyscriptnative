from flask import Flask, render_template_string

__version__ = "0.3.2"

def template_html(body):
    template = '''
    <!DOCTYPE html>
    <html>

        <head>

            <link rel="stylesheet" href="https://pyscript.net/latest/pyscript.css" />

            <script defer src="https://pyscript.net/latest/pyscript.js"></script>

            {% block py %}

                <py-script>

                    {{ py }}

                </py-script>

            {% endblock %}

            {% block requirements %}

                <py-config>

                    packages = {{ requirements }}
                
                </py-config>

            {% endblock %}

            {% block css %}

                <style>

                    {{ css }}
                
                </style>
            
            {% endblock %}
            
        </head>
        
        <body>

            {% block body %}

                ''' + body + '''

            {% endblock %}

            {% block js %}

                <script type="text/javascript">

                    {{ js }}
                
                </script>
            
            {% endblock %}
                
        </body>

    </html>
    '''

    return template

class Router:
    def __init__(self):
        self.htmlctx = ""
        self.cssctx = ""
        self.jsctx = ""
        self.pyctx = ""
        self.requirements = []

    def html(self, func):
        self.htmlctx = func

    def css(self, func):
        self.cssctx = func

    def js(self, func):
        self.jsctx = func
    
    def py(self, func):
        self.pyctx = func
    
    def require(self, pkg: str):
        self.requirements.append(pkg)
    
    def requires(self, pkgs: list):
        self.requirements = pkgs

    def run(self, host='localhost', port=8080, debug=False):
        app = Flask(__name__)

        @app.route('/')
        def index():
            return render_template_string(template_html(body=self.htmlctx), host=host, port=port, debug=debug, css=self.cssctx, js=self.jsctx, py=self.pyctx, requirements=self.requirements)

        app.run(host=host, port=port, debug=debug)
