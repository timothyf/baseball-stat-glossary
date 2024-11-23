import pandas as pd
from stat_categories import standard_categories, advanced_categories


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
    file.write("<!DOCTYPE html>\n<html>\n<head>\n<title>Advanced Baseball Stats Glossary</title>\n")
    file.write("<meta name='viewport' content='width=device-width, initial-scale=1.0'>\n")
    file.write(f"<link rel='stylesheet' type='text/css' href='{CSS_FILE_PATH}'>\n")
    file.write(f"<script src='{JS_FILE_PATH}'></script>\n")
    file.write("</head>\n<body>\n")
    file.write("<h1>Advanced Baseball Stats Glossary</h1>\n")

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
    """
    Writes the Table of Contents with two levels of hierarchy and up to 4 columns for stats within each category.
    Each column can have a maximum of 10 entries.
    """
    file.write("<nav id='toc-nav'>\n<h2>Stats by Category</h2>\n")
    
    # Top-level "Standard Stats" section
    file.write("<button class='collapsible first standard'>Standard Stats</button>\n")
    file.write("<div class='content'>\n<ul>\n")
    for category, stats in standard_categories.items():
        file.write(f"<li><button class='collapsible standard'>{category}</button>\n")
        file.write("<div class='content'>\n<div class='toc-category-container'>\n")
        
        # Sort stats alphabetically
        sorted_stats = sorted(stats)
        
        # Determine the number of columns and split stats accordingly
        max_items_per_column = 10
        num_columns = min(4, -(-len(sorted_stats) // max_items_per_column))  # Ceiling division
        split_size = len(sorted_stats) // num_columns + (len(sorted_stats) % num_columns > 0)
        toc_columns = [
            sorted_stats[i * split_size: (i + 1) * split_size] for i in range(num_columns)
        ]
        
        # Create up to 4 columns
        for col_items in toc_columns:
            file.write("<div class='toc-column'><ul>\n")
            for stat in col_items:
                anchor_link = slugify(stat)
                file.write(f"<li><a href='#{anchor_link}'>{stat}</a></li>\n")
            file.write("</ul></div>\n")
        
        file.write("</div></div></li>\n")  # Close category and content divs
    file.write("</ul>\n</div>\n")
    
    # Top-level "Advanced Stats" section
    file.write("<button class='collapsible advanced'>Advanced Stats</button>\n")
    file.write("<div class='content'>\n<ul>\n")
    for category, stats in advanced_categories.items():
        file.write(f"<li><button class='collapsible advanced'>{category}</button>\n")
        file.write("<div class='content'>\n<div class='toc-category-container'>\n")
        
        # Sort stats alphabetically
        sorted_stats = sorted(stats)
        
        # Determine the number of columns and split stats accordingly
        num_columns = min(4, -(-len(sorted_stats) // max_items_per_column))  # Ceiling division
        split_size = len(sorted_stats) // num_columns + (len(sorted_stats) % num_columns > 0)
        toc_columns = [
            sorted_stats[i * split_size: (i + 1) * split_size] for i in range(num_columns)
        ]
        
        # Create up to 4 columns
        for col_items in toc_columns:
            file.write("<div class='toc-column'><ul>\n")
            for stat in col_items:
                anchor_link = slugify(stat)
                file.write(f"<li><a href='#{anchor_link}' class='advanced'>{stat}</a></li>\n")
            file.write("</ul></div>\n")
        
        file.write("</div></div></li>\n")  # Close category and content divs
    file.write("</ul>\n</div>\n")
    
    file.write("</nav>\n")


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
