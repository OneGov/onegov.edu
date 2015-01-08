from ftw.upgrade import UpgradeStep


class InstallFtwUpgrade(UpgradeStep):
    """Install ftw.upgrade.
    """

    def __call__(self):
        self.setup_install_profile('profile-ftw.upgrade:default')
