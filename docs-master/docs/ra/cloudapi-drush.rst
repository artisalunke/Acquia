.. include:: /common/global.rst

Performing Acquia Automation security updates using CloudAPI and Drush
======================================================================

Acquia Automation provides security updates using a combination of
Acquia `CloudAPI </acquia-cloud/api>`__ and
`Drush </articles/drush-intro>`__. This document lists all relevant
commands, in order, for each step.

Requirements
------------

To replicate these steps, you will need the following items:

-  `Drush aliases </acquia-cloud/drush/aliases>`__
-  `CloudAPI </acquia-cloud/api>`__

.. admonition:: Notes

   -  Acquia RA uses the\ `RA environment </ra/environment>`__ for automation and deploying security updates. To perform the following steps, you will need to use another non-production environment such as Development.
   -  If the command is listed without ``@sitename.env``, it is assumed you are running on the server itself.
   -  You can run the same process from a local command line by adding the correct ``@sitename.env``.
   -  Acquia Automation is scripted to check and update all multisites. These commands are not included in the following steps.
   -  This process varies slightly for Drupal 8 due to different configuration commands.

Initial checks
--------------

Before starting, Acquia Automation examines the following items:

-  `RA preferences </ra/preferences>`__ for Do Not Inform
-  If the update status is currently paused
-  If a ``WELCOME`` tag is deployed on the Production environment.

If any of the previous states are not found, Acquia Automation proceeds.
At various points in the process, the RA preferences are checked to
ensure that the correct steps are taken.

Step One
--------

Check for updates:

a. Check the Production environment for security-only updates (run
   against each multisite separately):

   .. code-block:: none

      drush pm-updatestatus --security-only --fields='name,existing_version,candidate_version' --update-backend=drush --uri=default

b. Check the Production environment for Acquia-recommended updates:

   .. code-block:: none
   
      drush pm-updatestatus acquia_connector apachesolr memcache acquia_lift personalize visitor_actions --security-only --fields='name,existing_version,candidate_version' --update-backend=drush --uri=default

c. Check RA for an already fully updated branch (using the same drush
   commands as in the previous step).
d. If there are no updates or RA is secure, stop. Otherwise, complete
   the following steps:

RA preference check:

a. Inform Only: A ticket is created and the process is complete.
b. Update and Deploy: the process continues.

Prepare the RA Environment:

a. Production tag is deployed to the RA Environment (using
   drush/cloudapi):

   .. code-block:: none
   
      drush @sitename.ra ac-code-path-deploy $originating_tag

b. Databases are copied from the Production environment to RA (using
   drush/cloudapi):

   .. code-block:: none
   
      drush @sitename.prod ac-database-copy db_name ra

c. Download and install `Registry
   Rebuild <https://www.drupal.org/project/registry_rebuild>`__ and run
   to clean up changed paths:

   .. code-block:: none
   
      drush pm-download registry_rebuild-7.x --yes=TRUE
      drush rr --uri=default

d. Disable CSS/JS aggregation to fix Stage File Proxy issues:

   .. code-block:: none
   
      drush vset preprocess_js 0 --uri=default
      drush vset preprocess_css 0 --uri=default

e. Enable `LiveDev </acquia-cloud/develop/livedev>`__ on RA (using
   drush/cloudapi):

   .. code-block:: none
   
      drush @sitename.ra ac-environment-livedev action enable

Create and apply updates to the update branch while RA is in LiveDev:

a. Create the branch:

   .. code-block:: none
   
      git fetch --all --tags && git checkout -b $branch_name $originating_tag

b. Update core:

   .. code-block:: none
   
      drush pm-updatecode drupal --check-updatedb=0 --yes=TRUE --no-backup=TRUE --version-control=backup --security-only --uri=default

c. Commit the core update:

   .. code-block:: none
   
      git add . -A && git reset acquia-files; cd docroot && git reset sites/*/files files; git commit -m $commit_message

d. Update insecure and proactively maintained modules individually:

   .. code-block:: none
   
      drush pm-updatecode $module  --check-updatedb=0 --yes=TRUE --no-backup=TRUE --version-control=backup --uri=default --check-disabled

e. Commit the module updates:

   .. code-block:: none
   
      git add . -A && git reset acquia-files; cd docroot && git reset sites/*/files files;

f. Repeat the previous step until all modules are secure.
g. Look for and attempt to apply patches using `Drush Patch
   File <https://bitbucket.org/davereid/drush-patchfile>`__.
h. Add Stage File Proxy:

   .. code-block:: none
   
        drush pm-enable stage_file_proxy --yes=TRUE --uri=default
        drush php-eval ''print conf_path();'
        drush vget file_public_path   --uri=default
        drush variable-set stage_file_proxy_origin http://$site_url --uri=default
        drush variable-set stage_file_proxy_origin_dir sites/default/files   --uri=default
        drush variable-set stage_file_proxy_use_imagecache_root 1 --format=boolean --uri=default

i. Check for and disable Secure Pages:

   .. code-block:: none
   
      drush pm-info securepages --yes=TRUE --uri=default
      drush pm-disable securepages --yes=TRUE --uri=default

j. Run DB updates (run against each multisite separately):

   .. code-block:: none
   
      drush updatedb-status --uri=default

k. Push the updated branch to the repository:

   .. code-block:: none
   
      git push -u origin $branch_name

l. The new branch is deployed to the RA environment (using
   drush/cloudapi):

   .. code-block:: none
   
      drush @sitename.ra ac-code-path-deploy $branch_name

m. LiveDev is disabled (using drush/cloudapi):

   .. code-block:: none
   
      drush @sitename.ra ac-environment-livedev action disable

At this point in the process, Acquia RA generates a ticket listing what
updates were performed and what the next steps in the process are.

Step Two
--------

#. If necessary, redeploy the RA update branch to the RA environment
   (using drush/cloudapi):

   .. code-block:: none
   
      drush @sitename.ra ac-code-path-deploy $branch_name

#. Check if RA is up to date compared to the Production environment
   using Git commands. The script commands check the Production
   environment’s commit log against what is on the update branch
   ($``branch_name``).

   a. If there are any commits after the inverse grep, the Production
      environment is ahead of the update branch and the current
      Production tag needs to be merged into the update branch
      ($``branch_name``), redeployed to the RA environment, and retested
      before `Step Two <#step-two>`__.
   b. If the result of the inverse grep is blank, continue.

#. Enable LiveDev on RA (using drush/cloudapi):

   .. code-block:: none
   
      drush @sitename.ra ac-environment-livedev action enable

#. Back up the testing environment databases (using drush/cloudapi):

   .. code-block:: none
   
      drush @sitename.test ac-database-instance-backup db_name

#. Copy production databases to the testing environment (using
   drush/cloudapi):

   .. code-block:: none
   
      drush @sitename.prod ac-database-copy db_name ra

#. Tag the update branch and deploy to the testing environment (using
   drush/cloudapi):

   .. code-block:: none
   
      git tag -a -m '' -m 'Tag $update_tag generated automatically from $branch_name' $update_tag $branch_name
      drush @sitename.test ac-code-path-deploy $update_tag

#. If you have not already done so in `Step One <step-one>`__, download
   and install `Registry
   Rebuild <https://www.drupal.org/project/registry_rebuild>`__ for
   ``drush rr``:

   .. code-block:: none
   
      drush pm-download registry_rebuild-7.x   --yes=TRUE --root='\''~/.drush'\'

#. If necessary, determine the website aliases and run ``drush rr``
   against them:

   .. code-block:: none
   
      drush sa @sites --format=json -y
      drush rr   --uri=default

#. Set ``preprocess_js`` and ``preprocess_css`` to ``0`` for all
   websites:

   .. code-block:: none
   
      drush vset preprocess_js 0 --uri=default
      drush vset preprocess_css 0 --uri=default

#. Check the testing environment database(s) for updates:

   .. code-block:: none
   
      drush updatedb-status   --uri=default

#. Update the testing environment database(s):

   .. code-block:: none
   
      drush updatedb --uri=default

#. Disable live development on the RA environment (using
   drush/cloudapi):

   .. code-block:: none
   
      drush @sitename.ra ac-environment-livedev action disable

#. At this point, Acquia RA updates the ticket with the newly created
   tag name and lists the next steps required to proceed to step 3 of
   the process.

Step Three
----------

#. Redeploy the RA Step Two tag to the RA environment (using
   drush/cloudapi):

   .. code-block:: none
   
      drush @sitename.ra ac-code-path-deploy $update_tag

#. Grab the variables from the Step Two tag git log:

   .. code-block:: none
   
      cd /var/www/html/sitegroup.ra/docroot/.. && cd /var/www/repo/sitegroup;git log tags/$update_tag

#. Check if RA is up to date compared to the Production environment with
   the following Git commands. The script commands check the Production
   environment’s commit log against what is on the update tag
   ($``update_tag``). This is the same process as used in Step Two.
#. Production databases are backed up (using drush/cloudapi):

   .. code-block:: none
   
      drush @sitename.ra ac-database-instance-backup db_name

#. Deploy ``update_tag`` to the Production environment (using
   drush/cloudapi):

   .. code-block:: none
   
      drush @sitename.ra ac-code-path-deploy $update_tag

#. Determine the website aliases:

   .. code-block:: none
   
      drush sa @sites --format=json -y

#. Check the Production environment database(s) for updates:

   .. code-block:: none
   
      drush updatedb-status   --uri=default

#. Update the Production environment database(s):

   .. code-block:: none
   
      drush updatedb --uri=default

#. Enable Live Development on the RA environment (using drush/cloudapi):

   .. code-block:: none
   
      drush @sitename.ra ac-environment-livedev action enable

#. Merge ``update_tag`` into customer selected repository branch (using
   drush/cloudapi) in RA environment:

   .. code-block:: none
   
      git merge origin/ -m "initials: Some commit message"

#. Disable live development on RA environment (using drush/cloudapi):

   .. code-block:: none
   
      drush @sitename.ra ac-environment-livedev action disable

#. At this point, Acquia RA updates the ticket to inform that the
   process was completed successfully and, if applicable, that the
   branch has been merged back into the specified development branch
   (typically ``master``).
