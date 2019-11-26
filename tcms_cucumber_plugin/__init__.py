from tcms_api.plugin_helpers import Backend
from gherkin.parser import Parser
from gherkin.token_scanner import TokenScanner

class Plugin:  # pylint: disable=too-few-public-methods
    def __init__(self):
        self.backend = Backend(prefix='[cucumber] ')

    def parse(self, cucumber_file):
        # self.backend.configure()
        parser = Parser()
        gherkin_file = parser.parse(TokenScanner(cucumber_file))
        data = parser.parse(gherkin_file)

def main(argv):
    if len(argv) < 2:
        raise Exception("USAGE: {filename} results.xml".format(filename=argv[0]))

    plugin = Plugin()
    plugin.parse(argv[1])