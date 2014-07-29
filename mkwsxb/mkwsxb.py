"""Embed widgets from MKWS, the MasterKey Widget Set"""

import pkg_resources

from xblock.core import XBlock
from xblock.fields import Integer, Scope, String, Any, Boolean, Dict
from xblock.fragment import Fragment

class MKWSXB(XBlock):
    """Embed widgets from MKWS, the MasterKey Widget Set"""

    # Fields
    query = String(
      help="Search query",
      default="water",
      scope=Scope.content
    )

    def resource_string(self, path):
        """Helper for accessing resources."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    def student_view(self, context=None):
        """The primary view of the MKWS XBlock, shown to students when viewing courses."""
        html = self.resource_string("static/html/mkwsxb.html")
        frag = Fragment(html.format(query=self.query))
        frag.add_javascript_url("//mkws.indexdata.com/mkws-complete.js")
        frag.add_javascript_url("//example.indexdata.com/mkws-widget-ru.js")
        frag.add_css(self.resource_string("static/css/mkws-widget-ru.css"))
        frag.add_javascript(self.resource_string("static/js/src/mkwsxb.js"))
        frag.initialize_js('MKWSXB')
        return frag;

    def studio_view(self, context=None):
        """Studio configuration view."""
        html = self.resource_string("static/html/settings.html")
        frag = Fragment(html.format(query=self.query))
        frag.add_javascript(self.resource_string("static/js/src/settings.js"))
        frag.initialize_js('MKWSXBSettings')
        return frag

    @XBlock.json_handler
    def update_settings(self, data, suffix=''):
        """Studio configuration callback."""
        self.query = data['query']
        return {"result": "success"}

    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("MKWSXB",
             """<vertical_demo>
                <mkwsxb/>
                </vertical_demo>
             """),
        ]
