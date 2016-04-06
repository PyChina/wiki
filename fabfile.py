from fabric.api import *
import fabric.contrib.project as project
import os

# Local path configuration (can be absolute or relative to fabfile)
env.deploy_path = 'html'
env.static_path = '_static'

def build():
    local('markdoc build && '
            #'ls -la && '
            'rsync -avzP4 {static_path}/media/ {deploy_path}/media/ && '
            'pwd '.format(**env)
        )

def serve():
    local('markdoc serve')

def reserve():
    build()
    serve()

def CNAME():
    local('ls -la {deploy_path}/ && '
            'cp -f {static_path}/CNAME {deploy_path}/ && '
            'cp -f {static_path}/.nojekyll {deploy_path}/ && '
            'pwd '.format(**env)
        )

def gh_pages():
    local('cd {deploy_path} && '
            'pwd && '
            'git st && '
            'git add --all . && '
            'git ci -am "re-build from local by markdoc @MBP111216ZQ" && '
            #'git pu cafe gitcafe-page '
            'git pu && '
            'date '.format(**env)
          )

def pub():
    build()
    CNAME()
    gh_pages()

'''
env.qrsync_bin = '/opt/bin/7niu_package_darwin_amd64/qrsync'
env.qrsync_cfg = '../7niu4pychina.json'
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

'''