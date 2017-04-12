import argparse


def write_latex_file(filename_out, conf_name, subtitle, logo_path, date, filename_members):
    with open(filename_out, "w") as latex_file:
        latex_file.write("\\documentclass[a4paper,10pt]{letter}\n\n")
        latex_file.write("%% Character encoding\n\\usepackage[utf8]{inputenc}\n")
        latex_file.write("% load ticket.sty with the appropriate ticket definition\n")
        latex_file.write("\\usepackage[tdf-theme,crossmark]{ticket}\n\n")
        latex_file.write("% load misc stuff\n")
        latex_file.write("\\usepackage{graphicx}\n\n")
        latex_file.write("% make default ticket\n")
        latex_file.write("\\renewcommand{\\ticketdefault}{%\n")
        latex_file.write("  \\put(50,  3){\\includegraphics[width=15mm]{" + logo_path + "}}\n")
        latex_file.write("  \\put( 5, 13){\\line(1,0){60}}\n")
        latex_file.write("  \\put( 7, 10){\\scriptsize " + conf_name + "}\n")
        latex_file.write("  \\put( 7,  7){\\scriptsize " + subtitle + "}\n")
        latex_file.write("  \\put( 7,  4){\\scriptsize " + date + "}\n")
        latex_file.write("}\n\n")

        latex_file.write("% now what do you like to put in your ticket\n")
        latex_file.write("\\newcommand{\confpin}[2]{\\ticket{%\n")
        latex_file.write("\\put(3,35){\\fbox{\\parbox[b][4em][t]{0.50\\linewidth}{\\vfill\\centering\\bfseries\\Large #1}}}\n")
        latex_file.write("\\put(3,16){\\fbox{\\parbox[b][4em][t]{0.50\\linewidth}{\\centering\\bfseries\large #2}}}\n")
        latex_file.write("}}\n\n")


        latex_file.write("\\begin{document}\n")
        latex_file.write("\\sffamily\n")
        # add members
        with open(filename_members, "r") as csv_members:
            for line in csv_members.readlines():
                firstname, lastname, organization = line.rstrip().replace("&", "\&").split(';')
                latex_file.write("\\confpin{" + firstname + " " + lastname + "}{" + organization +"}\n")

        latex_file.write("\\end{document}\n")

def main():
    parser = argparse.ArgumentParser(
        description='Generate a latex file to generate tickets')
    parser.add_argument('logo', metavar='logo', type=str,
                        help='Logo to use')
    parser.add_argument('conf_name', metavar='conf_name', type=str,
                        help='Conference name', default=None)
    parser.add_argument('subtitle', metavar='subtitle', type=str,
                        help='Conference subtitle', default=None)
    parser.add_argument('csv_participant', metavar='csv_participant', type=str,
                        help='CSV of participants. Format: <Name>;<Lastname>;<institution>', default=None)
    parser.add_argument('date', metavar='date', type=str,
                        help='Conference date', default=None)
    parser.add_argument('f_out', metavar='filename_out', type=str,
                        help='Conference name', default=None)

    # parse arguments
    args = parser.parse_args()
    write_latex_file(args.f_out, args.conf_name, args.subtitle, args.logo, args.date, args.csv_participant)


if __name__ == "__main__":
    main()
