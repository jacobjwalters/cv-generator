import yaml
import sys

def generate_experience(data, sectionName, title):
    section = data[sectionName]
    if not section:
        return ""

    latex = "\\begin{rSection}{" + title + "}\n"
    for entry in section:
        if entry['include']:
            latex += "\\begin{rSubsection}{" + entry['name'] + "}{" + entry['start'] + " -- " + entry['end'] + "}{" + entry['role'] + "}\n"
            
            if entry['description']:
                for desc in entry['description']:
                    latex += "\\item " + desc + "\n"

            latex += "\\end{rSubsection}\n"

    latex += "\\end{rSection}\n"
    return latex

def generate_info(data):
    about = data['about']
    if not about:
        return ""

    latex = "\\name{" + about['name'] + "}\n"
    latex += "\\address{" + about['address'] + "}\n"
    latex += "\\address{" + about['phone'] + " \\ " + about['email'] + "}\n"

    return latex

def generate_summary(data):
    about = data['about']
    if not about:
        return ""

    return "\\begin{rSection}{Summary}\n" + about['summary'] + "\n\\end{rSection}\n"

def generate_education(data):
    return generate_experience(data, 'education', 'Education')

def generate_research(data):
    return generate_experience(data, 'research', 'Research Experience')

def generate_teaching(data):
    return generate_experience(data, 'teaching', 'Teaching Experience')

def generate_industry(data):
    return generate_experience(data, 'industry', 'Industry Experience')

def generate_volunteering(data):
    return generate_experience(data, 'volunteering', 'Positions of Responsibility')

def generate_posters(data):
    posters = data['posters']
    if not posters:
        return ""

    latex = "\\begin{rSection}{Posters}\n"
    for poster in posters:
        if poster['include']:
            latex += "\\begin{rSubsection}{" + poster['authors'] + "(" + poster['date'] + ")}{}{" + poster['title'] + "}\n"
            latex += poster['description'] + "\n"
            latex += "\\end{rSubsection}\n"

    latex += "\\end{rSection}\n"
    return latex

def generate_awards(data):
    awards = data['awards']
    if not awards:
        return ""

    latex = "\\begin{rSection}{Awards}\n"
    for award in awards:
        if award['include']:
            latex += award['name'] + "\n"
    
    latex += "\\end{rSection}\n"
    return latex

def generate_skills(data):
    return ""  # TODO: implement this!

def generate_conferences(data):
    conferences = data['conferences']
    if not conferences:
        return ""

    latex = "\\begin{rSection}{Conferences Attended}\n"
    latex += "\\begin{tabular}{ @{} >{\\bfseries}l @{\\hspace{6ex}} l }"
    for conf in conferences:
        if conf['include']:
            latex += conf['date'] + " & " + conf['name'] + ", " + conf['location'] + "\\\\"

    latex += "\\end{tabular}\\end{rSection}\n"
    return latex

def generate_references(data):
    references = data['references']
    if not references:
        return ""

    latex = "\\begin{rSection}{References}\n"

    if type(references) is list:
        # TODO: update if i add references
        for ref in references:
            latex += "\\textbf{" + ref['name'] + "} \\hfill " + ref['contact'] + "\n"
            latex += ref['relation'] + "\n\n"
    else:
        latex += references + "\n"

    latex += "\\end{rSection}\n"
    return latex

def generate_cv(data):
    latex = "\\documentclass{resume}\n"
    latex += "\\usepackage[left=0.75in,top=0.6in,right=0.75in,bottom=0.6in]{geometry} % Document margins\n"

    latex += generate_info(data)
    latex += "\\begin{document}\n"

    latex += generate_summary(data)
    latex += generate_education(data)
    latex += generate_research(data)
    latex += generate_teaching(data)
    latex += generate_industry(data)
    latex += generate_volunteering(data)
    latex += generate_posters(data)
    latex += generate_awards(data)
    latex += generate_skills(data)
    latex += generate_conferences(data)
    latex += generate_references(data)

    latex += "\\end{document}"
    return latex

def main():
    # Get filename from args
    filename = 'cv.yaml'
    if len(sys.argv) > 1:
        filename = sys.argv[1]

    with open(filename, 'r') as file:
        data = yaml.safe_load(file)

    latex_output = generate_cv(data)

    outfile_name = 'out/' + data['about']['name'] + ' CV.tex'
    outfile = open(outfile_name, 'w')
    outfile.write(latex_output)
    outfile.close()

    print(f"Generated CV at '{outfile_name}'")

if __name__ == '__main__':
    main()