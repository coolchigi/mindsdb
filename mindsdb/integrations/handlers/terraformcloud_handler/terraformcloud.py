import json
import requests

class TerraformCloud:
    def __init__(self, token, org, workspace):
        self.token = token
        self.org = org
        self.workspace = workspace
        self.base_url = 'https://app.terraform.io/api/v2/organizations'
        self.headers = {
            'Authorization': f'Bearer {self.token}',
            'Content-Type': 'application/vnd.api+json'
        }

    def _get(self, url):
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def get_workspace(self):
        url = f'{self.base_url}/{self.org}/workspaces/{self.workspace}'
        print("Here is the url: ", url)
        return self._get(url)

    def get_workspace_runs(self):
        print("Inside get_workspace_runs")
        workspace = self.get_workspace()
        workspace_id = workspace['data']['id']
        print("Here is the workspace id: ", workspace_id)
        url = f"https://app.terraform.io/api/v2/workspaces/{workspace_id}/runs"
        print("Here is the url: ", url)
        runs = self._get(url)

        if runs and 'data' in runs:
            run_statuses = {run['id']: run['attributes']['status'] for run in runs['data']}
            return run_statuses
        else:
            return None
            
    def get_workspace_run(self, run_id):
        workspace = self.get_workspace()
        url = f'https://app.terraform.io/api/v2/organizations/{self.org}/workspaces/{workspace}/runs/{run_id}'
        return self.get(url)

    def get_workspace_run_outputs(self, run_id):
        run = self.get_workspace_run(run_id)
        url = run['data']['relationships']['outputs']['links']['related']
        return self.get(url)

    def get_workspace_run_output(self, run_id, output_name):
        outputs = self.get_workspace_run_outputs(run_id)
        url = outputs['data'][0]['relationships']['output']['links']['related']
        return self.get(url)

    def get_workspace_run_output_value(self, run_id, output_name):
        output = self.get_workspace_run_output(run_id, output_name)
        return output['data']['attributes']['value']

    def get_workspace_run_output_sensitive(self, run_id, output_name):
        output = self.get_workspace_run_output(run_id, output_name)
        return output['data']['attributes']['sensitive']

    def get_workspace_run_output_sensitive_value(self, run_id, output_name):
        output = self.get_workspace_run_output(run_id, output_name)
        return output['data']['attributes']['sensitive_value']

    def get_workspace_run_output_sensitive_value(self, run_id, output_name):
        output = self.get_workspace_run_output(run_id, output_name)
        return output['data']['attributes']['sensitive_value']

    def get_workspace_run_output_sensitive_value(self, run_id, output_name):
        output = self.get_workspace_run_output(run_id, output_name)
        return output['data']['attributes']['sensitive_value']