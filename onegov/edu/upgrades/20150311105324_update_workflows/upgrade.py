from ftw.upgrade import UpgradeStep


class UpdateWorkflows(UpgradeStep):
    """Update workflows.
    """

    def __call__(self):
        self.install_upgrade_profile()
        self.update_workflow_security(
            ['onegov_edu_intranet_workflow', 'onegov_edu_workflow'],
            reindex_security=False)
