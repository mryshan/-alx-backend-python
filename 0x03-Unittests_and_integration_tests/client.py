#!/usr/bin/env python3
"""Github Org Client module"""
import requests



def get_json(url):
    """Fetch JSON data from a URL"""
    return requests.get(url).json()


class GithubOrgClient:
    """Client to interact with GitHub organization data"""

    ORG_URL = "https://api.github.com/orgs/{}"

    def __init__(self, org_name):
        self.org_name = org_name

    @property
    def org(self):
        """Return organization data"""
        return get_json(self.ORG_URL.format(self.org_name))

    @property
    def _public_repos_url(self):
        """Extracts the public repositories URL from org data"""
        return self.org.get("repos_url")

    def public_repos(self, license=None):
        """Return the list of public repos filtered by license (optional)"""
        repos = get_json(self._public_repos_url)
        if license is None:
            return [repo["name"] for repo in repos]
        return [
            repo["name"]
            for repo in repos
            if self.has_license(repo, license)
        ]

    @staticmethod
    def has_license(repo, license_key):
        """Check if repo has the specified license"""
        return repo.get("license", {}).get("key") == license_key
