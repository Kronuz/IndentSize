import sublime
import sublime_plugin


class IndentSizeCommand(sublime_plugin.TextCommand):
    def indent(self, edit, line, start):
        start_point = start.begin()

        tab_size = self.view.settings().get("tab_size")
        indent_size = self.view.settings().get("indent_size", tab_size)
        if indent_size > tab_size:
            indent_size = tab_size

        indentation_region = sublime.Region(line.begin(), start_point)
        indentation = self.view.substr(indentation_region)

        # Figure out the true length of the line (in spaces)
        indentation_length = indentation.replace(" " * tab_size, "\t")
        indentation_length = indentation_length.replace(" \t", "\t").replace("\t", " " * tab_size)
        indentation_length = len(indentation_length)

        # How many trailing spaces are there in the line:
        trailing_spaces = len(indentation) - len(indentation.rstrip(" "))

        # How many characters are there from the last indent stop:
        indent_mod = indentation_length % indent_size

        # How many spaces are there from the last tab stop:
        trailing_tab = min(indentation_length % tab_size, trailing_spaces)

        if trailing_tab >= indent_size:
            trailing = trailing_tab
            tab = "\t"
        else:
            trailing = 0
            tab = " " * (indent_size - indent_mod)

        if trailing:
            indentation_region = sublime.Region(start_point - trailing, start_point)
            self.view.erase(edit, indentation_region)
        self.view.insert(edit, start_point - trailing, tab)

    def run(self, edit):
        for region in reversed(self.view.sel()):
            if region.empty():
                line = self.view.line(region)
                self.indent(edit, line, region)
            else:
                for line in reversed(self.view.lines(region)):
                    if line.a != line.b:
                        start = self.view.find("[^ \t]", line.begin())
                        if start is None:
                            start = line
                        self.indent(edit, line, start)


class UnindentSizeCommand(sublime_plugin.TextCommand):
    def unindent(self, edit, line, start):
        start_point = start.begin()

        tab_size = self.view.settings().get("tab_size")
        indent_size = self.view.settings().get("indent_size", tab_size)
        if indent_size > tab_size:
            indent_size = tab_size

        indentation_region = sublime.Region(line.begin(), start_point)
        indentation = self.view.substr(indentation_region)

        trailing = 0

        indent_mod = True
        while len(indentation) and indent_mod:
            trailing += 1
            indentation = indentation[:-1]
            indentation_length = indentation.replace(" " * tab_size, "\t")
            indentation_length = indentation_length.replace(" \t", "\t").replace("\t", " " * tab_size)
            indentation_length = len(indentation_length)
            indent_mod = indentation_length % indent_size

        if trailing:
            indentation_region = sublime.Region(start_point - trailing, start_point)
            self.view.erase(edit, indentation_region)

    def run(self, edit):
        for region in reversed(self.view.sel()):
            for line in reversed(self.view.lines(region)):
                if line.a != line.b:
                    start = self.view.find("[^ \t]", line.begin())
                    if start is None:
                        start = line
                    self.unindent(edit, line, start)


class BackspaceSizeCommand(UnindentSizeCommand):
    def run(self, edit):
        for region in reversed(self.view.sel()):
            if region.empty():
                for line in reversed(self.view.lines(region)):
                    if line.a != line.b:
                        start = self.view.find("[^ \t]", line.begin())
                        if start is None:
                            start = line
                        if region.begin() > start.begin() or start.begin() == line.begin():
                            self.view.erase(edit, sublime.Region(region.begin() - 1, region.end()))
                        else:
                            self.unindent(edit, line, region)
                    else:
                        self.view.erase(edit, sublime.Region(region.begin() - 1, region.end()))
            else:
                self.view.erase(edit, sublime.Region(region.begin(), region.end()))
