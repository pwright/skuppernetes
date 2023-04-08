import os

site_url = os.environ.get("SITE_URL", "")

def path_nav(page):
    separator = "<span class=\"path-separator\">&#8250;</span>"
    links = [x.replace("href=\"", f"href=\"{site_url}") for x in list(page.path_nav_links)[1:]]
    links = separator.join(links)

    return f"<nav class=\"path-nav\">{links}</nav>"

def html_link(content, href=None):
    if href is None:
        return f"<a>{content}</a>"
    else:
        return f"<a href=\"{href}\">{content}</a>"

def table_button(content, href=None):
    if href is None:
        return f"<a class=\"table-button\">{content}</a>"
    else:
        return f"<a class=\"table-button\" href=\"{href}\">{content}</a>"

def cell(column_index, value):
    if column_index == 1:
        value = html_link(value)

    return f"<td>{value}</td>"

data = (
    ("frontend", "http://frontend:8080"),
    ("inventory", "http://inventory:8080"),
    ("orders", "http://orders:8080"),
    ("database", "jdbc://database:5432"),
    ("reviews", "http://reviews:8080"),
)

connection_url_table = html_table(data, headings=("Service", "Connection URL"), cell_fn=cell, style="width: 50%;")

def cell(column_index, value):
    if column_index == 0:
        value = html_link(value)
    elif column_index == 3:
        value = table_button("Delete")

    return f"<td>{value}</td>"

headings = "Name", "Status", "Created", "Actions"

data = (
    ("warehouse", "OK", "1/8/2020", None),
    ("headquarters", "Error: Unreachable", "3/15/2020", None),
)

link_table = html_table(data, headings=headings, cell_fn=cell)

headings = "Name", "Created"

data = (
    ("delivery-truck-201", "10/18/2021"),
    ("delivery-truck-202", "11/8/2021"),
)

incoming_link_table = html_table(data, headings=headings)

props = (
    ("Name", "storefront"),
    ("Ingress", "None"),
    ("Console enabled?", "Yes"),
    ("Routers", 1),
    ("Router CPU request", 1.0),
    ("Router CPU limit", 1.0),
)

site_settings = html_table(props, class_="properties")

props = (
    ("Version", "1.2.3"),
    ("Created", "2 days ago",),
)

site_properties = html_table(props, class_="properties")

def cell(column_index, value):
    if column_index == 3:
        value = table_button("Create a binding")

    return f"<td>{value}</td>"

headings = "Name", "Replicas", "Bindings", "Actions"

data = (
    ("frontend", 3, html_link("frontend-2da6", href=f"{site_url}/services/frontend/bindings/frontend-2da6/index.html"), None),
    ("reviews", 2, "-", None),
    ("orders", 2, "-", None),
)

deployment_table = html_table(data, headings=headings, cell_fn=cell)

def cell(column_index, value):
    if column_index == 0:
        value = html_link(value, href="frontend/index.html")
    elif column_index == 4:
        value = table_button("Delete")

    return f"<td>{value}</td>"

headings = "Name", "Status", "Bindings", "Created", "Actions"

data = (
    ("frontend", "OK", 2, "3 minutes ago", None),
    ("inventory", "OK", 1, "4 hours ago", None),
    ("orders", "OK", 1, "2 days ago", None),
    ("database", "OK", 1, "3/15/2020", None),
    ("reviews", "Error: No bindings", 0, "3/15/2020", None),
)

service_table = html_table(data, headings=headings, cell_fn=cell)

def cell(column_index, value):
    if column_index == 0:
        value = html_link(value)
    elif column_index == 4:
        value = " ".join((table_button("Download"), table_button("Delete")))

    return f"<td>{value}</td>"

headings = "Name", "Use limit", "Expiry", "Created", "Actions"

data = (
    ("storefront-token-1", 1, "15 minutes", "3 minutes ago", None),
    ("storefront-token-2", "None", "24 hours", "2 hours ago", None),
)

token_table = html_table(data, headings=headings, cell_fn=cell)

props = (
    ("Name", "storefront-token-1"),
    ("Use limit", 1),
    ("Expiry", "15 minutes"),
    ("Created", "3 minutes ago"),
)

token_properties = html_table(props, class_="properties")
