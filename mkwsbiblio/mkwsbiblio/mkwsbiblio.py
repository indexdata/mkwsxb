"""Embed bibliographic widget from MKWS, the MasterKey Widget Set"""

import pkg_resources
import random

from xblock.core import XBlock
from xblock.fields import Integer, Scope, String, Any, Boolean, Dict
from xblock.fragment import Fragment

class MKWSBiblio(XBlock):
    """Embed bibliographic widget from MKWS, the MasterKey Widget Set"""

    # Fields
    query = String(
      help="Search query",
      default="water",
      scope=Scope.content
    )
    recid = String(
      help="Record to display",
      default="content: title modern water resources engineering",
      scope=Scope.content
    )
    display_name = String(
      default="MKWS bibliographic details",
      scope=Scope.settings
    )

    def resource_string(self, path):
        """Helper for accessing resources."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    def student_view(self, context=None):
        """The primary view of the MKWS XBlock, shown to students when viewing courses."""
        html = self.resource_string("static/html/student.html")
        frag = Fragment(html.format(query=self.query, recid=self.recid, team=random.randint(0, 100000)))
        # student.js uses require.js as it cannot guarantee mkws-complete.js has loaded 
        # in studio without it. We'll need to add it if we're in the LMS:
        #frag.add_javascript_url("/static/js/vendor/require.js");
        frag.add_javascript_url("//cdnjs.cloudflare.com/ajax/libs/require.js/2.1.14/require.min.js");
        # frag.add_resource_url("//mkws.indexdata.com/mkws-complete", "text/javascript", "head");
        # frag.add_resource('<script src="//mkws.indexdata.com/mkws-complete.js"></script>', "text/html", "head");
        frag.add_css(self.resource_string("static/css/mkwsbiblio.css"))
        frag.add_javascript(self.resource_string("static/js/src/student.js"))
        frag.initialize_js('MKWSBiblio')
        return frag;

    def author_view(self, context=None):
        """The primary view of the MKWS XBlock, shown when authoring courses."""
        # This should closely mirror the student_view. Here all we do is not include
        # require.js as it's already in Studio and the lms path won't work.
        html = self.resource_string("static/html/student.html")
        frag = Fragment(html.format(query=self.query, recid=self.recid, team=random.randint(0, 100000)))
        frag.add_css(self.resource_string("static/css/mkwsbiblio.css"))
        frag.add_javascript(self.resource_string("static/js/src/student.js"))
        frag.initialize_js('MKWSBiblio')
        return frag;

    def studio_view(self, context=None):
        """Studio configuration view."""
        html = self.resource_string("static/html/settings.html")
        frag = Fragment(html.format(query=self.query, recid=self.recid))
        frag.add_javascript(self.resource_string("static/js/settings.js"))
        frag.initialize_js('MKWSBiblioSettings')
        return frag

    @XBlock.json_handler
    def update_settings(self, data, suffix=''):
        """Studio configuration callback."""
        self.query = data['query']
        self.recid = data['recid']
        return {"result": "success"}

    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("MKWSBiblio",
             """<vertical_demo>
                <mkwsbiblio/>
                </vertical_demo>
             """),
        ]
