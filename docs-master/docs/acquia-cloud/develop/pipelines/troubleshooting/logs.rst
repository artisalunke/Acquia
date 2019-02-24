.. include:: /common/global.rst

Evaluating pipelines log messages
=================================

Troubleshooting |acquia-product:ac| pipelines

-  `Failures </acquia-cloud/develop/pipelines/troubleshooting/logs>`__
-  `Errors </acquia-cloud/develop/pipelines/troubleshooting/logs/errors>`__
-  Logs

The ``pipelines logs`` command returns the log entries for the
application ID and job ID that you specify. The log entries include
standard output and standard error messages from the job. To run the
``logs`` command, obtain your application ID and job ID, which can be
found in the output of the ``start`` command.

The logs command has the following format:

``pipelines logs``

The log output will appear similar to the following:

``Log messages for build job b33e87f1-1a53-4f29-afad-bc7d3290b603: ============================================================== 2016-08-31 08:03:36                                                        INFO --------------------------------------------------------------------------------     The task has been added. ============================================================== 2016-08-31 08:03:37                                                        INFO --------------------------------------------------------------------------------     The task has started. ============================================================== 2016-08-31 08:05:18                                                        INFO --------------------------------------------------------------------------------     Successfully executed the build script. Output:     Starting local build...     Build file: /mnt/tmp/local.prod/.decoded.yml     Source: /mnt/tmp/local.prod/buildsteps     Target: /mnt/tmp/local.prod/buildsteps     Beginning to build /mnt/tmp/local.prod/buildsteps/mybuilddir/d7.make.       [ok]     drupal cloned from http://git.drupal.org/project/drupal.git.                [ok]     Checked out tag 7.50.                                                       [ok]     drupal patched with 872999-9.patch.                                         [ok] ============================================================== 2016-08-31 08:05:19                                                        INFO --------------------------------------------------------------------------------     Workspace status:     AM docroot     R  d7.make -> mybuilddir/d7.make ============================================================== 2016-08-31 08:05:34                                                        INFO --------------------------------------------------------------------------------     Successfully completed the build task. ==============================================================``
