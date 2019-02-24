.. include:: /common/global.rst

Deployments in |acquia-product:edg|
===================================

.. toctree::
   :hidden:
   :glob:

   /site-factory/workflow/deployments/process/
   /site-factory/workflow/deployments/hotfix/
   /site-factory/workflow/deployments/steps/
   /site-factory/workflow/deployments/errors/
   /site-factory/workflow/deployments/acsf-init/

A *deployment* is the process of updating all websites in a
|acquia-product:edg| subscription with updates to its code or
configuration. A deployment can contain customer-initiated codebase
updates, `updates to the |acquia-product:edg| platform that are created
by Acquia's engineering team <#platform>`__, or both.

After you determine what your deployment will contain, you can `perform
the deployment <#perform>`__.

If, during an ongoing deployment process, you determine that the
deployment contains one or more errors, |acquia-product:edg| also
supports the ability to `implement a hotfix for the
deployment <#hotfix>`__.

.. _platform:

Acquia platform updates
-----------------------

Although you are responsible for the feature branches and code updates
that you send to your websites to add features and resolve issues,
Acquia will maintain the |acquia-product:edg| platform and the
`|acquia-product:edg| Connector <https://www.drupal.org/project/acsf>`__
module that websites use to connect to |acquia-product:edg|. Acquia will
notify |acquia-product:edg| subscribers regarding upcoming platform
updates, and details about these updates are available in the `release
notes for |acquia-product:edg| </site-factory/release-notes>`__.

Even though platform fixes should not directly affect your code's
feature branches, you will periodically have to integrate some
Acquia-developed changes into your feature branches or website code.

To verify your platform version number or to determine if maintenance
has completed for your subscription, see `Determining your platform
version </site-factory/workflow/version>`__.

To ensure that websites can connect to |acquia-product:edg| and the
Acquia hosting platform, Acquia requires that websites have the
`|acquia-product:edg| Connector <https://www.drupal.org/project/acsf>`__
module installed and enabled. Certain platform changes to
|acquia-product:edg| can require changes to the |acquia-product:edg|
Connector module to ensure that it continues to allow access or to make
new or improved features available. If a new version of the module is
released, the `release notes </site-factory/release-notes>`__ page for
|acquia-product:edg| will note that you should obtain and install an
updated version of this module.

.. _feature-branch:

Updating your feature branches
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After Acquia releases changes, if you have existing feature branches, be
sure to incorporate any Acquia-created updates into your branches using
your preferred Git workflow method (either by merging or rebasing).

Note

If you use the branch-per-feature method, when you use the instructions
on the `Testing your feature
branches </site-factory/workflow/deployments#feature-branch>`__
documentation page to merge the updated |acquia-product:dgd| with your
code, replace the instruction in step 3 with the following:

``git merge origin/distro --no-ff``

We encourage you to update your branches as soon as possible after we
make a release to ensure that you have access to any new features and
security fixes contained in each update.

.. _perform:

Performing a deployment
-----------------------

Before performing a deployment, you should familiarize yourself with an
`overview of the |acquia-product:edg| deployment
process </site-factory/workflow/deployments/process>`__ to understand
how it updates your hosted websites. For the specific actions you need
to take to take when deploying, see the following pages:

-  `Updating your codebase with the ``acsf-init``
   command </site-factory/workflow/deployments/acsf-init>`__ to prepare
   your codebase for use on |acquia-product:edg|
-  `Scrubbing sensitive data from staged
   sites </site-factory/workflow/scrub>`__
-  `Steps in performing a production
   deployment </site-factory/workflow/deployments/steps>`__ for the
   commands needed to perform a manual deployment
-  Strategies for `resolving codebase update
   errors </site-factory/workflow/deployments/errors>`__

If you identify problems during the deployment process, you can `hotfix
a deployment in progress <#hotfix>`__.

.. _hotfix:

Hotfixing a deployment
----------------------

The |acquia-product:edg| continuous integration workflow is based on the
concept of *failing forward*. If an error in code deployed to your
production environment causes one or more site update failures, you will
need to modify the code to resolve the error, and then redeploy that
code to all of your websites to get them up and running again.

Because of this, the best practice is to `test your codebase
changes </site-factory/workflow/staging>`__ across a representative set
of websites in your staging environment before deploying those changes
to your production environment. If there are code issues with a
deployment directly to your production environment, your websites can
become unavailable to your website visitors for an extended period of
time.

For information about pausing a deployment to apply a hotfix, see
`Hotfixing an |acquia-product:edg|
deployment </site-factory/workflow/hotfix>`__.
