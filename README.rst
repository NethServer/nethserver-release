.. _nethserver-release-module:

nethserver-release
==================

This RPM can be installed on a plain CentOS 7 minimal. It provides the
``nethserver-install`` command that downloads, installs and configures
additional YUM repositories and RPMs for the NethServer system.

Building a release RPM
----------------------

1. The Version tag is fixed to "7". Increment the .spec file Release tag (e.g.: "12%{?dist}")
2. Write the %changelog entry in the .spec file
3. Commit the above changes
5. Create a git tag like "7r12". Do not use any "-" (minus) sign as separator!
6. Push the tag and the commit to start the automated build on Travis CI

Builds started from a tagged commit are published to "updates"!

More information: https://docs.nethserver.org/projects/nethserver-devel/en/v7/building_rpms.html
