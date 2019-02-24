.. include:: /common/global.rst

File connection
===============

You can combine your cloud provider's file storage with
|acquia-product:aj| to store and retrieve data related to a customer
journey. To use a file `adaptor </journey/adaptors>`__ with your
project, you must first connect to your cloud provider by configuring a
*file connection*.

For information about creating, configuring, or testing connections, see
|connections|_.

.. |connections| replace:: Managing \ |acquia-product:aj| \ connections
.. _connections: /journey/connect

.. _properties:

Connection properties
---------------------

The following list describes properties for the file connection:

-  **Type** - Cloud file provider, currently only Amazon S3 (Simple
   Storage Solution)
-  **S3 Bucket** - Your S3 storage bucket name
-  **AWS Access Key ID** - Your AWS access key ID
-  **AWS Secret Access Key** - Your AWS secret access key
