
"""
Fix TSV files with newlines in some of the fields.

Depends on lines having the same number of fields as the first line.
"""

from argparse import ArgumentParser


def fix_newlines(filename, separator):
    """Fix the newlines in the given file."""
    with open(filename, encoding="ISO-8859-1") as csvfile:
        # go through the csvfile finding lines with odd numbers of quotation
        # marks. When we hit one, collect up the field contents until we find another
        # one
        in_multiline = False
        multilines = []
        first_line = next(csvfile)
        num_separators = first_line.count(separator)
        print(first_line, end='')  # the first line is right by definition

        for line in csvfile:

            if in_multiline:
                multilines.append(line.rstrip('\n'))  # take off the newline here
                seps_so_far += line.count(separator)
                if seps_so_far < num_separators:
                    # this is not the last line, just keep going
                    pass
                elif seps_so_far == num_separators:
                    # this is the last line of the section, emit everything
                    print(" ".join(multilines))
                    in_multiline = False
                else:   # seps_so_far > num_separators
                    raise ValueError("Found inconsistent lines", multilines)

            else:  # not in a multi-line section

                if line.count(separator) == num_separators:
                    # line is okay, just emit it
                    print(line, end='')  # line already has a newline at the end
                else:
                    # line doesn't have enough fields, starts a multi-line section
                    in_multiline=True
                    multilines = [line.rstrip('\n')]  # take off the newline
                    seps_so_far = line.count(separator)

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("input_filename")

    args = parser.parse_args()
    fix_newlines(args.input_filename, '\t')
