from core.terraform.resources.misc import NullResource
from core.config import Settings

class DeployAddAccountServerless(NullResource):
    action = Settings.running_command.split(" ")[1]
    action_map = {
        "install": "deploy",
        "destroy": "remove",
        "redeploy": "deploy"
    }
    command = "sls %s -vv" % action_map.get("action", "deploy")
    working_dir = "/tmp/glaze-add-account-api/serverless"
    # interpreter = "/bin/bash"
    def get_provisioners(self):
        local_execs = [
            {
                'local-exec': {
                    'command': self.command,
                    "working_dir": self.working_dir
                }
            }

        ]
        return local_execs