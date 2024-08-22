AUTHOR = 'Leonardo Venturoso'
SITENAME = 'Leonardo Venturoso'
SITEURL = ""

PATH = "content"

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
AUTHOR = "Leonardo Venturoso"
SITENAME = "Leonardo Venturoso"
SITEURL = 'http://127.0.0.1:8000'
SITE_DESCRIPTION = (
    "My personal website. Here, you can read my blog posts, and learn about my"
    " projects. I write about data science, AI, programming, business, and"
    " other topics. "
)
# TODO
SITELOGO = "images/logo-resized.png"
PATH = "content"
TIMEZONE = "Europe/Rome"
DEFAULT_LANG = "en"

PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}.html"
PAGE_PATHS = ["pages"]
DEFAULT_CATEGORY = "blog"
ARTICLE_URL = "{category}/{slug}.html"
ARTICLE_SAVE_AS = "{category}/{slug}.html"
ARTICLE_EXCLUDES = ["html"]
ARTICLE_PATHS = ["posts"]
CATEGORY_URL = "category/{slug}.html"
CATEGORY_SAVE_AS = "category/{slug}.html"
USE_FOLDER_AS_CATEGORY = False
DRAFT_URL = "drafts/{slug}.html"


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
FEED_ALL_ATOM = "feeds/all.atom.xml"


# NO EXTRAS
TAGS_SAVE_AS = None
ARCHIVES_SAVE_AS = None
CATEGORIES_SAVE_AS = None
AUTHORS_SAVE_AS = None

# pagination
DEFAULT_PAGINATION = False

# extra paths
STATIC_PATHS = [
    "images",
    "pdfs",
    "extra/robots.txt",
    "pdfs/cv.pdf",
    "extra/CNAME",
    "html",
    "extra/favicons",
]


EXTRA_PATH_METADATA = {
    "extra/robots.txt": {"path": "robots.txt"},
    "pdfs/cv.pdf": {"path": "cv.pdf"},
    "extra/CNAME": {"extra/CNAME": {"path": "CNAME"}},
    "html/StateOfVim.html": {"path": "StateOfVim.html"},
}

FAVICONS_LIST = [
    "android-chrome-192x192.png",
    "android-chrome-512x512.png",
    "apple-touch-icon.png",
    "favicon-16x16.png",
    "favicon-32x32.png",
    "favicon.ico",
    "site.webmanifest",
]

for favicon in FAVICONS_LIST:
    EXTRA_PATH_METADATA[f"extra/favicons/{favicon}"] = {"path": f"favicons/{favicon}"}

# MARKDOWN
MARKDOWN = {
    "extensions": [
        "markdown.extensions.toc",
        "markdown.extensions.fenced_code",
        "markdown.extensions.codehilite",
    ]
}

# PLUGINS
PLUGIN_PATHS = ["plugins"]
PLUGINS = [
    "pelican.plugins.feed_filter",
    "sitemap",
    "simple_footnotes",
]
SITEMAP = {
    "exclude": ["archives.html", "author/", "category/", "photos/"],
    "format": "xml",
    "priorities": {"articles": 0.9, "indexes": 0.5, "pages": 0.9},
    "changefreqs": {
        "articles": "hourly",
        "indexes": "hourly",
        "pages": "hourly",
    },
}