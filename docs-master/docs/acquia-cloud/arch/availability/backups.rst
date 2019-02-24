.. include:: /common/global.rst

|acquia-product:ac| backups
===========================

Acquia maintains a comprehensive backup solution that includes
application code, static files, and databases. Integrated backup
facilities use Amazon’s Elastic Block Store (EBS) and Simple Storage
Service (S3).

.. _automatic:

Automatic snapshots for disaster recovery
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|acquia-product:ac| takes hourly snapshots of the passive master
database, file system, and code repository. These snapshots are
programmatically stored in Amazon S3 buckets (Amazon's highly available
cloud storage) and used to restore an application in the case of
multiple disk failure or total data center loss. Backup data stored in
Amazon S3 is maintained in the same region (for example, US-East,
US-West, or EU-East) where the production application is located. Amazon
S3 repositories are distributed amongst multiple Availability Zones
(data centers) and multiple devices within each Availability Zone for
redundancy.

|acquia-product:ac| retains disaster recovery snapshots on the following
schedule:

-  The four most recent hourly snapshots
-  Daily snapshots that are retained for one week
-  Weekly snapshots that are retained for one month
-  Monthly snapshots that are retained for three months

Acquia does not provide customer access to these snapshots and will not
use these snapshots to restore applications due to either data loss or
deletion by customers.

|Backups|

.. _customer:

Customer on-demand backups
~~~~~~~~~~~~~~~~~~~~~~~~~~

Customers have full server access to implement their own on-demand
backups of code, files, and database content. To assist, Acquia provides
the previous three days' database backups (dumps of the MySQL database)
to |acquia-product:ac| customers using the |acquia-product:ui| or `Cloud
API </acquia-cloud/api>`__. Additionally, customers may make on-demand
backups of any database at any time on the Workflow tab of the
|acquia-product:ac| user interface, or through SSH/SCP.
|acquia-product:edg| customers can also `make
backups </site-factory/manage/website/backup>`__ using the
|acquia-product:edg| interface.

|acquia-product:ac| keeps your on-demand backups until you delete them.
Your backup copies count against the storage space of your account.
Customers may download database backups and restore a previous backup on
the Backups tab of the |acquia-product:ac| user interface.

At the Drupal code layer, customers can manage and deploy their
customer-developed code using Acquia’s code repository service (Git).
These services allow for rollback and redeployment of Drupal code,
effectively backing up the application's code.

To ensure your organization's ability to access your application's code,
settings, database, and files during a major service interruption or a
disaster, Acquia recommends that you use the
|acquia-product:ac|-provided interfaces to copy this data to a local or
cloud storage location independent of Acquia on a regular basis, or
after you have deployed changes to the |acquia-product:ac| platform. You
should also periodically check to make sure that backups are being
successfully completed and test your ability to restore applications
from a backup copy.

.. |Backups| image:: https://cdn4.webdamdb.com/1280_42AdB3Ibw31.png?1526475697
   :class: no-sb align-center
   :width: 590px
   :height: 358px
