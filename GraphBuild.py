from string import Template

import sublime
import sublime_plugin
import subprocess

class BuildCommand(sublime_plugin.TextCommand):
    def run(self, edit):

        selection = sublime.Region(0, self.view.size())

        data = self.view.substr(selection).replace(' ', '').replace('\n', '')

        fd = open('template.html')
        template = Template(fd.read())
        fd.close()

        fd = open('/tmp/index.html', 'w')
        fd.write( template.substitute(data=data) )
        fd.close()

        subprocess.Popen('firefox /tmp/index.html', shell=True)
