
"""
Fix CSV files with newlines in some of the fields.

Depends on every field being quoted and using double quotation marks for literal
quotation marks in a field.
"""

from argparse import ArgumentParser


def fix_newlines(filename):
    """Fix the newlines in the given file."""
    with open(filename, encoding="ISO-8859-1") as csvfile:
        # go through the csvfile finding lines with odd numbers of quotation
        # marks. When we hit one, collect up the field contents until we find another
        # one
        in_multiline = False
        multilines = []
        for line in csvfile:
            balanced = (line.count('"') % 2 == 0)
            if in_multiline:
                multilines.append(line.rstrip())  # take off the newline here
                if balanced:
                    # this is not the last line, just keep going
                    pass
                else:
                    # this is the last line of the section, emit everything
                    print(" ".join(l.rstrip() for l in multilines))
                    multilines = []; in_multiline = False

            else:  # not in a multi-line section
                if line.count('"') % 2 == 0:
                    # line has balanced quotes, just emit it
                    print(line, end='')  # line already has a newline at the end
                else:
                    # line has unbalanced quotes so it starts a
                    # multi-line section
                    multilines.append(line.rstrip())
                    in_multiline=True

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("input_filename")

    args = parser.parse_args()
    fix_newlines(args.input_filename)
