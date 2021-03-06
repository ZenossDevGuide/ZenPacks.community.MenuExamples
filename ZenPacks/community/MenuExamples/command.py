import Globals
from Products.ZenUtils.Utils import unused
unused(Globals)

import os
from Products.ZenUtils.Utils import executeCommand
from Products.ZenUtils.jsonutils import unjson
from Products.ZenUI3.browser.streaming import StreamingView
import logging
log = logging.getLogger('.'.join(['zen', __name__]))

# MyPredefinedCommandView is used in several menus to create a popup window
#  containing "Hello" and "World" followed by the url argument and the uid (which may be null)
#  Runs the mywrapper_script1 script in the ZenPack's libexec directory

class MyPredefinedCommandView(StreamingView):

    def stream(self):
    # Setup a logging file
        lf = os.path.join(os.environ['ZENHOME'], 'log/example_logging.log')
        logfile = open(lf, 'a')

        logfile.write('Start logging')
        # data is a list that will contain 2 elements:
        #   the url argument and the uid
        data = unjson(self.request.get('data'))
        logfile.write(' data is \n' % (data))
        try:
            args = data['args']
            logfile.write('Argument is %s \n' % (args))
            arg3 = args
        except:
            logfile.write(' No args \n')
            arg3 = ''
        try:
            uids = data['uids']
            logfile.write('uids is %s \n' % (uids))
            arg4 = uids
        except:
            logfile.write('No uids \n')
            arg4 = ''

        libexec = os.path.join(os.path.dirname(__file__), 'libexec')

        arg1 = "Hello"
        arg2 = "World"

        # Find the  script in the libexec directory of the ZenPack
        myPredefinedCmd1 = [
             libexec + '/mywrapper_script1',
            arg1, arg2, arg3, arg4
        ]
        logfile.write(' myPredefinedCmd1 is %s ' % (myPredefinedCmd1))
        self.write('Preparing my command...')
        result = executeCommand(myPredefinedCmd1, None, write=self.write)
        self.write('End of command...')
        logfile.close()
        return result


