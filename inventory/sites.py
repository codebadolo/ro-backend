# sites.py
from unfold.sites import UnfoldAdminSite

class StockAdminSite(UnfoldAdminSite):
    site_title = "Stock"
    site_header = "Stock Management"
    index_title = "Welcome to Stock Admin"

stock_admin_site = StockAdminSite(name="stock_admin_site")