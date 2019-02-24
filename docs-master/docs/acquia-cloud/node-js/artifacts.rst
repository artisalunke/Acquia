.. include:: /common/global.rst

About build artifacts
=====================

Node.js application support in |acquia-product:ac| uses the
|acquia-product:ac| pipelines functionality to build an *artifact* that
you can then deploy to your environment.

Each artifact has a name, which enables you to select a specific
artifact by that name in the
`deployment </acquia-cloud/node-js/workflow>`__ phase. When you deploy,
the most recently built artifact will be at the top of the list. The
default naming convention for node artifacts is as follows:

``[git branch]@[commit hash]``

This can cause issues, as commits can be amended. This can result in two
artifacts with the same name but with different comments.

It is possible to set a default name for your artifact by adding
configurations to your ``yaml`` file. To do this, complete the following
steps:

#. Edit your build definition file.
#. Find the following line in the file:

   ``- pipelines-artifact start``

#. Edit the line by adding the ``PIPELINE_VCS_PATH`` and
   ``PIPELINE_GIT_HEAD_REF`` options to your start command, similar to
   the following:

   ``- PIPELINE_VCS_PATH=artifact PIPELINE_GIT_HEAD_REF=example pipelines-artifact start``

#. Save the build definition file.

Using this example, your artifact name will become ``artifact@example``
rather than ``branch@commit``.
