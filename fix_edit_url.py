from mkdocs.plugins import BasePlugin
from mkdocs.config import config_options

class WikiEditUrlPlugin(BasePlugin):
    def on_page_context(self, context, page, config, nav):
        if 'edit_url' in context:
            edit_url = context['edit_url']
            if edit_url.endswith('.md'):
                context['edit_url'] = edit_url[:-3] + '/_edit'
        return context
