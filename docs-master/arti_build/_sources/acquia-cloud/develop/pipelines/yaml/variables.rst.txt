.. include:: /common/global.rst

Creating a custom variable for job tracking
===========================================

As part of building scripts for your |acquia-product:ac| application,
you may need a custom variable that provides the full URL to a specific
job in the pipeline. Because the job ID and application ID are both
provided in a job's output, it is possible to combine them into a custom
variable in your `build definition
file </acquia-cloud/develop/pipelines/yaml>`__.

.. _id:

Obtaining the application ID and job ID
---------------------------------------

The UUIDs for your ``PIPELINE_APPLICATION_ID`` and ``PIPELINE_JOB_ID``
are available in the **Initialization** section of an pipelines job's
log, and appear similar to the following:

``export PIPELINE_APPLICATION_ID='11111111-2222-3333-4444-555555555555' export PIPELINE_JOB_ID='66666666-7777-8888-9999-000000000000'``

.. _job-url:

Obtaining the job URL
---------------------

To have a job's full URL be made available for use as a variable called
``PIPELINE_JOB_URL``, add the following line to the ``VARIABLES``
section of your build definition file:

``PIPELINE_JOB_URL: "https://cloud.acquia.com/app/develop/applications/${PIPELINE_APPLICATION_ID}/pipelines/jobs/${PIPELINE_JOB_ID}"``
