import sublime
import sublime_plugin


class IndentSizeCommand(sublime_plugin.TextCommand):
    def indent(self, edit, region, start_point):
        translate_tabs_to_spaces = self.view.settings().get("translate_tabs_to_spaces")
        tab_size = self.view.settings().get("tab_size")
        indent_size = self.view.settings().get("indent_size", tab_size)
        if indent_size > tab_size:
            indent_size = tab_size

        if translate_tabs_to_spaces or indent_size < tab_size:
            # insert spaces upto the next "indent stop" (like tab stop)
            row, char_column = self.view.rowcol(start_point)
            real_column = 0
            for i in range(start_point - char_column, start_point):
                if self.view.substr(i) == "\t":
                    real_column += tab_size
                else:
                    real_column += 1
            space_count = indent_size - (real_column % indent_size)
            tab = " " * space_count
        else:
            tab = "\t"
        self.view.insert(edit, start_point, tab)

        if not translate_tabs_to_spaces:
            start_point += len(tab)
            line = self.view.line(start_point)
            indentation_region = sublime.Region(line.begin(), start_point)
            indentation = self.view.substr(indentation_region)
            indentation = indentation.replace("\t", " " * tab_size)
            indentation = indentation.replace(" " * tab_size, "\t")
            self.view.replace(edit, indentation_region, indentation)

    def run(self, edit):
        for region in reversed(self.view.sel()):
            for line in reversed(self.view.lines(region)):
                if line.a != line.b:
                    start = self.view.find("[^ \t]", line.begin())
                    if start is None:
                        start = line
                    self.indent(edit, region, start.begin())


class UnindentSizeCommand(sublime_plugin.TextCommand):
    def unindent(self, edit, region, start_point):
        translate_tabs_to_spaces = self.view.settings().get("translate_tabs_to_spaces")
        tab_size = self.view.settings().get("tab_size")
        indent_size = self.view.settings().get("indent_size", tab_size)
        if indent_size > tab_size:
            indent_size = tab_size

        line = self.view.line(start_point)
        indentation_region = sublime.Region(line.begin(), start_point)
        indentation = self.view.substr(indentation_region)
        indentation = indentation.replace("\t", " " * tab_size)
        indentation = indentation[:-indent_size]
        if not translate_tabs_to_spaces:
            indentation = indentation.replace(" " * tab_size, "\t")
        self.view.replace(edit, indentation_region, indentation)

    def run(self, edit):
        for region in reversed(self.view.sel()):
            for line in reversed(self.view.lines(region)):
                if line.a != line.b:
                    start = self.view.find("[^ \t]", line.begin())
                    if start is None:
                        start = line
                    self.unindent(edit, region, start.begin())


class BackspaceSizeCommand(UnindentSizeCommand):
    def run(self, edit):
        for region in reversed(self.view.sel()):
            if region.empty():
                for line in reversed(self.view.lines(region)):
                    if line.a != line.b:
                        start = self.view.find("[^ \t]", line.begin())
                        if start is None:
                            start = line
                        if region.begin() > start.begin():
                            self.view.erase(edit, sublime.Region(region.begin() - 1, region.end()))
                        else:
                            self.unindent(edit, region, region.begin())
                    else:
                        self.view.erase(edit, sublime.Region(region.begin() - 1, region.end()))
            else:
                self.view.erase(edit, sublime.Region(region.begin(), region.end()))
