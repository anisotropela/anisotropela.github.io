import ads
import html
from pathlib import Path

"""
Purpose
-------
    Retrieve papers from ADS and outputs them in an .html file.

    More specifically this script:
        - Queries ADS for an author
        - Sorts by year (descending)
        - Extracts title, authors, journal, volume, page, year
        - Turns title into a link to the paper
        - Lists all authors up to and including the user,
  		  unless there are too many
        - Outputs HTML

Prerequisites
-------------
    1. To run the script, an ADS API key is needed:
         - Create one at https://ui.adsabs.harvard.edu/user/settings/token
         - For one-time use, you can set it as an environment variable:
             $ export ADS_API_KEY="your_api_key"
           but it is better to add the key to a file ~/.ads/dev_key
             $ mkdir .ads
             $ echo "your_api_key" > ~/.ads/dev_key
    2. The Python package "ads". Install with
         $ pip install ads
       (or perhaps with conda?) 

Usage
-----
	Run the script with:
    	$ python get_pub_list.py

    Some hardcoding is needed: Substrings from titles of unwanted papers are
    given below in the key word `exclude_titles`.
 	Other key words are explained below.
"""

# User settings ---------------------------------------------------------------
author         = 'toft, s'                   # First name or initial is needed
refereed       = 'refereed'                  # or 'notrefereed'. This is 'property" on ADS, but that's a built-in function in ADS, so...
year           = '2000-'                     
max_authors    = 10                          # Max no. of author before writing "et al." instead. All authors up to and including `author` are listed, as long as there are < max_authors
outfile        = Path("./publications.html") # Results are written in .html format, to be viewed in a browser
bullets        = True                        # Add bullets to list? (or just list results) 
print_query    = False                       # Print ADS queary to std. output
exclude_titles = [                           # Exclude titles with the following substrings:
    "Diet of raccoon dogs",
    "Prey killing rate",
    "The spider fauna",
    "time to kill in the soil",
    "Occurrence, spatiotemporal trends",
    "Lack of Female Preference for Nuptial Gifts",
    "Spatiotemporal trends and impact",
    "two invasive harvestmen",
    "Sperm competition intensity",
    "Macronutrient niches",
    "omnivorous carnivores",
    "Prey acceptance and metabolic",
    "Habitat specialist spiders",
    "Fly disturbance suppresses",
    "Sperm competition tactics",
    "Maintenance of deceptive gifts",
    "on kill rate and reproduction",
    "Ten years after the invasion",
    "Cold acclimation reduces",
    "Negative effects of low",
    "in a carnivorous beetle",
    "of gifts in spiders",
    "Balancing of lipid",
    "Spider web and silk",
    "Danish yellow dunes",
    "Can differential nutrient",
    "Optimal numbers of matings",
    "Cold-acclimation increases",
    "gift wrapping when choosing mates",
    "Condition dependence of male",
    "Dome-shaped functional",
    "subsocial spider",
    "Nutrient regulation in a predator",
    "gift-giving spider",
    "A specialized araneophagic",
    "The advantage of starving",
    "Protein and carbohydrate",
    "Nutrient balance affects",
    "success in male spiders",
    "Can ant-eating Zodarion",
    "results from a Danish population",
    "Balancing of protein",
    "Why Do Males of the Spider",
    "Thanatosis as an adaptive",
    "Temperature and prey",
    "Dietary and prey-capture",
    "Nutrient-Specific Compensation",
    "Nuptial gifts of male spiders",
    "Tachyporus hypnorum",
    "Death feigning in the face",
    "Nutritional value of cannibalism",
    "The quality of aphids as food",
    "Effects of alternative prey",
    "Compensatory growth following",
    "exposed wolf spiders",
    "Biological Control in Rice",
    "food for a generalist predator",
    "Importance of insect prey",
    "Artificial selection for aphid",
    "The three-dimensional macronutrient",
    "Hunger-dependent female receptivity",
    "Foraging in Invertebrate Predators",
    "Nutrient composition of the"
]


# Build ADS query -------------------------------------------------------------
not_titles = " OR ".join(f'title:"{t}"' for t in exclude_titles)
query_string = 'author:"'  + author       + '" ' \
             + 'property:' + refereed     + ' '  \
             + 'year:'     + year         + ' '  \
             + 'NOT ('     + not_titles   + ')'
if print_query:
    print("ADS query:\n" + query_string)


# Author handling -------------------------------------------------------------
lastName = (
    author      
    .split(",")[0]      # toft
    .strip()
    .lower()
)

def is_author(currentAuthor):
    """
    Returns True if this author matches the author surname.
    """
    return currentAuthor.lower().startswith(f"{lastName},")

def format_authors(authors):
    """
    If author is among the first max_authors authors:
      -> list all authors up to and including the author (and boldface it)
    else:
      -> FirstAuthor et al.
    """
    for i, a in enumerate(authors):
        if is_author(a):
            if i < max_authors:
                out = []
                for b in authors[: i + 1]:
                    last = b.split(",")[0]
                    if is_author(b):
                        out.append(f"<b>{last}</b>")
                    else:
                        out.append(last)
                return ", ".join(out)
            else:
                first = authors[0].split(",")[0]
                return f"{first} et al."

    # Fallback (should not happen given query)
    first = authors[0].split(",")[0]
    return f"{first} et al."


# Run query -------------------------------------------------------------------
print('Querying ADS...')
query = ads.SearchQuery(
    q=query_string,
    fl=[
        "title",
        "author",
        "year",
        "pub",
        "volume",
        "page",
        "doi",
        "adsurl",
    ],
    sort="date desc",
    rows=2000,
)
papers = list(query)
print(f"ADS returned {len(papers)} records")


# Write html ------------------------------------------------------------------
if bullets:
    li0,li1 = '<li>','</li>'
    ul0,ul1 = '<ul>','</ul>'
else:
    li0,li1 = '','<br>'
    ul0,ul1 = '',''

lines = [
    "<!DOCTYPE html>",
    "<html>",
    "<head>",
    '<meta charset="utf-8">',
    "<title>Publication list</title>",
    "</head>",
    "<body>",
    "<h2>Publications</h2>",
    ul0,
]

for p in papers:
    # This handles (missing) .html syntax in titles # # #
    title_raw = html.unescape(p.title[0])               #
    title_raw = (                                       #
        title_raw                                       #
        .replace("<SUB>", "<sub>")                      #
        .replace("</SUB>", "</sub>")                    #
        .replace("<SUP>", "<sup>")                      #
        .replace("</SUP>", "</sup>")                    #
    )                                                   #
    title = html.escape(title_raw, quote=False)         #
    title = (                                           #
        title                                           #
        .replace("&lt;sub&gt;", "<sub>")                #
        .replace("&lt;/sub&gt;", "</sub>")              #
        .replace("&lt;sup&gt;", "<sup>")                #
        .replace("&lt;/sup&gt;", "</sup>")              #
    )                               # # # # # # # # # # #
    authors = format_authors(p.author or [])
    journal = html.escape(p.pub or "")
    volume = p.volume or ""
    page = p.page[0] if p.page else ""
    year = p.year or ""

    if p.doi:
        url = f"https://doi.org/{p.doi[0]}"
    else:
        url = p.adsurl

    entry = (
        f'{li0}<a href="{url}">{title}</a>, '
        f'{authors}, {year}, {journal} {volume}, {page}{li1}'
    )
    lines.append(entry)

lines += [
    ul1,
    "</body>",
    "</html>",
    ]

outfile.write_text("\n".join(lines), encoding="utf-8")

print(f"Wrote {len(papers)} publications to '{outfile}'")
