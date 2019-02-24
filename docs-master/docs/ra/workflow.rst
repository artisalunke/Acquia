.. include:: /common/global.rst

Using the recommended workflow
==============================

Acquia recommends that you have the following working environments, in
addition to the RA environment provided by Acquia:

.. list-table::
  :header-rows: 1

  * - Environment
    - Description
  * - **Production (Prod)**
    - This environment contains your live code. No testing takes place here, and
      all production code is run from a tag, not a branch.
  * - **Staging (Stage)**
    - Acquia uses this environment to either deploy and test small changes or
      security updates, or to perform a final test of a development branch or tag
      before going live. Your staging and production environments should be on the
      same tag, except when a new tag is being tested on staging for imminent
      deployment to production.
  * - **Development (Dev)**
    - Your development environment is where active development and testing
      occurs. Development should be on a branch or ``master`` unless the environment
      is needed for parallel testing. Development branches are merged into either
      ``master`` only when you are ready to test on your staging environment as a
      precursor to live deployment on production.
  * - **Remote Administration (RA)**
    - Acquia provides an additional RA environment to facilitate security
      updates. Acquia uses this environment for the proactive process of deploying
      and testing security updates before deploying them to production. Acquia
      will regularly overwrite the code and databases on the RA environment. This
      environment should be used only for testing security update branches. For
      more information about this environment, see
      `Remote Administration environment </ra/environment>`__.

Version control system (VCS) and workflow
-----------------------------------------

Acquia recommends that your VCS workflow has the following attributes:

-  *Master (Git) is always a stable, up-to-date codebase.*
   This means that ``master`` is immediately deployable to production
   unless updates are in process. The ``master`` is deployed to your
   development environment unless testing is in process.
-  *Branches are used for developing and testing new code and updates.*
   Branches will be taken from the production tag. Acquia labels
   branches according to the function, the date and time started (for
   example, ``AcquiaRA-2018-02-12-13-14-15``).
-  *Development can happen in parallel on different branches.*
   Acquia recommends keeping track of changes that are eventually merged
   into ``master``, and regularly updating the branch with ``master`` to
   ensure that the working branch is up-to-date. This may or may not be
   possible depending on the type of development on the branch.
   During the automated RA update process, do not merge these changes
   into ``master`` or deploy them to production until after the RA
   update process has completed and the update branch has been merged
   back into the main branch.
-  *All tested and approved branches should be merged back into master.*
   Once fully tested, development branches should be merged into
   ``master``. This ensures that ``master`` always includes updated
   code.
-  *Tags from tested and approved branches (including the master)
   are used for production.*
   Tags are snapshots of your code, frozen in time and unchangeable.
   Commits may not be made against a tag. By not modifying tags, you can
   easily revert to a previous tag if an error is discovered on the most
   recent tag.
