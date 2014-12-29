from fabric.api import *
import fabric.contrib.project as project
import os

# Local path configuration (can be absolute or relative to fabfile)
env.deploy_path = '.html'
env.qrsync_bin = '/opt/bin/7niu_package_darwin_amd64/qrsync'
env.qrsync_cfg = '../7niu-zhgdg.json'


def serve():
    local('markdoc serve')
def reserve():
    build()
    serve()
def build():
    local('markdoc build')

def p2cafe():
    build()
    local('pwd && '
            'cd {deploy_path} && '
            #'ls -la && '
            'git st && '
            'git add --all . && '
            'git ci -am "re-gen. by markdoc. @MBP111216ZQ" && '
            'git pu && '
            #'ls && '
            'pwd '.format(**env)
          )
def pub7niu():
    build()
    local('pwd && '
            #'git pu && '
            '{qrsync_bin} {qrsync_cfg} && '
            #'ls && '
            'pwd '.format(**env)
          )

