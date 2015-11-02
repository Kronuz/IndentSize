# Indentation Size Setting

Sublime Text 3 Plugin To Add Indentation Size Setting


## Synopsis

This plugin gives Sublime Text the ability to have different settings for tab
width, indent size, indent type (spaces vs. tabs), so it correctly displays and
properly indent old code, as requested in
https://www.sublimetext.com/forum/viewtopic.php?f=4&t=15922.

Some codebases have indentation requirements that are unusual by today's
standards, meaning they require Tab characters to be 8 spaces wide, but
indentations to be 4 spaces.

This creates a problem with Sublime Text because while we can set the "tab_size"
parameter to 8, it then causes all tab key presses to use 8 spaces as well. This
is my attempt at resolving this issue. I decided to put this out there because
from reading the forums and the userecho site for Sublime Text, there are at
least a few other people out there in my shoes.

This plugin was inspired by Vimdentation (https://github.com/Wintaru/Vimdentation)
but it has been tweaked and improved so it's more cleanly and transparently
integrated with Sublime Text.


## Installation

**With the Package Control plugin:** The easiest way to install IndentSize
is through Package Control, which can be found at this site:
http://wbond.net/sublime_packages/package_control

Once you install Package Control, restart Sublime Text and bring up the
*Command Palette* (Command+Shift+P on OS X, Control+Shift+P on Linux/Windows).
Select "Package Control: Install Package", wait while Package Control fetches
the latest package list, then select IndentSize when the list appears. The
advantage of using this method is that Package Control will automatically keep
IndentSize up to date with the latest version.

**Without Git:** Download the latest source from
[GitHub](https://github.com/Kronuz/IndentSize) and copy the whole directory into
the Packages directory.

**With Git:** Clone the repository in your Sublime Text Packages directory,
located somewhere in user's "Home" directory (Preferences -> Browse Packages...):

```
git clone git://github.com/Kronuz/IndentSize.git
```


## Configuration

One configuration option is available: `indent_size`; which defaults to
`tab_size`, effectively disabling the plugin.

In my case, I have the following in my Syntax Specific settings for C/C++:

```
{
    "tab_size": 8,
    "indent_size": 4,
    "translate_tabs_to_spaces": false,
    "detect_indentation": false
}
```


## License

```
Copyright (c) 2015 by German M. Bravo (Kronuz)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
