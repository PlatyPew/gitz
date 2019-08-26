class Helper:
    def __init__(self, command, **kwds):
        self.command = command
        for f in FIELDS:
            value = kwds.get(f.upper(), '').lstrip().rstrip()
            if f != 'danger':
                value = self._indent(value)
            setattr(self, f, value)
        if self.danger:
            self.danger = 'DANGER: %s\n\n' % self.danger

    def print_help(self, argv):
        if not ('-h' in argv or '--h' in argv):
            return False
        if self.summary and self.examples:
            print(HELP.format(**vars(self)).rstrip())
        else:
            print(self.usage.rstrip())
            print(self.help.rstrip())
        return True

    INDENT = '    '

    def _indent(self, text):
        return '\n'.join(self.INDENT + i for i in text.splitlines()) + '\n'


FIELDS = 'danger', 'examples', 'help', 'summary', 'usage'

HELP = """\
{command}:
{summary}
USAGE:
{usage}
{danger}DESCRIPTION:
{help}
EXAMPLES:
{examples}
"""
