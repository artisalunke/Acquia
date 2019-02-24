.. include:: /common/global.rst

Git best practices on |acquia-product:edg|
==========================================

You should treat your Git repository that is hosted by Acquia as a
repository for build artifacts created as part of your continuous
integration (CI) setup, with your chosen workflow determining how direct
changes are prepared for inclusion through CI. Depending on the size of
your team, Acquia recommends that you use either the `feature branch
workflow <#feature>`__ or the `gitflow workflow <#gitflow>`__ as you
develop and maintain your |acquia-product:edg| code.

|Learning Services logo|\ *For additional information, visit
`|acquia-product:aa| <https://customers.acquiacademy.com/>`__ (sign-in
required) for the `|acquia-product:edg| Code Management
Concepts <https://customers.acquiacademy.com/catalog/info/id:418>`__
video tutorial.*

For more information about using Git, including clients and basic
commands, see `Using Git </acquia-cloud/develop/repository/git>`__.

.. _feature:

Feature branch workflow
-----------------------

The `feature branch
workflow <https://www.atlassian.com/git/tutorials/comparing-workflows#feature-branch-workflow>`__
is a development style that is well-suited for small teams, which
encourages having all feature development work take place on a dedicated
branch of your Git repository, instead of committing locally to the
standard ``master`` branch. A sample workflow is as follows:

#. A developer creates a new branch (based on the ``master`` branch) to
   start work on a new feature.
#. When the work is completed, the feature branch is pushed back to the
   ``origin``, which is the remote of the developer's forked repository.
#. The developer opens a pull request against ``master``, giving other
   team members the chance to review the developer's work.
#. After the developer's work is accepted, it is merged into the
   ``master`` branch.

Larger teams should instead consider the `Gitflow workflow <#gitflow>`__
as it provides better release management than the simpler feature branch
workflow.

.. _gitflow:

Gitflow workflow
----------------

The `Gitflow
workflow <https://www.atlassian.com/git/tutorials/comparing-workflows#gitflow-workflow>`__
extends the feature branch workflow by requiring developers to submit
pull requests against a ``develop`` branch which serves as an
integration branch for new feature, while maintaining a stable
``master`` branch that remains in a good state.

Here is a description of a sample workflow based on Gitflow:

#. A developer creates a new branch (based on an up-to-date ``develop``
   branch) to start work on a new feature.
#. When the developer completes work, the feature branch is pushed back
   to the ``origin``, which is the remote of the developer's forked
   repository.
#. The developer opens a pull request against the ``develop`` branch,
   giving other team members the chance to review the developer's work
   prior to merging into the ``develop`` branch.
#. After the pull request is approved and the features merged into the
   ``develop`` branch, a new ``release`` branch is created off of the
   ``develop`` branch.
#. The development team continues to create feature branches off of the
   ``develop`` branch, while the release team prepares the ``release``
   branch to add only what is necessary for the release.
#. As part of releasing the code, the ``release`` branch is merged back
   into ``master``.
#. The ``develop`` branch is rebased onto ``master`` to incorporate the
   changes made in the latest release.

In this development strategy, any needed hotfixes are merged directly
into a ``hotfix`` branch, which can then be merged with ``master``.

.. |Learning Services logo| image:: https://cdn2.webdamdb.com/1280_M8mezAoljs55.png?1526475704
   :class: no-sb float-left
   :width: 36px
