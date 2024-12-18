import pandas as pd
from stat_categories import standard_categories, advanced_categories
from generate_toc import generate_toc


# Constants
CSS_FILE_PATH = "styles/main.css"
JS_FILE_PATH = "javascript/main.js"
HTML_FILE_PATH = "advanced-baseball-stats.html"
CSV_FILE_PATH = "advanced-baseball-stats.csv"

def slugify(text):
    """
    Converts text into a slug suitable for HTML id and anchor links.
    """
    return text.lower().replace(" ", "-").replace("/", "-").replace("%", "").replace(".", "")

def write_html_glossary(df, standard_categories, advanced_categories):
    """
    Writes the HTML glossary from the DataFrame and categories.
    """
    with open(HTML_FILE_PATH, 'w') as file:
        write_html_header(file)
        write_search_bar(file)
        write_table_of_contents(file, standard_categories, advanced_categories)
        write_glossary_sections(file, df, standard_categories, advanced_categories)
        write_html_footer(file)

def write_html_header(file):
    """
    Writes the HTML header section.
    """
    file.write("<!DOCTYPE html>\n<html>\n<head>\n<title>Baseball Stats</title>\n")
    file.write("<meta name='viewport' content='width=device-width, initial-scale=1.0'>\n")
    file.write(f"<link rel='stylesheet' type='text/css' href='{CSS_FILE_PATH}'>\n")
    file.write(f"<script src='{JS_FILE_PATH}'></script>\n")
    file.write("</head>\n<body>\n")
    file.write("<h1>Baseball Stats</h1>\n")

def write_search_bar(file):
    """
    Writes the search bar section with "SEARCH" label on the left and two search boxes on the right.
    """
    file.write("<nav>\n<div class='search-container' style='display: flex; align-items: center; justify-content: space-between;'>\n")
    file.write("<label id='search-label'>SEARCH</label>\n")
    file.write("<div id='search-btn-div'>\n")
    file.write("<input type='text' id='search-input' placeholder='Stat name...'>\n")
    file.write("<input type='text' id='full-search-input' placeholder='Full text search...'>\n")
    file.write("</div>\n")
    file.write("</div>\n</nav>\n")


def write_table_of_contents(file, standard_categories, advanced_categories):
    html = generate_toc(standard_categories, advanced_categories)
    file.write(html)

def write_glossary_sections(file, df, standard_categories, advanced_categories):
    """
    Writes each glossary section from the DataFrame.
    Adds the class 'advanced' to the button if the stat is in an advanced category.
    Includes alternate names in parentheses after the stat name on the button.
    """
    # Flatten advanced categories into a set of advanced stats
    advanced_stats = set(stat for category in advanced_categories.values() for stat in category)
    standard_stats = set(stat for category in standard_categories.values() for stat in category)

    file.write("<nav>\n<h2>All Stats</h2>\n")
    file.write("<div class='glossary'>\n")
    for _, row in df.iterrows():
        stat_anchor = slugify(row['Stat'])
        # Check if the stat belongs to an advanced or standard category
        is_advanced = row['Stat'] in advanced_stats
        is_standard = row['Stat'] in standard_stats
        if is_standard:
            button_class = "collapsible standard"
        elif is_advanced:
            button_class = "collapsible advanced"
        else:
            button_class = "collapsible"

        # Include the alternate name if available
        alternate_name = f"<span class='alt-name'>({row['Alternate Name']})</span>" if not pd.isnull(row['Alternate Name']) else ""
        file.write(f"<button class='{button_class}' id='{stat_anchor}'>{row['Stat']}{alternate_name}</button>\n")

        file.write("<div class='content'>\n")
        file.write(f"<p>{row['Description']}</p>\n")
        for column in df.columns:
            if column != 'Stat' and column != 'Alternate Name' and column != 'Description' and not pd.isnull(row[column]):
                file.write(f"<p><strong>{column}:</strong> {row[column]}</p>\n")
        file.write("</div>\n")
    file.write("</div>\n")



def write_html_footer(file):
    """
    Writes the HTML footer section.
    """
    file.write("<footer>Generated by Baseball Stats Glossary Tool</footer>\n")
    file.write("</body>\n</html>")

def convert_csv_to_html_glossary():
    """
    Main function to read the CSV and generate the HTML glossary.
    """
    # Read and sort the DataFrame
    df = pd.read_csv(CSV_FILE_PATH).sort_values(by='Stat', key=lambda col: col.str.lower())

    # Write the glossary
    write_html_glossary(df, standard_categories, advanced_categories)

# Run the script
convert_csv_to_html_glossary()
