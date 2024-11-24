
def generate_toc(standard_categories, advanced_categories):
    """
    Generates the Table of Contents with two levels of hierarchy and up to 4 columns for stats within each category.
    Each column can have a maximum of 10 entries.
    """
    html_output = "<nav id='toc-nav'>\n<h2>Stats by Category</h2>\n"
    
    # Top-level "Standard Stats" section
    html_output += "<button class='collapsible first standard'>Standard Stats</button>\n"
    html_output += "<div class='content'>\n<ul>\n"
    for category, stats in standard_categories.items():
        html_output += f"<li><button class='collapsible standard'>{category}</button>\n"
        html_output += "<div class='content'>\n<div class='toc-category-container'>\n"
        
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
            html_output += "<div class='toc-column'><ul>\n"
            for stat in col_items:
                anchor_link = slugify(stat)
                html_output += f"<li><a href='#{anchor_link}'>{stat}</a></li>\n"
            html_output += "</ul></div>\n"
        
        html_output += "</div></div></li>\n"  # Close category and content divs
    html_output += "</ul>\n</div>\n"
    
    # Top-level "Advanced Stats" section
    html_output += "<button class='collapsible advanced'>Advanced Stats</button>\n"
    html_output += "<div class='content'>\n<ul>\n"
    for category, stats in advanced_categories.items():
        html_output += f"<li><button class='collapsible advanced'>{category}</button>\n"
        html_output += "<div class='content'>\n<div class='toc-category-container'>\n"
        
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
            html_output += "<div class='toc-column'><ul>\n"
            for stat in col_items:
                anchor_link = slugify(stat)
                html_output += f"<li><a href='#{anchor_link}' class='advanced'>{stat}</a></li>\n"
            html_output += "</ul></div>\n"
        
        html_output += "</div></div></li>\n"  # Close category and content divs
    html_output += "</ul>\n</div>\n"
    
    html_output += "</nav>\n"
    
    return html_output

def slugify(text):
    """
    Converts text into a slug suitable for HTML id and anchor links.
    """
    return text.lower().replace(" ", "-").replace("/", "-").replace("%", "").replace(".", "")