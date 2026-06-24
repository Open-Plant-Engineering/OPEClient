from pyopeclient.client.workflow import WorkflowClient


def test_full_workflow():
    client = WorkflowClient()

    # This should run full lifecycle
    client.run()